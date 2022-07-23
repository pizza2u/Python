#--- Importando um módulo em um módulo

class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0
    # Inicializa os atributos que descrevem o carro
    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()
    # Devolve um nome descritivo formatado em modo elegante
    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    # Exibe uma frase que mostra a quilometragem do carro
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    # Define o valor de leitura do hodômetro com o valor especificado, rejeita alteração se for um valor menor para o hodômetro
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem
    # Soma a quantidade especificada ao valor de leitura do hodômetro