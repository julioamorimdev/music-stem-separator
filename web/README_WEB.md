# Interface HTML (upload + mix)

## Rodar

```bash
cd /Users/juliocesardeamorim/Desktop/teste
source .venv/bin/activate
python web/app.py
```

Abra no navegador:

- `http://127.0.0.1:5173`

## O que faz

- Importa um arquivo `.mp3`, `.wav` ou `.flac`
- Valida:
  - **tamanho** (limite em MB)
  - **duração** (limite em segundos)
- Processa com **Demucs `htdemucs_ft`**
- Exibe dois players sincronizados:
  - **Instrumental** (slider de volume)
  - **Vocais** (slider de volume)
- Permite **baixar** as duas faixas separadas

## Limites / Configuração

Edite em `web/app.py`:

- `MAX_MB`
- `MAX_SECONDS`
- `ALLOWED_EXTS`

