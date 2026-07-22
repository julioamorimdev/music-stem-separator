# Contribuindo

## Configurar Ambiente

1. Clone o repositório
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o ambiente: `source venv/bin/activate` (ou `venv\Scripts\activate` no Windows)
4. Instale dependências: `pip install -r requirements.txt`

## Rodar Testes

Execute os testes com:
```bash
pytest
```

## Abrir Pull Request

1. Crie uma branch para sua feature: `git checkout -b minha-feature`
2. Faça suas alterações
3. Commit com mensagens claras: `git commit -m "Descrição da alteração"`
4. Push para sua branch: `git push origin minha-feature`
5. Abra uma Pull Request descrevendo suas mudanças

## Diretrizes

- Mantenha o código limpo e bem documentado
- Adicione testes para novas funcionalidades
- Certifique-se de que todos os testes passam antes de submeter a PR
