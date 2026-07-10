[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-Development-orange.svg)](#)

# music-stem-separator

Ferramenta open source em Python para remover vocais ou instrumentais de músicas com uma interface web simples.

## Funcionalidades

- Upload de `.mp3`, `.wav` ou `.flac`
- Validação de **tamanho** e **duração** do arquivo
- Separa em:
  - **Vocais** (`*_vocals.mp3`)
  - **Instrumental** (`*_instrumental.mp3`)
- Interface web com dois players sincronizados e controle de volume independente + download

## Início Rápido

Para setup e instalação detalhados, veja [Documentação Completa](docs/README.md).

```bash
cd seu-projeto
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python web/app.py
```

Abra: `http://127.0.0.1:5173`

## Documentação

- **[Setup](docs/SETUP.md)** - Instalação e configuração
- **[Estrutura do Projeto](docs/ESTRUTURA.md)** - Organização de pastas
- **[Como Usar](docs/README.md)** - Guia de uso
- **[Contribuindo](docs/CONTRIBUINDO.md)** - Como contribuir

## Notas

- No **macOS**, decodificação MP3 usa `afconvert` (built-in), sem necessidade de FFmpeg
- Primeira execução pode precisar baixar pesos do modelo Demucs

## Licença

MIT — veja `LICENSE`.
