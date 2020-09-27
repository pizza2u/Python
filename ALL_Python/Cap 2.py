# TIPOS DE DADOS I - CAPÍTULO 2
#==================================================
# TÓPICO 1: NÚMEROS
# Função type() - retorna o tipo do dados que você colocar dentro dos parênteses
#EXEMPLO 1:
print(type(5))
# Ele vai mostrar um <class 'int'> para mostrar que é um número inteiro
#EXEMPLO 2: Números float
print(type(1.3))
# Que vai mostrar <class 'float'> que é o ponto flutuante, ou seja, números reais
# O python lê qualquer número com '.' como float, então sempre vai ser float.
# Os números inteiros podem ser reais, mas os reais não podem ser inteiros
# Sempre que houver expressões com números não inteiros, o  resultado vai ser real.
# EXEMPLO 3:
a= 1.5
b= 2.5
y=a+b
print(type(y))
print(y)     #Vai printar <class 'float'>  4.0

#Um caso especial é na divisão
#EXEMPLO  4:
a=4
b=a/2
print(type(b))
print(b)          #obtemos <class 'float'> 2.0
# Por quê acontece isso???? Pq usamos o operador da divisão real(/), e não o da divisão inteira(//)
#See it:
a=4
b=a//2
print(type(b))      #Vai printar <class 'int'> 2
print(b)

#__________________________________________________________________________________
# Problemas de números reais no computador
# Números float na computação são aproximações muito boas, nunca exatos.
#A precisão sempre vai ser de aproximadamente 16 casas decimais(precisão dupla). As 16 primeiras casa decimais de um número real vão estar sempre certas, o valor após isso é duvidoso.
# É comum ter bugs no programa por conta das imprecisões do tipo float.

#----------------------------------------------------------------------------------------------------------------------------------
# TÓPICO 2: BOOLEANS
# Às vezes o programa não quer guardar número ou textos em variáveis, apenas quer um SIM ou NÃO.
# Boolean - Pode expressar os valores True e False.
# EXEMPLO 5:
uma_boolean = True
outra = False   # Só funcionam se a primeira letra for maiuscula e o resto minusculo, caso seja true e false não vai rolar não!
# O computador só lê 1 e 0, entçao ele vai entender !!! True como 1 !!! &  !!!! False para 0 !!!
print("somando um boolean: ", 99+uma_boolean)
print("Multiplicando um boolean: ", 20*outra)
# Obtemos: Somando: 100
            #   Multiplicando: 0
#_________________________________________________________
            # Operações de comparação
       # Os booleanos podem ser criados a partir de comparações
       # EXEMPLO 6 :
print( 2==3) # Essa comparação obviamente e falsa, 2 não é igual a 3

 # E o operador verifica isso com ==
 # Outro operador de comparação é o !=, que verifica se são diferentes
 # EXEMPLO 7:
a=1
b=3
c= "fred"
d= "elton"
print( a != b) # True - São diferentes
print( c == d) # False - São diferentes

# Da mesma forma ocorre na matemática:
# EXEMPLO 8:
x= 10.0
print(x>5) # True
print(20<x) # False
print(10>= x) # True                           >= significa maior ou igual (além de uma carinha triste KKKK),o operador da esquerda e maior ou igual ao da direita

w= 12.5
print(w <= x) # False          <= menor ou igual

#_____________________________________________________________________________________________________________________________________
# Comparação Alfabética
# Os operadores > e < também podem ser usados com strings. E no python ele checa a ordem alfabética
# EXEMPLO 9:
palavra1 = "abacaxi" # Vamos ler assim: abacaxi = 1
palavra2 = "maça" # maça = 13
palavra3 = "Pera" # Pera = 0
print(palavra1> palavra2) #False  -  Foi False porque alfabeticamente, abacaxi vem antes
print(palavra3< palavra2) # True
print( palavra1< palavra3) #False
# Em python, todo o alfabeto de letras maiusculas vem antes das minusculas

