# Como usar Music Stem Separator

## Iniciando a aplicação

Ter certeza de que a aplicação está rodando:

```bash
python web/app.py
```

Acesse: `http://127.0.0.1:5173`

## Fazendo upload de uma música

1. Clique no botão **"Upload"** ou arraste um arquivo para a área de upload
2. Selecione um arquivo `.mp3`, `.wav` ou `.flac`
3. Aguarde a validação (verifica tamanho e duração)
4. Pressione **"Processar"** ou **"Separar"**

## Formatos aceitos

| Formato | Extensão | Status |
|---------|----------|--------|
| MP3 | `.mp3` | ✅ Recomendado |
| WAV | `.wav` | ✅ Suportado |
| FLAC | `.flac` | ✅ Suportado |

## Tempo de processamento

- **Música de 3min:** ~30-60 segundos
- **Música de 5min:** ~1-2 minutos
- **Música de 10min:** ~3-5 minutos

(Depende do seu computador)

## Usando a interface de reprodução

Após o processamento, você verá:

### Player duplo
- **Esquerda:** Vocals (a voz)
- **Direita:** Instrumental (a música sem voz)
- Os dois players estão **sincronizados** — começam e param juntos

### Controles
- **Play/Pause** — toca ou pausa ambos ao mesmo tempo
- **Barra de progresso** — arraste para avançar/retroceder
- **Volume independente** — ajuste o volume de cada player separadamente

### Download

Clique em **"Download"** para baixar:
- `nome_original_vocals.mp3`
- `nome_original_instrumental.mp3`

Os arquivos são salvos na sua pasta de downloads.

## Exemplo prático

**Cenário:** Você quer uma versão sem vocal de uma música para praticar.

1. Faça upload do MP3
2. Aguarde o processamento
3. Ouça o resultado no player duplo
4. Se gostar, clique "Download" para guardar a versão instrumental
5. Pronto! Você tem a música sem vocal em `nome_instrumental.mp3`

## Dicas

- **Use MP3 de boa qualidade** (320kbps ou superior) para melhores resultados
- **Músicas mais recentes** costumam separar melhor (modelo foi treinado com música moderna)
- **Paciência:** Primeira execução baixa ~500MB de modelo, leva tempo
