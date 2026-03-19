from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

import soundfile as sf
import torch
from demucs.apply import apply_model
from demucs.audio import convert_audio, save_audio
from demucs.pretrained import get_model


@dataclass(frozen=True)
class SeparationConfig:
    model_name: str = "htdemucs_ft"
    device: str | None = None  # "cuda" | "mps" | "cpu" | None(auto)
    shifts: int = 1
    overlap: float = 0.25
    segment: int | None = None
    jobs: int = 0
    mp3_bitrate: int = 320
    mp3_preset: int = 2


def _choose_device(explicit: str | None) -> str:
    if explicit:
        return explicit
    if torch.cuda.is_available():
        return "cuda"
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return "mps"
    return "cpu"


def _has_ffmpeg() -> bool:
    return shutil.which("ffmpeg") is not None


def _mp3_to_wav_macos_afconvert(mp3: Path, wav_out: Path) -> None:
    subprocess.run(
        [
            "afconvert",
            "-f",
            "WAVE",
            "-d",
            "LEI16",
            str(mp3.resolve()),
            str(wav_out.resolve()),
        ],
        check=True,
        capture_output=True,
    )


def _mp3_to_wav_ffmpeg(mp3: Path, wav_out: Path) -> None:
    subprocess.run(
        [
            "ffmpeg",
            "-y",
            "-hide_banner",
            "-loglevel",
            "error",
            "-i",
            str(mp3.resolve()),
            str(wav_out.resolve()),
        ],
        check=True,
    )


def _normalize_and_apply(model, mix: torch.Tensor, cfg: SeparationConfig, device: str) -> torch.Tensor:
    ref = mix.mean(0)
    x = mix.clone()
    x -= ref.mean()
    x /= ref.std() + 1e-8

    sources = apply_model(
        model,
        x[None],
        device=device,
        shifts=cfg.shifts,
        split=True,
        overlap=cfg.overlap,
        progress=True,
        num_workers=cfg.jobs,
        segment=cfg.segment,
    )[0]

    sources *= ref.std()
    sources += ref.mean()
    return sources


def load_audio_as_model_wav(path: Path, *, audio_channels: int, samplerate: int) -> torch.Tensor:
    """
    Retorna tensor float32 no formato (channels, samples), já convertido para
    `samplerate` e `audio_channels` do modelo.

    - MP3 no macOS: usa afconvert (não depende de FFmpeg).
    - MP3 em outros OS: requer FFmpeg.
    """
    path = path.resolve()
    tmp: Path | None = None
    src = path

    if path.suffix.lower() == ".mp3":
        fd, tmp_name = tempfile.mkstemp(suffix=".wav", prefix="demucs_in_")
        os.close(fd)
        tmp = Path(tmp_name)
        if sys.platform == "darwin":
            _mp3_to_wav_macos_afconvert(path, tmp)
        else:
            if not _has_ffmpeg():
                raise RuntimeError("FFmpeg não encontrado para decodificar MP3 neste sistema.")
            _mp3_to_wav_ffmpeg(path, tmp)
        src = tmp

    data, sr = sf.read(str(src), dtype="float32", always_2d=True)
    if tmp and tmp.exists():
        try:
            tmp.unlink()
        except OSError:
            pass

    wav = torch.from_numpy(data.T.copy())
    wav = convert_audio(wav, sr, samplerate, audio_channels)
    return wav


def get_duration_seconds(path: Path) -> float:
    """
    Duração aproximada em segundos (para validação de limite).
    Para MP3 no macOS, faz leitura via afconvert→wav temporário.
    """
    path = path.resolve()
    if path.suffix.lower() != ".mp3":
        info = sf.info(str(path))
        return float(info.frames) / float(info.samplerate)

    if sys.platform != "darwin":
        raise RuntimeError("Cálculo de duração para MP3 sem macOS requer FFmpeg/conversão.")

    fd, tmp_name = tempfile.mkstemp(suffix=".wav", prefix="demucs_dur_")
    os.close(fd)
    tmp = Path(tmp_name)
    try:
        _mp3_to_wav_macos_afconvert(path, tmp)
        info = sf.info(str(tmp))
        return float(info.frames) / float(info.samplerate)
    finally:
        try:
            tmp.unlink(missing_ok=True)
        except OSError:
            pass


def separate_to_files(
    input_audio: Path,
    output_dir: Path,
    *,
    cfg: SeparationConfig = SeparationConfig(),
    base_name: str | None = None,
) -> tuple[Path, Path]:
    """
    Separa `input_audio` em dois arquivos MP3:
    - {base}_vocals.mp3
    - {base}_instrumental.mp3
    Retorna (vocals_path, instrumental_path).
    """
    output_dir = output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    base = base_name or input_audio.stem

    model = get_model(cfg.model_name)
    model.cpu()
    model.eval()
    device = _choose_device(cfg.device)

    mix = load_audio_as_model_wav(
        input_audio,
        audio_channels=model.audio_channels,
        samplerate=model.samplerate,
    )

    sources = _normalize_and_apply(model, mix, cfg, device=device)

    names = list(model.sources)
    if "vocals" not in names:
        raise RuntimeError(f'Modelo sem stem "vocals": {names}')
    iv = names.index("vocals")
    vocals = sources[iv]

    instrumental = torch.zeros_like(sources[0])
    for i, s in enumerate(sources):
        if i != iv:
            instrumental = instrumental + s

    vocals_out = output_dir / f"{base}_vocals.mp3"
    inst_out = output_dir / f"{base}_instrumental.mp3"

    save_audio(
        vocals,
        vocals_out,
        samplerate=model.samplerate,
        bitrate=cfg.mp3_bitrate,
        preset=cfg.mp3_preset,
        clip="rescale",
    )
    save_audio(
        instrumental,
        inst_out,
        samplerate=model.samplerate,
        bitrate=cfg.mp3_bitrate,
        preset=cfg.mp3_preset,
        clip="rescale",
    )
    return vocals_out, inst_out