# Comperação em cadeia
# Não precisam ser apenas comparações entre valores, vamos misturar.
#EXEMPLO 10:
idade=18
adolescente= 17>idade>13  # Só vai ser adolescente se for menor que 17 e maior que 13
print(adolescente) # O resultado deu False, não sendo adolescente

#-- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
 # Implementando input no exemplo anterior
# EXEMPLO 11:
print("\nExemplo 7\n")

sua_idade=int(input("Qual a sua idade?\n")) #---- Acrescentar o int antes do input faz com que o computador entenda que o objeto inserido é um número inteiro.
jovem = 25> sua_idade > 17
print(jovem) # Retorna True se estiver entre essas idades


#-------------------------------------------------------------------------------------------------------------------------------------------------
# TÓPICO 3: CONVERSÃO DE TIPOS
# Pra que isso? Converter tipos? eu hein!
# Então more, as vezes não dá pra fazer operações que a gente quer com o que a gente tem.
# Chora ou Chora
#E aí a gente tem que fazer manualmente (spoiler foi dado no exemplo 11)

#EXEMPLO 12:
outra_idade=input("Diga ai boy:\n")
print(outra_idade * 3) # O resultado dá um chernobyl, caso você tenha testado, vou dar meu exemplo: minha idade é 18, e no resultado do print vai aparecer 181818
#A variável outra_idade vai receber o valor digitado mas em forma de string.E então o texto é triplicado.
# Por essa nem o futuro esperava
# Old que você esperava que fosse fazer uma operação matématica né
# Então a gente precisa que os dados sejam numéricos.
# No caso, temos que fazer como o EXEMPLO 7
#EXEMPLO 13:
outraIDADE=int(input(" Bora diga de novo:\n "))
print(outraIDADE *3)  # Dessa vez obtivemos uma operação matemática, e no meu caso o resultado deu 54.
# Repare que a função que a gente usou para converter a saída da função input é inteiro (int)
# inteiro - int()
#real - float()
#boolean - bool()
#texto - str()
# lista - list()
# tupla - tuple()               A LÓGICA É  A MESMA
#------------
#BÔNUS:
#E isso também serve para string, como foi mostrado no EXEMPLO BÔNUS 1 do capítulo anterior,vamos implementar como a forma usando o input
# Exemplo Bônus
# Exemplo bônus:
first_n= str(input("Qual o seu primeiro nome?\n"))
last_n=str(input("Qual o seu segundo nome?\n"))
full= first_n+ " " + last_n +"\t"   #\t é usado para acrescentar tabulação ao texto.
print(full) # Que vai printar o primeiro nome e o segundo
print(full.title()) # Para printar os nomes com as letras iniciais maiúsculas, como visto no CAP 1


#______________________________________
# Compatibilidade dos tipos
# Então pessoas lindes que leem isso,  não importa qual o tipo de dado que coloca dentro das funções, desde que compatível vai funcionar
# EXEMPLO 14:
print("\n")
print(str(int("45") * float("2")) + str(3.14))
# Vou explicar o que diacho aconteceu aí: Convertemos o texto "45"( tudo entre aspas é considerado string(texto)), ai convertemos "2" para número real,e depois o resultado da multiplicação 45 pelo real 2.0 para texto de novo, e uniu com "3.14"
# Parece chernobyl
# Que vai printar: 90.03.14
# É a junção de "90.0" com "3.14"
# MASSSSSSSSSSSSSSS  nem tente converter palavra em inteiro viu, já ta chernobyl ai tu deixa mais.
# TEM QUE SER COMPATÍVEL ESSE NEGOCIO
# um dos principais erros é conversão de tipo usando real com vírgula.
# NÚMEROS DECIMAIS SÃO REPRESENTADOS COM PONTOS não seja burre
# !!!!!!!!!! As principais conversões são de números pra texto, com str(), e de texto para números, com int() e float()
#FLW



























