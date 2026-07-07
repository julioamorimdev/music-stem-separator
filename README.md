# Music Stem Separator

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Ativo-brightgreen.svg)](#)

Ferramenta open source em Python para separar vocais e instrumentais de músicas com uma interface web intuitiva e moderna.

## 📋 Índice

- [Sobre o Projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Como Usar](#como-usar)
- [Exemplos](#exemplos)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Documentação Detalhada](#documentação-detalhada)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## 🎵 Sobre o Projeto

O **Music Stem Separator** é uma aplicação web que utiliza inteligência artificial (modelo Demucs) para separar automaticamente vocais e instrumentais de arquivos de áudio. A ferramenta oferece uma interface amigável com players sincronizados, controle de volume independente e facilidades para download dos arquivos processados.

Perfeit para:
- Criadores de conteúdo
- Músicos em busca de tracks instrumentais
- Produtores que precisam remixar
- Desenvolvedores interessados em processamento de áudio

## ✨ Funcionalidades

✅ **Upload de áudio flexível**
- Suporta formatos: `.mp3`, `.wav`, `.flac`
- Validação automática de tamanho (máx. 500MB)
- Validação de duração (máx. 30 minutos)

✅ **Separação de stems**
- Extração de **vocais** (`*_vocals.mp3`)
- Extração de **instrumental** (`*_instrumental.mp3`)
- Processamento usando modelo Demucs (IA de ponta)

✅ **Interface web intuitiva**
- Players sincronizados para vocais e instrumental
- Controle de volume independente para cada track
- Preview em tempo real
- Download direto dos arquivos processados

✅ **Otimizações**
- No macOS: decodificação MP3 nativa com `afconvert` (sem FFmpeg)
- Cache inteligente de modelos IA
- Processamento assíncrono

## 🔧 Pré-requisitos

Antes de começar, verifique se possui:

- **Python 3.8+** instalado ([Download](https://www.python.org/downloads/))
- **pip** (gerenciador de pacotes Python)
- **Espaço em disco**: ~2GB para modelos IA + espaço para arquivos de áudio
- **RAM**: Mínimo 4GB recomendado

### Requisitos do Sistema

| Sistema | Requisito | Nota |
|---------|-----------|------|
| macOS | Python 3.8+ | Usa `afconvert` nativo para MP3 |
| Linux | Python 3.8+ | Requer FFmpeg para decodificação MP3 |
| Windows | Python 3.8+ | Requer FFmpeg para decodificação MP3 |

## 📥 Instalação

### 1️⃣ Clone o Repositório

```bash
git clone https://github.com/seu-usuario/music-stem-separator.git
cd music-stem-separator
```

### 2️⃣ Crie um Ambiente Virtual

```bash
# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Instale as Dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ (Opcional) Instale FFmpeg

Se estiver em **Linux** ou **Windows**, instale FFmpeg:

**Ubuntu/Debian:**
```bash
sudo apt-get install ffmpeg
```

**macOS (com Homebrew):**
```bash
brew install ffmpeg
```

**Windows (com Chocolatey):**
```bash
choco install ffmpeg
```

Ou baixe de [ffmpeg.org](https://ffmpeg.org/download.html)

### 5️⃣ Execute a Aplicação

```bash
python web/app.py
```

A aplicação abrirá automaticamente em `http://127.0.0.1:5173`

## 🚀 Como Usar

### Via Interface Web

1. **Acesse a interface**: Abra `http://127.0.0.1:5173` no seu navegador
2. **Faça upload**: Clique em "Selecionar Arquivo" ou arraste um arquivo de áudio
3. **Aguarde o processamento**: A IA processará o áudio (tempo varia com duração)
4. **Ouça e compare**: Use os players para ouvir vocais e instrumental
5. **Faça download**: Clique em "Baixar" para obter os arquivos separados

### Limitações e Restrições

- **Tamanho máximo**: 500MB por arquivo
- **Duração máxima**: 30 minutos
- **Formatos suportados**: MP3, WAV, FLAC
- **Tempo de processamento**: ~2-5 minutos por música (varia com CPU)

## 📚 Exemplos

### Exemplo 1: Processamento Básico

```bash
# Terminal (se houver interface CLI)
python -m stem_separator input.mp3 output_folder/
# Resultados:
# - output_folder/input_vocals.mp3
# - output_folder/input_instrumental.mp3
```

### Exemplo 2: Usando a Aplicação Web

```bash
# Inicie a app
python web/app.py

# Navegador: http://127.0.0.1:5173
# 1. Clique em "Escolher arquivo"
# 2. Selecione sua música (ex: musica.mp3)
# 3. Aguarde o processamento
# 4. Baixe vocais e instrumental
```

### Exemplo 3: Integração com Script Python

```python
from stem_separator import StemSeparator

# Inicializar
separator = StemSeparator()

# Processar arquivo
vocals, instrumental = separator.separate('musica.mp3')

# Salvar resultados
vocals.export('vocais.mp3')
instrumental.export('instrumental.mp3')
```

## 📁 Estrutura do Projeto

```
music-stem-separator/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── LICENSE                   # Licença MIT
├── .gitignore               # Arquivos a ignorar no Git
│
├── web/                     # Aplicação web
│   ├── app.py              # Aplicação Flask/FastAPI principal
│   ├── templates/          # Templates HTML
│   │   └── index.html      # Interface da aplicação
│   └── static/             # Arquivos estáticos
│       ├── css/            # Estilos CSS
│       └── js/             # Scripts JavaScript
│
├── stem_separator/         # Pacote principal
│   ├── __init__.py
│   ├── core.py            # Lógica de separação de stems
│   ├── models.py          # Modelos IA (Demucs)
│   ├── audio/             # Processamento de áudio
│   │   ├── loader.py      # Carregamento de arquivos
│   │   └── exporter.py    # Exportação de áudio
│   └── utils/             # Utilitários
│       ├── validators.py  # Validação de arquivos
│       └── config.py      # Configurações
│
├── tests/                 # Testes automatizados
│   ├── test_core.py
│   └── test_audio.py
│
├── docs/                  # Documentação completa
│   ├── README.md         # Guia de uso detalhado
│   ├── SETUP.md          # Instruções de instalação
│   ├── ESTRUTURA.md      # Explicação de estrutura
│   ├── CONTRIBUINDO.md   # Como contribuir
│   └── API.md            # Documentação da API
│
└── uploads/              # Pasta temporária (gitignored)
    └── [arquivos processados]
```

## 📖 Documentação Detalhada

### Setup e Instalação
Veja [docs/SETUP.md](docs/SETUP.md) para:
- Instalação em diferentes sistemas operacionais
- Configuração de variáveis de ambiente
- Troubleshooting de problemas comuns
- Requisitos específicos por plataforma

### Estrutura do Projeto
Veja [docs/ESTRUTURA.md](docs/ESTRUTURA.md) para:
- Explicação detalhada de cada diretório
- Arquitetura da aplicação
- Fluxo de dados
- Padrões de código

### Guia de Uso
Veja [docs/README.md](docs/README.md) para:
- Tutorial passo a passo
- Recursos avançados
- Troubleshooting
- FAQ (Perguntas Frequentes)

### Contribuindo
Veja [docs/CONTRIBUINDO.md](docs/CONTRIBUINDO.md) para:
- Como reportar bugs
- Como sugerir melhorias
- Processo de contribuição
- Padrões de código e commits

### API Reference
Veja [docs/API.md](docs/API.md) para:
- Documentação completa da API
- Exemplos de uso
- Respostas de erro
- Limites e quotas

## 🔍 Troubleshooting

### Problema: "Module not found"
```bash
# Solução: Ative o ambiente virtual
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Reinstale dependências
pip install -r requirements.txt
```

### Problema: "FFmpeg not found" (Windows/Linux)
```bash
# Instale FFmpeg (veja [Instalação](#instalação))
sudo apt-get install ffmpeg  # Ubuntu
brew install ffmpeg          # macOS
```

### Problema: "CUDA out of memory"
```bash
# Use CPU ao invés de GPU em stem_separator/config.py
# Ou reduza o tamanho do batch
```

### Problema: Primeira execução lenta
```bash
# Normal: modelo Demucs (~750MB) está sendo baixado
# Conexão internet estável recomendada
# Próximas execuções serão mais rápidas
```

## 🤝 Contribuindo

Contribuições são muito bem-vindas! Para contribuir:

1. **Faça um Fork** do repositório
2. **Crie uma branch** para sua feature (`git checkout -b feature/MinhaFeature`)
3. **Commit suas mudanças** (`git commit -m 'Adiciona MinhaFeature'`)
4. **Push para a branch** (`git push origin feature/MinhaFeature`)
5. **Abra um Pull Request** com descrição clara

### Diretrizes de Contribuição

- Siga o [PEP 8](https://www.python.org/dev/peps/pep-0008/) para Python
- Escreva testes para novas funcionalidades
- Atualize a documentação conforme necessário
- Use commits descritivos em português
- Veja [CONTRIBUINDO.md](docs/CONTRIBUINDO.md) para mais detalhes

## 🐛 Reportando Bugs

Encontrou um bug? Abra uma [issue](https://github.com/seu-usuario/music-stem-separator/issues) com:

- Descrição clara do problema
- Passos para reproduzir
- Versão do Python e SO
- Screenshots (se aplicável)
- Logs de erro

## 💡 Sugestões de Melhorias

Tem uma ideia? Abra uma [discussion](https://github.com/seu-usuario/music-stem-separator/discussions) ou issue com tag `enhancement`.

## 📋 Roadmap

- [ ] Suporte a batch processing (múltiplos arquivos)
- [ ] Modelos de IA alternativos (Spleeter, Umx)
- [ ] API REST completa com autenticação
- [ ] Desktop app (Electron)
- [ ] Integração com Spotify
- [ ] Suporte a outros idiomas na interface

## 🤖 Tecnologias Utilizadas

- **Backend**: Python 3.8+, Flask/FastAPI
- **IA/ML**: Demucs (Facebook Research)
- **Processamento de Áudio**: librosa, pydub
- **Frontend**: HTML5, CSS3, JavaScript
- **Gerenciamento de Pacotes**: pip, requirements.txt

## 📄 Licença

Este projeto está licenciado sob a **Licença MIT** — veja o arquivo [LICENSE](LICENSE) para detalhes.

### O que isso significa?

- ✅ Usar comercialmente
- ✅ Modificar o código
- ✅ Distribuir
- ✅ Usar privadamente
- ❌ Responsabilidade limitada
- ❌ Sem garantias

**Exigência**: Incluir cópia da licença em distribuições

## 📞 Contato e Suporte

- **Issues**: [GitHub Issues](https://github.com/seu-usuario/music-stem-separator/issues)
- **Discussions**: [GitHub Discussions](https://github.com/seu-usuario/music-stem-separator/discussions)
- **Email**: seu-email@exemplo.com

## ⭐ Apoie o Projeto

Se este projeto foi útil para você:

- ⭐ Deixe uma star no repositório
- 🔗 Compartilhe com amigos e colegas
- 💬 Deixe feedback e sugestões
- 🤝 Contribua com código ou documentação
- 📢 Mencione em seus projetos

## 🙏 Agradecimentos

- Ao time da [Facebook Research](https://github.com/facebookresearch/demucs) pelo modelo Demucs
- À comunidade open source Python
- A todos os contribuidores deste projeto

---

**Última atualização**: Janeiro 2024

**Versão**: 1.0.0

Feito com ❤️ por [Seu Nome/Seu Time]