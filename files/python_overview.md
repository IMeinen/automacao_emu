## O que é Python?

Python é uma linguagem de programação criada por Guido van Rossum em 1991. Os objetivos do projeto da linguagem eram: produtividade e legibilidade. Em outras palavras, Python é uma linguagem que foi criada para produzir código bom e fácil de manter de maneira rápida. Entre as características da linguagem que ressaltam esses objetivos estão:

    Baixo uso de caracteres especiais, o que torna a linguagem muito parecida com pseudo-código executável;
    O uso de identação para marcar blocos;
    Python é uma boa linguagem para começar a aprender programação
    Coletor de lixo para gerenciar automaticamente o uso da memória;

## Declaração de variável:

Diferente de outras linguagens, Python não precisa dizer qual o tipo da variável (Integer, Float,etc)
Exemplo:
    nome = “João”
    numero_decimal = 2.5
    numero_inteiro = 5

OBS:
    Variável sempre começa com letra ou “_”, nunca com números
    Variável é case-sensitive, “Nome” é diferente de “nome”

## Como comentar um código:

Exemplo 1:

    #nome = “João” (Variavel é comentada)​

    nome = “João” #Variavel de nome (Variável não é comentada)​

Exemplo 2:

    “””

    Tudo escrito entre três tremas duplas estará comentado,

    não importando se está quebrado em diferentes linhas

    ”””


## Funções:
Funções são blocos de comando que rodam apenas quando são chamados.
Ex: 
    valor_subtracao = 10
    def subtracao(valor):
        print(valor)
    valor = valor - valor_subtracao
    print(valor)
    subtracao(20)

4. Comando print:
Exemplo 1:
    • print(“Hello, World!”)

Exemplo 2:

    • nome = “João”
    • print(nome)

5. Listas:
Exemplo 1:
lista = [“João”, “Maria”, “Marcos”]

Exemplo 2:
lista = [1, 2, 3]
print(lista[0])#print trará o valor “1” da lista

OBS:
No Python a lista sempre começa na posição 0. No exemplo 2 temos três posições na lista, onde:
posição 0 = 1
posição 1 = 2

6. Comparações:
    • Igual: a == b
    • Diferente: a != b
    • Menor que: a < b
    • Menor igual: a <= b
    • Maior que: a > b
    • Maior igual: a >= b
7. Operadores Lógicos:
E: and
Ex: a = 1
      b = 2
      c = 3
      if a < b and c > b:
print(“Esta validação retornou verdadeiro”)

Ou: or
Ex: a = 1
       b = 2
       c = 3
       if a > b or c > b:
print(“Esta validação retornou verdadeiro”)

Não: not
Ex: x = 5
      print(not(x > 3 and x < 10))

8. Comparação X Atribuição:

Devemos tomar cuidado com sinal de comparação (==) e com o sinal de atribuição (=)

“==” serve para realizar uma comparação de um valor com outro

Ex: if a == b:
…

“=” serve para atribuição de valor

Ex: a = 2
      b = 4

9. If … elif:

Exemplo:
              a = 10
              b = 20
  if b > a:
print(“b é maior que a”)
  elif b == a:
print(“b é igual a a”)
  else:
print(“b é menor que a”)

10. While:

O Comando while é um laço que irá executar tudo que estiver dentro dele enquanto sua condição for verdadeira.

Ex: a = 1
      while a < 6:
print(a)
a += 1

IMPORTANTE: Sempre na cadeia de comandos dentro do while, o valor deve ser incrementado/quebrado, caso contrário o loop continuará infinitamente.


11. For:
O comando for é um laço que se repete por um número determinado de vezes. Este número de vezes é determinado antes do início do comando.
Ex: frutas = ["maçã", "banana", "cereja"]
       for item in frutas:
       print(item)

