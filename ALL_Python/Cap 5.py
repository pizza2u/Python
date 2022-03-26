# CAPÍTULO 5 - REAPROVEITAMENTO DO CÓDIGO ( Já aviso que tem muita informação esse capítulo)
#================================================
# TÓPICO 1: LAÇOS DE REPETIÇÃO
# Para ser breve, as duas estruturas de repetição em Python são o while e for

# LAÇO WHILE
# Se você lembrar bem, em if, fomos capazes de executar ou não um bloco de código dependendo de uma condição booleana
# O while é bem parecido
#while exp:
       #código a ser executado
       #enquanto for verdade
#EXEMPLO 1: (loop infinito)
 while 1<5:
       print("é mermo é")

       # Se você executar esse código, ele vai entrar em loop infinito, já que 1 é menor que 5
#MAAAS se fizermos
cont = 1
while cont <= 100:
       print(cont)
       cont += 1
       # O que que rolou nesse código? Então, nesse código o laço não vai se repetir para sempre, digamos que ele tenha um critério de parada, e esse critério é 100,
  # a cada vez que o código se repetir , a variável cont vai ter um valor diferente
       # ou seja para cada cont rodado, o valor vai receber +1.
       # Mas quando o valor de cont for maior que 100 o programa vai parar

# LAÇO FOR
# Diferente do while. baseado em condições booleanas, o for tem um número determinado de passos
#Você pode dizer ,antes da repetição começar, quais vão ser os valores de uma determinada variável a cada loop
# EXEMPLO 2:
for variavel in [2,3,5,78]:
       print (variavel)
# Aqui vai ser mostrado apenas o vetor
for isso in range(1,101):
       print(isso)

# A função range exibe os números do 1 a 100
# Mas por que 101? É porque o segundo intervalo não tá incluso.
# Além de que, não é obrigatorio usar a variavel da estrutura
for aquilo in range(5):
       print("Oi") # Como eu só usei um valor, ele vai de 0 até o valor (x)
       # Printando Oi em 5 vezes

# Laço For com string
# As strings também funcionam no laço for
# EXEMPLO 3:
frase = "Star trek"
for letra in frase:
        print (letra)
#Ele vai imprimir uma lista com cada letra de star trek
        # um print para cada letra
# E o nome da variável de for é você que escolhe

#----------------------------------------------------------------------------------------------------------------------------------------------------
# TÓPICO 2  - FUNÇÕES
# Utilidade das funções: Bom, funções são blocos de código que você consegue salvar para reutilizar. Quando você declara uma função, você tá salvando um "modelo" de código. Sempre que precisar , você pode chamar sua função que você criou e aquele bloco de código vai ser executado para você
# útil porque evita repetições de códigos.
# Estrutura:
# def nome_da_funcao(parametros)
       #corpo da função aqui
# A palavra chave "def" específica o que vem a seguir é uma função, e você precisa usar sempre que quiser criar uma função
# Os parâmetros são uma sequência de variáveis pré-criadas,separadas por vírgulas, para ser usada na função.
# As variáveis criadas como parâmetros podem ser definidas de fora da função.
# Ou seja, uma função pode não ter nenhum parâmetros, mas mesmo assim você precisa colocar os parentêses

# A palavra chave return - Ele define o fim da função, quando o comando return for executados , a função acabada
# Ele devolve pro código que chamou a função o resultado da expressão que você colocar junto com o retorn

# Sem mais enrolação vamos pro código
# EXEMPLO 4: Calcular a área de triângulos
def area_triang(base,altura):
       return base*altura / 2

triang1 = area_triang(4,6) # Parametros de base e altura
triang2= area_triang(3,7)
print(" Área do triângulo 1 é %.2f ."%(triang1) )  # Lembrando da formatação , float - %0.xf 
print(" Área do triângulo 2 é %.2f ."%(triang2) )
# Acho que deu pra pegar né

# Escopo de funções
# Cada função tem seu corpo, e esse corpo é privado. Não é possível acessar o código escrito dentro de uma função externamente, Isso significa que toda variável que você criar dentro de uma função só existe dentro dela.

# Oia o exemplo
# EXEMPLO 5:
 def teste( ):
       maça = 4
       morango =10

 teste( )
 print(morango) Vai dar erro!
