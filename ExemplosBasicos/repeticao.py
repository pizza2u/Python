# Código while
numero =21
tentativa = 3

rodada = 1
while(tentativa >= rodada):
    print("tentativa {} de {}".format(rodada,tentativa))
    chute = int(input("bora: "))

    if chute == numero:
        print("acertou")
        break
    else:
        if chute> numero:
            print("o chute é maior que o numero")
           
        if chute < numero:
            print(" o chute é menor que o numero")

    rodada = rodada +1
           


print('fim de jogo')

