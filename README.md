# music-stem-separator

Open source Python tool to remove vocals or instrumentals from songs with a simple web interface.

## Features

- Upload `.mp3`, `.wav` or `.flac`
- Validates **file size** and **duration**
- Separates into:
  - **Vocals** (`*_vocals.mp3`)
  - **Instrumental** (`*_instrumental.mp3`)
- Web UI with two synced players and independent volume controls + download

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

