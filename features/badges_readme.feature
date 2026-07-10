Feature: Badges de Credibilidade no README
  Como visitante do repositório
  Quero visualizar badges de licença, versão Python e status do projeto
  Para ter confiança na qualidade e manutenção do projeto

  Scenario: Exibir badge de licença MIT
    Given o README.md está aberto
    When procuro pela badge de licença MIT
    Then vejo uma imagem com o texto "MIT License"
    And o link da badge aponta para o arquivo LICENSE

  Scenario: Exibir badge de versão mínima do Python
    Given o README.md está aberto
    When procuro pela badge de versão Python
    Then vejo uma imagem indicando "Python 3.8+" ou superior
    And o link da badge aponta para python.org

  Scenario: Exibir badge de status do projeto
    Given o README.md está aberto
    When procuro pela badge de status
    Then vejo uma imagem com "Stable" ou "In Development"
    And a cor reflete o estado atual do projeto

  Scenario: Badges localizadas no topo do README
    Given o README.md está aberto
    When procuro pelas badges
    Then encontro todas as três badges nos primeiros 5 parágrafos
    And elas aparecem antes da seção de descrição principal

  Scenario: Badges utilizam shields.io
    Given o README.md está aberto
    When inspeciono o código-fonte das badges
    Then todas as imagens vêm de img.shields.io
    And possuem URLs bem-formadas com parâmetros válidos

  Scenario: Badges são responsivas e acessíveis
    Given o README.md está aberto
    When renderizo em um navegador
    Then as badges exibem corretamente em dispositivos móveis
    And possuem texto alternativo descritivo (alt text)
    And o contraste de cores atende WCAG AA
