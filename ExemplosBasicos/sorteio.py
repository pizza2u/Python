import random
#Código sorteio 
sorteado = random.randrange(0,3)  #aleatorio

print(sorteado)

if sorteado == 1:
  print("Feliz")
elif sorteado ==2:
  print("Infeliz")
else:
  print("Nada")
