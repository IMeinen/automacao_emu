Feature: Pesquisar vaga de desenvolvedor no site da Zallpy

  Como um usuário qualquer
  Eu quero acessar o site da Zallpy no Google
  De modo que eu consiga acessar e visualizar suas informações

  Scenario: Pesquisar vaga de desenvolvedor no site da zallpy
    Given que tenho permissão para acessar o Google
    When  acesso o site da Zallpy
    And   seleciono a aba oportunidades verificando vagas de desenvolvedor
    Then  as vagas de desenvolvedor são encontradas com sucesso