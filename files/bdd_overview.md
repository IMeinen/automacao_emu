## O que é BDD(Behaviour Driven Development)?

Desenvolvimento Guiado por Comportamento, do inglês Behavior Driven Development, conhecido pela sigla BDD é uma metodologia de desenvolvimento ágil que estimula a participação de todos os membros da equipe, desenvolvedores, analistas e gestores do projeto.

Utilizando o conceito de linguagem ubíqua onde o foco é o fluxo em que o código deve ser escrito, não gerando a necessidade de conhecimentos técnicos, permitindo então que qualquer pessoa com conhecimento técnico ou não possa montar os cenários de teste.

## Dentre as praticas de BDD obtemos:

*Entendimento de todas as partes do processo;
*Documentação viva;
*Redução da perda do tempo de confecção de casos de testes;
*Redução do custo;
*Automação.

## Metodologia:

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd1.png">
</div>

## Palavras-chave:

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd2.png">
</div>

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd3.png">
</div>

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd4.png">
</div>

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd5.png">
</div>

Exemplo:

    Feature: Vender doces

        Para quando uma doce for vendido
        Eu, como vendedor
        Desejo decrementar um item no estoque

    Cenário: Baixa 1 bala do estoque
         Dado que cliente pede 1 bala
         E tenho 10 balas em estoque
         Quando ele compra realiza a compra
         Então eu fico com 9 balas em estoque
         
##  Exemplo de história BDD na automação utilizando Gherkin:

<div align="center">
    <img width="750" src="https://github.com/IMeinen/automacao_emu/blob/master/images/bdd6.png">
</div>

## Melhores práticas:

    • Evitar ter descrições longas, com foco no escopo e contexto (Features);
    • Escolher um simples formato para todas features(template);
    • Não usar linguagem técnica;
    • Manter cenários curtos (evitar muitos “AND” e “BUT” nos passos);
    • Evitar steps conjuntivos(muitos “AND”);
    • Cobrir cenários com caminho feliz e não feliz;
    • Tentar criar steps que possam ser reutilizados(a ideia é ter uma biblioteca de steps de definições);
    • Ter cenários atômicos(rodar independente, sem qualquer dependência de outro cenário.





