# CAPÍTULO 6 - MÓDULOS E PACOTES
# Vamos supor que pra resolver um determinado exercício tu precisa calcular seno de um ângulo qualquer
# A ideia do negócio é que pode importar códigos escritos por outras pessoas
# Como o math, esse vem com códigos pronto pra matemática
# Basta fazer isso:
import math
# JUST THIS
# obs: caso você tenha que importar mais de um módulo, faça nas primeiras linhas, um abaixo do outro

#-------------------------------------
# USANDO O PI
# O módulo math vem com um pi com várias casas decimais,basta escrever:
print(math.pi)
print(math.pi * 2)
print(math.pi **2)

#------------------------------------
# Métodos trigonométricos
print(math.sin(math.pi/4)) #45º
print(math.cos(math.pi/3)) #60º
print(math.tan(math.pi*3/4)) #135º
#Mas não esqueça que essas funçoes recebem os ânbulos em RADIANOS
# Se quiser converter de graus para radianos, é necessario usar uma função de conversão
print(math.sin(math.radians(45))) #45º

# Também é possível o processo ao contrário, converter radianos para graus basta usar math.degrees()
print(math.degrees(math.pi)) #180º

#---------------------------------------
# Método de raiz quadrada
# Existem dois metodos
print(49**(1/2))
print(math.sqrt(49))

# Essas formas obtem o mesmo resultado
# MAS se tentar calcular raizes negativas, o math.sqrt vai retornar um erro.
# Caso a questão seja de números complexos, a primeira forma é a única possível

#------------------------------------------
# Logaritmos com math
# O módulo math também pode ser utilizado na resoluçao de logaritmos (ln)
print(math.log(1))
print(math.log(0)) # ERRO
# Não da pra calculas log de número negativo e 0
# Apenas reais (infinitos não são reais)

# Caso queira calcular log de uma base específica, você pode usar o segundo parâmentro da função math.log()
print(math.log(100,10))

#---------------------------------------
#Usando constante de euler
# math.exp(x) retorna e^x
print(math.exp(2))
print(math.exp(1))

#---------------------------------
# Arredondamentos
# As funções math,floor() e math.ceil() arredondam para baixo e para cima respectivamente.
pi=math.pi
pbaixo=math.floor(pi)
pcima=math.ceil(pi)
print(pbaixo)
print(pcima)

#---------------------------------------
# Números complexos
#Não da pra fazer cálculos de números complexos com essa biblioteca, mas podemos usar o cmath
import cmath
print(cmath.exp(2))
print(cmath.sin(1))
print(cmath.log(2))
print(cmath.sqrt(-4))

# Funciona, masss vai ter uma parte imaginária, é a única forma de fazer operações com complexos


#============================================================================
# Módulo Random

# Primeiro que a aleatoriedade na computação não e 100% real
# Digite a biblioteca random
import random

# Funções aleatórias
random.seed(20028922) 

r1= random.random( ) # O número real aleatória entre 0 e 1
r2= random.randint(2,50)

lista=[10,3.14,"<3", True]
r3 = random.choice(lista) # Um item da lista

stringg= "BORA"
r4= random.choice(stringg) # Uma letra da string
print(r1)
print(r2)
print(r3)
print(r4)

#Função random.randint()
# Retorna um número inteiro no intervalo que determinamos como foi visto acima

# Função random.choice()
# Como o próprio nome ja diz, ele vai escolher  um parâmetro entre parênteses, em uma lista ou string

# Função random.seed()
# Saiba que todas as funções do módulo random fazem contas doidas com o valor que você passa na função random.seed()
# O importante é que se você usar o mesmo seed, o resultado vai ser o mesmo
# por exemplo : # Na linha onde temos random.seed(20028922) , teste rodar duas vezes com essa linha, e depois sem ela, ou com outro número no parênteses
# O resultado sem o seed vai ser sempre diferente, é como se você sorteasse uma bolinha roxa e desse um número a ela, e então enquanto não trocar o número essa se mantem daquela cor

# Em resumo, você só precisa usar o seed se quiser números aleatório pré definidos

#============================================================================
# Módulo time
import time
# time = tempo
# Esse módulo pega dados sobre tempo e data
# Acontece que todos os computadores sabem quantos segundos se passaram desde 00h de 1 janeiro de 1970
tempo = time.time()
for i in range(2000000):
       x = i * i

tempoD = time.time() - tempo

print(" O programa levo %.2fs para ser executado."%tempoD)

# Esse exemplo acima, calcula o quadrado de todos os números entre 0 e 2000000,
# Usando time.time()

# Sabendo a quantidade de segundos, pode-se converter pra dias e meses, anos ,etc
# Mas existe um função que ajuda nisso
# FUNÇÃO LOCALTIME
data= time.localtime()
print(data.tm_year) # ano
print(data.tm_mon) # mes
print(data.tm_mday) #dia
print(data.tm_hour) #hora
print(data.tm_min) # minutos
print(data.tm_sec) #segundos

# E se a gente so printar o data?
print(data)
# Ele vai mostrar o resultado de cada um acima, mas bagunçado

# E seee a gente inserir algo nos parênteses?? Bom ele vai calcular em um certo tempo de segundos

oxe= time.localtime(1000000000)
print(oxe.tm_year) # ano
print(oxe.tm_mon) # mes
print(oxe.tm_mday) #dia
print(oxe.tm_hour) #hora
print(oxe.tm_min) # minutos
print(oxe.tm_sec) #segundos

# Vai mostrar que desde de 1970 até 2001(ano printado) foram decorridos 1000000000 segundos

# Função sleep
print(" Início")
time.sleep(5) # Bem óbvio que ele vai demorar 5 segundos para poder rolar a próxima linha
print("Fim")





























