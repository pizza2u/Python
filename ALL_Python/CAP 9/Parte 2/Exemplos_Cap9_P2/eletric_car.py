class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

tesla = ElectricCar('tesla','modelo s', 2016)
print(tesla.get_decriptive_name())

#----------------- Acréscimo de atributo
print("\n\n--------- Acréscimo de atributo")
class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("Esse carro tem uma bateria de "+str(self.battery_size)+ "kWh")    

tesla = ElectricCar('tesla','modelo s', 2016)
print(tesla.get_decriptive_name())
tesla.describe_battery()

#---------- Sobrescrevendo
print("\n\n--------- Sobrescrevendo")
class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem
    

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("Esse carro tem uma bateria de "+str(self.battery_size)+ "kWh")    

    def fill_gas_tank():
        print("Esse carro não precisa de gasolina")

tesla = ElectricCar('tesla','modelo s', 2016)
print(tesla.get_decriptive_name())
tesla.describe_battery()


#---------- Instâncias como atributos
print("\n\n------ Instâncias como atributos")
class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem

class Battery():
        def __init__(self,battery_size=70):
            self.battery_size = battery_size

        def decribe_battery(self):
            print("Esse carro tem uma bateria de "+ str(self.battery_size)+ " kWh")

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

tesla = ElectricCar('tesla','modelo s','2016')
print(tesla.get_decriptive_name())
tesla.battery.decribe_battery()

#---------- Acrescentando +Instâncias como atributos
print("\n\n------ Acrescentando +Instâncias como atributos")
class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")
    
    def increment_odometer(self,quilometragem):
        self.odometer_reading += quilometragem

class Battery():
        def __init__(self,battery_size=70):
            self.battery_size = battery_size

        def decribe_battery(self):
            print("Esse carro tem uma bateria de "+ str(self.battery_size)+ " kWh")

        def get_range(self):
            if self.battery_size==70:
                range=386
            elif self.battery_size ==85:
                range = 434
            message = "Esse carro pode percorrer aproximadamente " +str(range)
            message += " Km com bateria carregada."
            print(message)

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

tesla = ElectricCar('tesla','modelo s','2016')
print(tesla.get_decriptive_name())
tesla.battery.decribe_battery()
tesla.battery.get_range()