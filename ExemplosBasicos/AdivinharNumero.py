tentativa = 3
import random

x = random.randint(1,100)

rodada = 1
while(tentativa >= rodada):
    print("tentativa {} de {}".format(rodada,tentativa))
    chute = int(input("bora: "))

    if chute == x:
        print("acertou")
        print('fim de jogo')
        break
    else:
        if chute> x:
            print("o chute é maior que o número")
           
        if chute < x:
            print(" o chute é menor que o número")
      
    rodada = rodada +1

print('A resposta certa é:', x)
