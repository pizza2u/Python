# Continuação da Parte 1 do CAPÍTULO 9
# ---------- Herança
# Se a classe que você estiver escrevendo for uma versão especializada de outra já criada, a herança poderá ser usada.
# Quando uma classe herda de outra ela assumirá todos os atributos e méodos da primeira classe.
# A classe original se chama classe-pai e a nova é classe-filha. A classe-filha herda todos os atributos e métodos do pai, mas também pode definir novos atributos
# e métodos próprios.

#----- Método __init__() de uma classe-filha
# A primeira tarefa é  atribuir valores a todos os atributos de classe-pai. Para isso, o método __init__() de uma classe-filha precisa da ajuda do pai.
# Como exemplo, modelares um carro elétrico. Esse carro é apenas um tipo específico, logo podemos basear-se na outra classe criada Car(), ou mais especificamente, Car4() do arquivo anterior.
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

# Começamos colocar a nossa classe já feita na Parte 1 que foi Car(). Quando criamos a classe-filha, a classe-pai deve fazer parte do arquivo atual, logo se torna o parâmetro da classe-filha.
# O método __init__() aceita as informações necessárias para criar uma instância de Car.
# A função super() é uma função especial que ajuda o Python a criar conexões entre a classe-pai e filha.
# Ela diz que para o python chamar o método __init__() de classe-pai de ElectricCar(), que confere todos os atributos da classe-pai para a criada.
# O super é derivado de uma convenção onde a classe-pai se chama superclasse, e a filha é a subclasse.
# É criado uma instância da classe ElectricCar() e armazenamos o tesla nele. A linha chama o método __init__() definido em ElectricCar que diz ao Python para chamar o método __init__() definido na classe-pai.
# E após é fornecido os detalhes do carro, senndo marca, modelo e ano.
# Além do init, não há outros atributos nem métodos que sejam particulares a um carro elétrico.
# A instância de ElectricCar funciona como uma instância de car, logo pode ser definido atributos e métodos mais específicos aos carros elétricos.

#----- Definindo atributos e métodos da classe-filha
# Depois que tiver um classe-filha que herde de uma classe-pai, é possível acrescentar qualquer atributo ou método novo necessário para diferenciar a classe filha da pai.
# Iremos acrescentar um atributo que seja específico aos carros elétricos, como bateria, e um método para mostrar isso.
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

# Foi adicionado um novo atributo self.battery_size e definido seu valor inicial como 70. Esse atributo será associado a todas
# as instâncias criadas a partir de ElectricCar(), mas não será associado a nenhum instância de Car.
# Também foi adicionado o método describe_battery() que exibe as informações sobre a  bateria.
# Não há limites de quanto você pode especializar a classe ElectricCar.

#----- Sobrescrevemdo métodos da classe-pai 
#  Qualquer método de classe-pai que não se enquadre no que você estiver modelando com a classe-filha pode ser sobrescrito.
# Para isso, é preciso definir um método na classe filha com o mesmo nome do método do pai. Python despreza o método da classe-pai e só prestará atenção no método definido na classe-filha.
#  Suponhamos que a classe Car tenha um método chamado fill_gas_tank(), e sobrescreveremos esse método.
class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("Esse carro tem uma bateria de "+str(self.battery_size)+ "kWh")    

    def fill_gas_tank():
        print("Esse carro não precisa de gasolina")

# Se algúem tentar chamar fill_gas_tank() com um carro elétrico, o python ignorará esse método de Car e executará o código apresentado no lugar.
#  Ao usar herança, é possível fazer as classes-filhas preservarem o que for necessário e sobrescrever tudo que não for utilizado na classe-pai.

#----- Instâncias como atributos
# Ao modelar algo será perceptível adicionar cada vez mais detalhes a uma classe.
# Há uma lista crescente de atributos e métodos e assim os arquivos ficarão extensos.
# Nesses casos, é notório que uma parte da classe pode ser escrita como classe separada. 
# Por exemplo, se continuarmos com detalhes em ElectricCar,  podemos parar e transferir esse atributos e métodos para uma classe diferente chamada Battery, e assim usar uma instância de Battery como atributo da classe ElectricCar.
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

# Foi definido uma classe chamada Battery() que não herda de nenhuma outra classe. O método __init__() nessa classe tem um parâmetro
# battery_size, além de self. É um parâmetro opcional que define a capacidade da bateria com 70 se nenhum valor for especificado, o método describe_battery()
# também foi transferido para a classe Battery().
# Na classe ElectricCar, adicionamos um atributo chamado de self.battery, que diz ao python para criar uma nova instância de Battery(com capacidade default de 70), e 
# armazenar essa instância no atributo self.battery. O que acontecerá sempre que o init for chamado, qualquer instância de ElectricCar terá uma instância de Battery.
tesla.battery.decribe_battery()
#Esse linha acima informa ao python para usar a instância tesla, encontrar o atributo battery e chamar o método describe_battery() associado à instância de Battery do atributo.
# Vamos acrescentar outro método em Battery que informa a distância que o carro pode percorrer de acordo com a bateria dele.
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
                range=240
            elif self.battery_size ==85:
                range = 270
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

# O novo método get_range() que efetua uma análisem, em que caso a capacidade da bateria seja de 70 kWh, é definido um alcance
# do carro com 386 Km, se a capacidade for de 85 kWh, o alcance será de 434 Km.
# E é chamado por meio do atributo battery do carro. A saída informa a distância que o carro é capaz de percorrer de acordo com a bateria.

# À medida que começar a modelar itens mais complexos, terá mais detalhes e perguntas a se fazer. Por exemplo, se estivermos descrevendo uma linha de carros,
# é provável que vamos querer transferir o get_range() para a classe ElectricCar(), e o método get_range continuaria verificando a capacidade da bateria antes de determinar as distâncias,
# de modo alternativo, poderia ter uma associação entre get_range() e a bateria, mas passaríamos um parâmetro a ele, como car_model. Assim o método get_range() informaria a distância
# que o carro poderá fazer de acordo com o modelo do carro e sua bateria.