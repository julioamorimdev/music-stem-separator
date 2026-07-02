# music-stem-separator

Open source Python tool to remove vocals or instrumentals from songs with a simple web interface.

## Features

- Upload `.mp3`, `.wav` or `.flac`
- Validates **file size** and **duration**
- Separates into:
  - **Vocals** (`*_vocals.mp3`)
  - **Instrumental** (`*_instrumental.mp3`)
- Web UI with two synced players and independent volume controls + download

## Requisitos

- **Python**: 3.8 ou superior
- **Bibliotecas de áudio**:
  - `librosa`: ≥ 0.9.2 (processamento e análise de áudio)
  - `soundfile`: ≥ 0.10.0 (leitura/escrita de arquivos de áudio)
  - `pydub`: ≥ 0.25.1 (manipulação de áudio MP3, WAV, FLAC)
  - `numpy`: ≥ 1.21.0 (operações numéricas)
  - `scipy`: ≥ 1.7.0 (processamento de sinais)
- **Dependências web**:
  - `flask`: ≥ 2.0.0 (framework web)
  - `flask-cors`: ≥ 3.0.10 (suporte a CORS)
- **Separação de stems**:
  - `demucs`: ≥ 4.0.0 (modelo de separação de áudio)

## Quick start (macOS)

```bash
cd /Users/juliocesardeamorim/Desktop/teste
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python web/app.py
```

Open: `http://127.0.0.1:5173`

## Notes

- On **macOS**, MP3 decoding uses `afconvert` (built-in), so you don't need FFmpeg.
- First run may require downloading Demucs model weights. If SSL fails, see `README_INSTRUMENTAL.md`.

## License

MIT — see `LICENSE`.
