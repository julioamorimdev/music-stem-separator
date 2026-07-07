Funcionalidade: API de Saúde
  Como um cliente da API
  Quero verificar o status da aplicação
  Para garantir que o serviço está operacional

  Cenário: Verificar saúde da API com sucesso
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/health
    Então recebo o status 200
    E a resposta contém a chave "version"
    E a resposta contém a chave "model_loaded"
    E o valor de "model_loaded" é um booleano

  Cenário: Versão está no formato correto
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/health
    Então a resposta contém "version" com um valor não-vazio

  Cenário: Modelo carregado indica estado válido
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/health
    Então o valor de "model_loaded" é verdadeiro ou falso

Funcionalidade: API de Formatos
  Como um cliente da API
  Quero conhecer as extensões de arquivo aceitas
  Para enviar arquivos no formato correto

  Cenário: Listar formatos aceitos com sucesso
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/formats
    Então recebo o status 200
    E a resposta contém a chave "formats"
    E "formats" é uma lista

  Cenário: Formatos retornados não estão vazios
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/formats
    Então a lista "formats" contém pelo menos um elemento

  Cenário: Extensões no formato correto
    Dado que a API está em execução
    Quando faço uma requisição GET para /api/formats
    Então cada elemento em "formats" começa com um ponto (.)
