from car2 import Car
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
