# TIPOS DE DADOS I - CAPÍTULO 2
#==================================================
# TÓPICO 1: NÚMEROS
# Função type() - retorna o tipo do dados que você colocar dentro dos parênteses
#Exemplo:
print(type(5))
# Ele vai mostrar um <class 'int'> para mostrar que é um número inteiro
#Exemplo 2: Números float
print(type(1.3))
# Que vai mostrar <class 'float'> que é o ponto flutuante, ou seja, números reais
# O python lê qualquer número com '.' como float, então sempre vai ser float.
# Os números inteiros podem ser reais, mas os reais não podem ser inteiros
# Sempre que houver expressões com números não inteiros, o  resultado vai ser real.
# Exemplo 3:
a= 1.5
b= 2.5
y=a+b
print(type(y))
print(y)     #Vai printar <class 'float'>  4.0

#Um caso especial é na divisão
# Exemplo 4:
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

#---------------------------------------------------------------------------------------------------------------------
# Problemas de números reais no computador
# Números float na computação são aproximações muito boas, nunca exatos.
#A precisão sempre vai ser de aproximadamente 16 casas decimais(precisão dupla). As 16 primeiras casa decimais de um número real vão estar sempre certas, o valor após isso é duvidoso.
# É comum ter bugs no programa por conta das imprecisões do tipo float.
