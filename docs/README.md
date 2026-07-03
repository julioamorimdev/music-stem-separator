# Music Stem Separator - Documentação

Ferramenta open source para separação de vocais e instrumentais em músicas.

## O que é?

O **music-stem-separator** é uma aplicação web que permite separar faixas de áudio em:
- **Vocais**: Apenas a voz/vocal da música
- **Instrumental**: Apenas instrumentos (sem vocais)

## Como Funciona?

1. **Upload**: Envie um arquivo de áudio (MP3, WAV ou FLAC)
2. **Processamento**: A ferramenta usa o modelo Demucs para separar os stems
3. **Download**: Baixe as faixas separadas em formato MP3

## Começando

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação Rápida

```bash
# Clone ou navegue até o projeto
cd seu-projeto

# Crie ambiente virtual
python3 -m venv .venv

# Ative o ambiente
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate  # Windows

# Instale dependências
pip install -r requirements.txt

# Execute a aplicação
python web/app.py
```

### Acessar
Abra seu navegador em: **http://127.0.0.1:5173**

## Recursos Principais

✅ Interface web intuitiva  
✅ Dois players sincronizados  
✅ Controle de volume independente  
✅ Validação de arquivo (tamanho e duração)  
✅ Download das faixas separadas  
✅ Suporte a múltiplos formatos  

## Plataformas Suportadas

| Plataforma | Status | Observações |
|-----------|--------|-------------|
| macOS     | ✅ Completo | Usa `afconvert` nativo |
| Linux     | ✅ Completo | Requer FFmpeg |
| Windows   | ✅ Completo | Requer FFmpeg |

## Próximos Passos

- Leia o [Guia de Setup](SETUP.md) para detalhes técnicos
- Conheça a [Estrutura do Projeto](ESTRUTURA.md)
- Veja [Como Contribuir](CONTRIBUINDO.md)
