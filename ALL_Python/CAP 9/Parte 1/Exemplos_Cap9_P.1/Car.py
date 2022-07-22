print("\n------Car \n")
class Car():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
    
    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()

novo_car = Car('audi','a4','2016')
print(novo_car.get_decriptive_name())

print("\n------Car 2 \n")
class Car2():
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

novo_car2 = Car2('audi','a4','2016')
print(novo_car2.get_decriptive_name())
novo_car2.read_odometer()
# Alterando o valor do atributo pela instância:
print("\nPelo instância: \n")
novo_car2.odometer_reading = 25
novo_car2.read_odometer()

# Alterando pelo método:
print("\nPelo método:")
print("------Car 3 \n")
class Car3():
    def __init__(self, make, model, year):
        self.make= make 
        self.model = model
        self.year = year
        self.odometer_reading = 20
    
    def get_decriptive_name(self):
        long_name = str(self.year) +' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("Esse carro tem: "+ str(self.odometer_reading)+ " KM rodados")
    
    def update_odometer(self,quilometragem):
        if quilometragem >= self.odometer_reading:
            self.odometer_reading = quilometragem
        else: print("Você não pode mudar o valor do hodometro")

novo_car3 = Car3('audi','a4','2016')
print(novo_car3.get_decriptive_name()) 

novo_car3.update_odometer(10)
novo_car3.read_odometer()

 # Alterando pela Incremenação do valor de um atributo com um método            
print("\nPelo incrementação de valor do atributo com método:")
print("------Car 4 \n")
class Car4():
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

carro_usado = Car4('subaru','outback',2013)
print(carro_usado.get_decriptive_name())

carro_usado.update_odometer(26)
carro_usado.read_odometer()

carro_usado.increment_odometer(50)
carro_usado.read_odometer()