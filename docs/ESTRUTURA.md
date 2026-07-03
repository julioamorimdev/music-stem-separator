# Estrutura do Projeto

## Árvore de Diretórios

```
music-stem-separator/
├── docs/                    # Documentação (markdown)
│   ├── README.md           # Guia principal
│   ├── SETUP.md            # Instalação e configuração
│   ├── ESTRUTURA.md        # Este arquivo
│   └── CONTRIBUINDO.md     # Guia de contribuição
│
├── web/                     # Aplicação web
│   ├── app.py              # Arquivo principal Flask/FastAPI
│   ├── templates/          # Templates HTML
│   └── static/             # Assets (CSS, JS)
│
├── music_separator/        # Lógica principal
│   ├── __init__.py
│   ├── separator.py        # Classe de separação de stems
│   └── utils.py            # Funções utilitárias
│
├── tests/                  # Testes automatizados
│   └── test_separator.py   # Testes da lógica principal
│
├── README.md               # README raiz
├── requirements.txt        # Dependências Python
├── LICENSE                 # Licença MIT
└── .gitignore              # Arquivos ignorados no Git
```

## Descrição das Pastas

### `/docs`
📚 **Documentação do projeto**
- Guias de instalação
- Como usar
- Estrutura do projeto
- Contribuições

### `/web`
🌐 **Interface web e backend**
- `app.py`: Servidor principal
- `templates/`: Páginas HTML
- `static/`: Estilos e scripts JavaScript

### `/music_separator`
🎵 **Lógica de separação de áudio**
- `separator.py`: Classe principal com Demucs
- `utils.py`: Funções auxiliares de processamento

### `/tests`
✅ **Testes automatizados**
- Validação de funcionalidades
- Testes de separação de stems

## Arquivos Importantes

| Arquivo | Função |
|---------|--------|
| `requirements.txt` | Lista de dependências Python |
| `README.md` | Documentação principal |
| `LICENSE` | Licença MIT |
| `.gitignore` | Arquivos excluídos do Git |

## Fluxo de Funcionamento

```
Usuário
   ↓
Web UI (HTML/JS)
   ↓
app.py (Backend)
   ↓
separator.py (Demucs)
   ↓
Arquivo de Áudio
   ↓
Vocals.mp3 + Instrumental.mp3
   ↓
Download para Usuário
```

## Dependências Principais

- **Flask/FastAPI**: Framework web
- **Demucs**: Modelo de separação de áudio
- **librosa**: Processamento de áudio
- **PyTorch**: Machine learning (requerido por Demucs)

## Próximos Passos

- [Setup](SETUP.md) - Instale e configure o projeto
- [README](README.md) - Saiba como usar
- [Contribuindo](CONTRIBUINDO.md) - Como colaborar
