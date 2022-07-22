import math

print(math.pi)
print(math.pi * 2)
print(math.pi **2)

print(math.sin(math.pi/4)) 
print(math.cos(math.pi/3)) 
print(math.tan(math.pi*3/4))

print(math.sin(math.radians(45)))

print(math.degrees(math.pi))

print(49**(1/2))
print(math.sqrt(49))

print(math.log(1))

print(math.log(100,10))

print(math.exp(2))
print(math.exp(1))


pi=math.pi
pbaixo=math.floor(pi)
pcima=math.ceil(pi)
print(pbaixo)
print(pcima)


import cmath
print(cmath.exp(2))
print(cmath.sin(1))
print(cmath.log(2))
print(cmath.sqrt(-4))


import random

random.seed(20028922) 

r1= random.random( ) 
r2= random.randint(2,50)

lista=[10,3.14,"<3", True]
r3 = random.choice(lista)

string= "Young"
r4= random.choice(string) 
print(r1)
print(r2)
print(r3)
print(r4)

import time


tempo = time.time()
for i in range(2000000):
       x = i * i

tempoD = time.time() - tempo

print(" O programa levou %.2fs para ser executado."%tempoD)
print("\n\n")

data= time.localtime()
print(data.tm_year) # ano
print(data.tm_mon) # mes
print(data.tm_mday) #dia
print(data.tm_hour) #hora
print(data.tm_min) # minutos
print(data.tm_sec)
print("\n\n")
print("Mais organizado:\n")
print("Ano:" + str(data.tm_year)) 
print("Mês:" +  str(data.tm_mon)) 
print("Dia:" + str(data.tm_mday)) 
print("Hora:" + str(data.tm_hour)) 
print("Minuto:" + str(data.tm_min)) 
print("Segundos:" + str(data.tm_sec)) 

print(" Início")
time.sleep(5) 
print("Fim")