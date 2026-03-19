from __future__ import annotations

import sys
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import asdict
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, render_template, request, send_from_directory
from werkzeug.utils import secure_filename

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR.parent))

from demucs_service import SeparationConfig, get_duration_seconds, separate_to_files  # noqa: E402
UPLOAD_DIR = BASE_DIR / "uploads"
RESULTS_DIR = BASE_DIR / "results"
TMP_DIR = BASE_DIR / "tmp"

ALLOWED_EXTS = {".mp3", ".wav", ".flac"}
MAX_MB = 40  # limite de tamanho do upload (MB)
MAX_SECONDS = 8 * 60  # limite de duração do áudio (segundos)


app = Flask(__name__, static_folder=str(BASE_DIR / "static"), template_folder=str(BASE_DIR / "templates"))
app.config["MAX_CONTENT_LENGTH"] = MAX_MB * 1024 * 1024

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RESULTS_DIR.mkdir(parents=True, exist_ok=True)
TMP_DIR.mkdir(parents=True, exist_ok=True)

executor = ThreadPoolExecutor(max_workers=1)
jobs: dict[str, dict[str, Any]] = {}


def _err(msg: str, status: int = 400):
    return jsonify({"ok": False, "error": msg}), status


def _validate_file(filename: str) -> str | None:
    if not filename:
        return "Arquivo ausente."
    ext = Path(filename).suffix.lower()
    if ext not in ALLOWED_EXTS:
        return f"Formato não suportado ({ext}). Use: {', '.join(sorted(ALLOWED_EXTS))}."
    return None


@app.get("/")
def index():
    return render_template(
        "index.html",
        max_mb=MAX_MB,
        max_seconds=MAX_SECONDS,
        allowed=", ".join(sorted(ALLOWED_EXTS)),
    )


@app.post("/api/jobs")
def create_job():
    f = request.files.get("file")
    if not f:
        return _err("Envie um arquivo no campo 'file'.")
    msg = _validate_file(f.filename or "")
    if msg:
        return _err(msg)

    job_id = uuid.uuid4().hex
    safe_name = secure_filename(f.filename or f"upload{job_id}")
    in_path = UPLOAD_DIR / f"{job_id}_{safe_name}"
    f.save(in_path)

    # valida duração (tempo) – no macOS MP3 usa afconvert por baixo.
    try:
        dur = get_duration_seconds(in_path)
    except Exception as e:
        in_path.unlink(missing_ok=True)
        return _err(f"Não consegui ler o áudio: {e}")

    if dur > MAX_SECONDS:
        in_path.unlink(missing_ok=True)
        return _err(f"Duração acima do limite: {dur:.1f}s (limite: {MAX_SECONDS}s).")

    # device=None escolhe automaticamente (cuda/mps/cpu).
    cfg = SeparationConfig(model_name="htdemucs_ft", device=None)
    jobs[job_id] = {
        "id": job_id,
        "status": "queued",
        "progress": None,
        "input_name": safe_name,
        "duration_seconds": dur,
        "config": asdict(cfg),
        "result": None,
        "error": None,
    }

    def _run():
        jobs[job_id]["status"] = "running"
        try:
            out_dir = RESULTS_DIR / job_id
            vocals, inst = separate_to_files(in_path, out_dir, cfg=cfg, base_name="resultado")
            jobs[job_id]["status"] = "done"
            jobs[job_id]["result"] = {
                "vocals_url": f"/results/{job_id}/{vocals.name}",
                "instrumental_url": f"/results/{job_id}/{inst.name}",
            }
        except Exception as e:
            jobs[job_id]["status"] = "error"
            jobs[job_id]["error"] = str(e)
        finally:
            try:
                in_path.unlink(missing_ok=True)
            except OSError:
                pass

    executor.submit(_run)
    return jsonify({"ok": True, "job": jobs[job_id]})


@app.get("/api/jobs/<job_id>")
def get_job(job_id: str):
    job = jobs.get(job_id)
    if not job:
        return _err("Job não encontrado.", 404)
    return jsonify({"ok": True, "job": job})


@app.get("/results/<job_id>/<path:filename>")
def serve_result(job_id: str, filename: str):
    folder = RESULTS_DIR / job_id
    return send_from_directory(folder, filename, as_attachment=True)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5173, debug=True)

