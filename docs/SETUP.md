# Setup e Configuração

## Requisitos do Sistema

- **Python**: 3.8 ou superior
- **pip**: Gerenciador de pacotes Python
- **Espaço em disco**: ~500MB (para modelos Demucs)

## Instalação Passo a Passo

### 1. Preparar o Ambiente

```bash
# Navegue até o diretório do projeto
cd caminho/para/music-stem-separator
```

### 2. Criar Ambiente Virtual

```bash
# macOS e Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python web/app.py
```

A aplicação estará disponível em: **http://127.0.0.1:5173**

## Configurações Específicas por SO

### macOS

✅ **Sem necessidade de FFmpeg**
- Usa `afconvert` nativo do sistema
- MP3 decodificado automaticamente

⚠️ **SSL/Certificados**
- Se encontrar erro de certificado na primeira execução:
  ```bash
  /Applications/Python\ 3.x/Install\ Certificates.command
  ```

### Linux

📋 **Instalação de FFmpeg**
```bash
# Debian/Ubuntu
sudo apt-get install ffmpeg

# Fedora
sudo dnf install ffmpeg
```

### Windows

📋 **Instalação de FFmpeg**
1. Baixe em: https://ffmpeg.org/download.html
2. Extraia e adicione ao PATH
3. Ou use: `choco install ffmpeg` (com Chocolatey)

## Primeiro Acesso

⏳ **Aguarde**: Na primeira execução, o sistema baixará os pesos do modelo Demucs (~600MB)  
✅ **Pronto**: Após o download, você poderá usar a ferramenta

## Solução de Problemas

| Problema | Solução |
|----------|----------|
| `ModuleNotFoundError` | Certifique-se de ativar o ambiente virtual |
| Porta 5173 em uso | Mude a porta no arquivo `app.py` |
| FFmpeg não encontrado | Instale FFmpeg para seu sistema |
| Erro de SSL/Certificado | Execute o instalador de certificados do Python |

## Próximos Passos

- Leia a [Estrutura do Projeto](ESTRUTURA.md)
- Veja [Como Usar](README.md)
- Conheça [Como Contribuir](CONTRIBUINDO.md)
