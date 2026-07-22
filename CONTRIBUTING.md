# Guia de Contribuição

Obrigado por contribuir! Este guia explica como preparar seu ambiente, testar e submeter alterações.

## Configurar Ambiente

1. Faça um fork e clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/projeto.git
   cd projeto
   ```

2. Instale as dependências:
   ```bash
   npm install
   ```
   (ou `pip install -r requirements.txt`, `yarn install`, conforme o projeto)

3. Crie uma branch para sua feature:
   ```bash
   git checkout -b minha-feature
   ```

## Rodar Testes

Antes de submeter, execute os testes:

```bash
npm test
```

Certifique-se de que todos os testes passam e o código segue o padrão do projeto.

## Abrir um Pull Request

1. Commit suas mudanças com mensagens claras:
   ```bash
   git add .
   git commit -m "Descrição breve da mudança"
   ```

2. Push para seu fork:
   ```bash
   git push origin minha-feature
   ```

3. Abra um Pull Request no repositório principal com:
   - Título descritivo
   - Explicação do que foi alterado e por quê
   - Referência a issues relacionadas (se houver)

4. Aguarde revisão da equipe

## Dúvidas?

Abra uma issue para discussões ou entre em contato com os mantenedores.
