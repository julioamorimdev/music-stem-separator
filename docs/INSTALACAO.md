# Como instalar Music Stem Separator

## Pré-requisitos

- **Python 3.8+** instalado
- **pip** (gerenciador de pacotes Python)
- Aproximadamente **2GB de espaço em disco** (para download do modelo)

## Passo a passo

### 1. Clone ou baixe o repositório

```bash
git clone https://github.com/julioamorimdev/music-stem-separator.git
cd music-stem-separator
```

### 2. Crie um ambiente virtual

Um ambiente virtual isola as dependências do projeto:

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

Este comando instala todas as bibliotecas necessárias (Flask, Demucs, etc).

### 4. Inicie a aplicação

```bash
python web/app.py
```

Você verá uma mensagem como:
```
Running on http://127.0.0.1:5173
```

### 5. Acesse a interface web

Abra seu navegador e acesse:
```
http://127.0.0.1:5173
```

Pronto! A aplicação está rodando.

## Primeira execução

Na primeira vez que usar, a ferramenta baixará automaticamente os **modelos de IA** (~500MB). Isso pode levar alguns minutos dependendo de sua conexão.

**macOS:** MP3 usa `afconvert` nativo, sem necessidade de FFmpeg adicional.

## Solução de problemas

### Erro SSL ao baixar modelos?
Ver `README_INSTRUMENTAL.md` no repositório raiz.

### Porta 5173 já em uso?
Edite `web/app.py` e altere a porta na última linha.

### Versão Python incorreta?
Verifique com:
```bash
python --version
```
Deve ser 3.8 ou superior.
