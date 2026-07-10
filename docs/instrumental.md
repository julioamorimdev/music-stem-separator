# Remover vocais (Demucs)

## Uso

```bash
cd /Users/juliocesardeamorim/Desktop/teste
source .venv/bin/activate
python remover_vocais.py
```

Saída: pasta `instrumentais_resultado/` com `parte1_instrumental.mp3` e `parte2_instrumental.mp3`.

## Dependências

- Python 3.10+ (venv com `demucs`, `soundfile`)
- **macOS:** `afconvert` (já incluído) para ler MP3
- **Outros:** FFmpeg para MP3, ou use arquivos `.wav`

## Modelo `htdemucs_ft` (primeira execução)

Se o download pelo Python falhar (SSL), baixe os 4 arquivos para  
`~/.cache/torch/hub/checkpoints/`:

```bash
BASE=https://dl.fbaipublicfiles.com/demucs/hybrid_transformer
cd ~/.cache/torch/hub/checkpoints
for f in f7e0c4bc-ba3fe64a.th d12395a8-e57c48e6.th 92cfc3b6-ef3bcb9c.th 04573f0d-f3cf25b2.th; do
  curl -LO "$BASE/$f"
done
```

## Tempo

Faixas longas (~1 h) podem levar de **30 min a várias horas** em CPU; em Apple Silicon use `-d mps` (padrão automático no Mac).

## Qualidade

`-n htdemucs_ft` é o modelo fine-tuned (alta precisão). Para mais estabilidade: `--shifts 5` (bem mais lento).