# E essa função não tem a palavra return. Não é obrigatório usar, mas a função não retorna nada. Logo não pode fazer variável = função ( )

#Variáveis globais
# Quando a gente cria variáveis dentro das funções, é inpossível acessar fora né.
# Mas o oposto também é parecido. Normalmente a gente só consegue ler as variáveis globais de dentro de função, mas não consegue alterar elas:
# Se liga
# EXEMPLO 6:
 batata= 123
 def func( ):
       print(batata)
      batata=batata*2 # Erro aqui

 func( )

# A  gente consegue ler o valor das variáveis fora das funções, mas não escrever nelas
# PRA TUDO TEM UM JEITO
# Existe uma forma de ter permissão para alterar essas variáveis, e se chama global
# sim, global
# Chegue ver curiose
batata= 123
def func( ):
       global batata  # pedindo permissao
       print(batata)
       batata=batata * 2 # agora vai

func( )
print(batata)


# BÔNUS INFORMAÇÃO
# Aprendemos a criar funções, mas você sabia que tem usado funções há tempos.
# Todos os comando , print(), input(), int(), etc, são funções
# Essas ja vieram programadas pelos criadores do python
# E se chamando built-in, que já vem dentro do python

#----------------------------------------------------------------------------------------------------------------------------------
#TÓPICO 3 - RECURSÃO
# Até aqui vimos os laços for e while, mas cada um desses laços tem vantagens e limitações. Mas existe um segredinho...
# Existe uma técnica chamada recursão, para fazer repetições sem usar laços de repetição.
# Como funciona:

#  º Teoria: quando temos 1+1+1+1+1+1+1+1, você não é capaz de calcular de cara certo? Mas sabemos que o resultado é 8
# E se utilizarmos o 1+1+1+1+1+1+1+1+1 ( Com um 1 a mais), você ja vai saber calcular e o resultado será 9
# Esse método se chama recurssão, a gente usa mentalmente, sem perceber, para resolver alguns problemas.
# Funções recursivas são funções que chama a si mesmas

# º Aplicação: Em casos clássicos como, em números fatoriais como o 5! = 5*4*3*2*1
# Okay você não sabe resolver isso de cara, então e se usarmos 5!= 5 x 4!
# Ué  o problema é fatorial e a resposta tem fatoral EXATO
# Mas quanto é 4! ? = 4! = 4 * 3!
# DE NOVO???????? sim
# E assim vai até o 1! = 1x0! e 0!=1
# Mas para o 0! não precisamos calcular nada ne
# 0!= 1   1! = 1*1 =1      2! = 2*1 =2     3!= 3*2=6      4!=4*6 = 24        5!=5*24= 120
# OU SEJA PRA RESUMIR TUDO
# n! = n*(n-1)!

# º Em python:
def fat(n):
       if n==0:
              return 1
       else:
              return n *fat(n-1)
print("5! é igual a %i. " %(fat(5)))
print(" 2! é igual a %i. "%(fat(2)))
print(" 21! é igual a %i. " %(fat(21)))

# ALERTA: Às vezes( muitas) a nossa função dá errado, e abaixo segue algumas causas para caso não funcione.

# LOOP infinito
# Se a condição do if não for atingida fica em loop
# Vamos ver outro exemplo de função recursiva
# Imagina que precisamos de uma função que soma todos os números entre 0 e N,um número inteiro recebido como argumento da função, vamos supor 10
# soma(10) = 10 + soma(9)
# soma(9) = 9 + soma(8)
#    ...
#  soma(0) = 0
# ou seja soma(n) = n + soma(n-1)
# Em python ficaria
def soma(n):
        return n +soma(n-1) # E pronto? ERRADO, porque desse jeito a função vai ficar rodando pro infinito e além, a função vai chamar a si mesma pra sempre
       # Por isso é preciso de uma condição para acabar com o loop
# O certo é esse:
       if n == 0:
              return 0
       else:
              return n + (n-1)
print("Soma de 5 com o número anterior a ele (4) é %i."%(soma(5)))

# Vai mostrar 9

print("Soma de 9 com o número anterior a ele (8) é %i."%(soma(9)))

# É isto pessoal




