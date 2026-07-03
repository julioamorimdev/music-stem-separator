# Como Contribuir

Obrigado por considerar contribuir ao **music-stem-separator**! Aqui estão algumas orientações simples.

## Tipos de Contribuição

### 🐛 Reportar Bugs

1. Verifique se o bug já foi reportado
2. Se não, abra uma **Issue** descrevendo:
   - Versão do Python e SO
   - Passos para reproduzir
   - Comportamento esperado vs. real

### 💡 Sugerir Melhorias

- Abra uma **Issue** com o prefixo `[FEATURE]`
- Descreva por que seria útil
- Exemplos de uso (se aplicável)

### 📝 Enviar Código

1. **Fork** o repositório
2. Crie uma branch: `git checkout -b minha-feature`
3. Faça as mudanças
4. Teste localmente
5. Commit: `git commit -m "Adiciona [descrição]"`
6. Push: `git push origin minha-feature`
7. Abra um **Pull Request**

## Diretrizes

### Código
- Mantenha a estética existente
- Use nomes descritivos em português/inglês
- Adicione comentários quando necessário
- Teste seu código antes de enviar

### Commits
- Mensagens claras e concisas
- Um commit por funcionalidade
- Use prefixos: `[fix]`, `[feature]`, `[docs]`, `[refactor]`

### Pull Requests
- Descreva as mudanças
- Linke Issues relacionadas
- Inclua screenshots se relevante (UI)

## Áreas para Contribuição

✅ Correção de bugs  
✅ Novas funcionalidades  
✅ Melhoria de performance  
✅ Melhor documentação  
✅ Testes automatizados  
✅ Suporte a novos formatos  

## Desenvolvimento Local

```bash
# Clone seu fork
git clone https://github.com/seu-usuario/music-stem-separator.git

# Configure o ambiente
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Teste
python -m pytest tests/

# Execute
python web/app.py
```

## Questões?

- Abra uma **Discussion** no repositório
- Consulte a [Documentação](README.md)
- Veja [Setup](SETUP.md) para detalhes técnicos

## Código de Conduta

Sej respeitoso e inclusivo com todos os contribuidores. Comportamento abusivo não será tolerado.

Obrigado por contribuir! 🎉
