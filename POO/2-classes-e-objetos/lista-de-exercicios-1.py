# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.



# Crie uma instância da classe carro.


# Faça o carro "andar" utilizando os métodos da sua classe.


# Faça o carro "parar" utilizando os métodos da sua classe.

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor
        self.modelo = modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("O carro está ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            if self.velocidade == 0:
                self.ligado = False
                print("O carro está desligado.")
            else:
                print("O carro não pode ser desligado enquanto está em movimento.")
        else:
            print("O carro já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("Você precisa ligar o carro primeiro.")

    def desacelera(self, decremento):
        if self.ligado:
            if self.velocidade >= decremento:
                self.velocidade -= decremento
                print(f"O carro desacelerou para {self.velocidade} km/h.")
            else:
                print("O carro não pode desacelerar abaixo de 0 km/h.")
        else:
            print("Você precisa ligar o carro primeiro.")

# Criando uma instância 
meu_carro = Carro(cor="vermelho", modelo="Sedan")

#  carro "andar"
meu_carro.liga()
meu_carro.acelera(20)
meu_carro.acelera(30)

# "parar"
meu_carro.desacelera(20)
meu_carro.desacelera(30)
meu_carro.desliga()
