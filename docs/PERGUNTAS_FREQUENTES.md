# Perguntas Frequentes (FAQ)

## Instalação

### P: Preciso de FFmpeg?
**A:** Apenas no Windows ou Linux. No macOS, usa `afconvert` nativo.

### P: Quanto espaço preciso?
**A:** ~2GB:
- Dependências: ~500MB
- Modelo Demucs: ~500MB
- Espaço temporário: variável (tamanho dos arquivos)

### P: Qual versão Python?
**A:** Python 3.8 ou superior. Verifique com `python --version`.

### P: Posso usar num servidor (VPS)?
**A:** Sim, mas não há interface gráfica nativa. Rodará em headless (linha de comando).

---

## Uso da aplicação

### P: Qual é o tamanho máximo de arquivo?
**A:** Depende da sua RAM. Recomendado até ~200MB. Arquivos maiores podem travar.

### P: Quanto tempo leva para processar?
**A:** 3-5 minutos por 3-5 minutos de música (varia com o computador).

### P: Qual formato é melhor: MP3, WAV ou FLAC?
**A:** FLAC > WAV > MP3 (em termos de qualidade). MP3 é mais comprimido, pode perder qualidade. Use FLAC ou WAV se tiver a opção.

### P: A separação é perfeita?
**A:** Não. Pode haver:
- Vozes fracas em áreas com muitos instrumentos
- Instrumentos (como violino) vazando no vocal
- Ruído de fundo em ambos os arquivos

É uma tecnologia em contínua melhoria.

### P: Posso processar múltiplas músicas?
**A:** Uma por vez. Processe uma, baixe, depois faça upload da próxima.

---

## Problemas

### P: Erro "SSL: CERTIFICATE_VERIFY_FAILED" ao iniciar?
**A:** Ver `README_INSTRUMENTAL.md` no repositório raiz para solução.

### P: Porta 5173 já em uso?
**A:** Outro programa está usando a porta. Edite `web/app.py` e altere:
```python
app.run(host='127.0.0.1', port=5174)  # Altere 5173 para 5174
```

### P: A música demora muito para processar?
**A:** Normal para arquivos grandes. Use uma música menor para testar.

### P: Onde são salvos os arquivos processados?
**A:** Na pasta onde você iniciou a aplicação (diretório do projeto).

---

## Técnico

### P: Posso treinar o modelo com minhas próprias músicas?
**A:** Não diretamente. Demucs usa um modelo pré-treinado. Seria necessário muita computação.

### P: O código é realmente open source?
**A:** Sim! Licença MIT — você pode usar, modificar e redistribuir.

### P: Posso contribuir melhorias?
**A:** Sim! Abra um pull request no repositório GitHub.

---

## Não encontrou resposta?

Abra uma **issue** no repositório:
https://github.com/julioamorimdev/music-stem-separator/issues
