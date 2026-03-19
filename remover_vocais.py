#!/usr/bin/env python3
"""
Remove vocais de .mp3 com precisão (Demucs htdemucs_ft) — saída instrumental em MP3.

Este script agora usa o módulo `demucs_service.py` (reutilizado também pela interface web).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from demucs_service import SeparationConfig, separate_to_files

DEFAULT_MODEL = "htdemucs_ft"


def main() -> int:
    p = argparse.ArgumentParser(description="Instrumental sem vocais (Demucs)")
    p.add_argument(
        "-i",
        "--inputs",
        nargs="*",
        default=["parte1.mp3", "parte2.mp3"],
    )
    p.add_argument("-o", "--output-dir", default="instrumentais_resultado")
    p.add_argument("-n", "--model", default=DEFAULT_MODEL)
    p.add_argument("-d", "--device", default=None)
    p.add_argument("--shifts", type=int, default=1, help="Mais shifts = melhor, mais lento")
    p.add_argument("--overlap", type=float, default=0.25)
    p.add_argument("--segment", type=int, default=None, help="Limite de segmento (memória)")
    p.add_argument("-j", "--jobs", type=int, default=0)
    args = p.parse_args()

    base = Path(__file__).resolve().parent
    saida = base / args.output_dir
    cfg = SeparationConfig(
        model_name=args.model,
        device=args.device,
        shifts=args.shifts,
        overlap=args.overlap,
        segment=args.segment,
        jobs=args.jobs,
    )

    n = 0
    for nome in args.inputs:
        arq = base / nome if not Path(nome).is_absolute() else Path(nome)
        if not arq.is_file():
            print(f"Aviso: não encontrado: {arq}", file=sys.stderr)
            continue
        try:
            vocals_path, inst_path = separate_to_files(arq, saida, cfg=cfg, base_name=arq.stem)
            print(f"OK → {inst_path}")
            n += 1
        except Exception as e:
            print(f"Erro em {arq}: {e}", file=sys.stderr)
            raise
    if n == 0:
        return 1
    print(f"\nConcluído: {n} arquivo(s) em {saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
