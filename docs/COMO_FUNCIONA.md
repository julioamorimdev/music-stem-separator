# Como funciona Music Stem Separator

## Visão geral

Music Stem Separator usa **inteligência artificial** (especificamente um modelo chamado **Demucs**) para analisar uma música e separar seus componentes principais:

- **Vocals** — a voz do cantor
- **Instrumental** — toda a música sem a voz (batida, violão, sintetizadores, etc)

## O que é Demucs?

**Demucs** é um modelo de IA desenvolvido pelo Facebook/Meta que foi treinado com milhões de músicas. Ele aprendeu a reconhecer padrões de:
- Como soa uma voz humana
- Como soa instrumentação

Quando você envia uma música, o Demucs analisa e separa esses elementos.

## Fluxo simplificado

```
1. Você faz upload de uma música (MP3, WAV ou FLAC)
                    ↓
2. A ferramenta valida:
   - Tamanho do arquivo (não pode ser muito grande)
   - Duração da música (muito longa pode travar)
                    ↓
3. O modelo Demucs processa a música
   (pode levar minutos dependendo do tamanho)
                    ↓
4. Você recebe 2 arquivos:
   - *_vocals.mp3 (só a voz)
   - *_instrumental.mp3 (sem a voz)
                    ↓
5. Na interface, você pode:
   - Ouvir os dois em tempo real
   - Controlar volume independentemente
   - Download dos arquivos
```

## Por que funciona bem?

- O modelo foi treinado com muitos tipos de música
- Usa redes neurais profundas para separação espectral
- Mesmo com vozes procesadas, consegue separar bem

## Limitações

- **Vozes muito processadas** (muito reverb, efeitos) podem sair mais fracas
- **Instrumentais muito próximos da voz** (flauta, violino agudo) podem vazard na separação
- **Qualidade de entrada** afeta a saída (MP3 com baixa bitrate produz resultados piores)

## Alternativas técnicas

Existem outros modelos como Spleeter, HDEMUCS, mas Demucs oferece melhor custo-benefício entre qualidade e velocidade.
