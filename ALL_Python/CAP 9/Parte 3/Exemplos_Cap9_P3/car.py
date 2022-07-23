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


#----------------- Armazenando as outras classes Battery e ElectricCar

class Battery():
        def __init__(self,battery_size=70):
            self.battery_size = battery_size
        # Inicializa os atributos da bateria
        def decribe_battery(self):
            print("Esse carro tem uma bateria de "+ str(self.battery_size)+ " kWh")
        # Exibe um frase que descreve a capacidade da bateria
        def get_range(self):
            if self.battery_size==70:
                range=386
            elif self.battery_size ==85:
                range = 434
            message = "Esse carro pode percorrer aproximadamente " +str(range)
            message += " Km com bateria carregada."
            print(message)
        # Exibe a frase sobre a distância que o carro pode correr com a bateria
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
    # Inicializa os atributos da classe-pai; e inicializa os atributos específicos de um carro elétrico

