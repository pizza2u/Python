# Continuação da Parte 2 do CAPÍTULO 9
# -------Importando Classes
# À medida que é acrescentado mais funcionalidade às classes, os arquivos ficam maiores, mesmo com a herança de forma apropriada.
# O python permite armazenar clsses em módulos e então importar as classes necessárias.

#--- Importando uma única classe 
# Vamos criar um módulo de que contenha apenas a classe Car. Qualquer programa que use o nódumo precisará de um nome mais específico, como my_car.py;
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

# OS ARQUIVOS DEVEM ESTAR EM UMA MESMA PASTA!
# Após colocar esse código em um arquivo car.py(! Atenção que car.py agora está com a palavra "car" minúsculo),
#  criamos separadamente outro arquivo chamado my_car.py. Ele importará a classe Car e criará uma instância dela

from car import Car

my_new_car = Car('toyota','sw4',2011)
print(my_new_car.get_decriptive_name())

my_new_car.odometer_reading= 20
my_new_car.read_odometer()

# A instrução import diz ao Python para abrir o módulo car e importar a classe Car. Agora é possível usar a classe Car como
# se ela estivesse definida no arquivo.
# Importar classe é uma maneira eficiente de programar, em resumo, para deixar o código mais limpo.
# Quando transferimos a classe para um módulo e importamos, continuamos usufruindo da mesma funcionalidade, mas o arquivo está mais fácil de ler.

#--- Armazenando várias classes em um módulo
# É possível armazenar tantas classes quantas forem necessárias em um único módulo, embora cada classe deva estar em um módulo.
# As classes Battery e ElectricCar ajudam a representar carro, logo acrescentaremos elas ao módulo car.py

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
   


    print("\n\n----------------- Acrescentando as outras classes Battery e ElectricCar")

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

# Agora podemos criar um novo arquivo chamado my_electric_car.py e importar a classe ElectricCar.

#--- Importando várias classes de um módulo
# Podemos  importar quantas  classes forem necessárias em um arquivo.
# Se quisermos criar um carro comum e um elétrico no mesmo arquivo, precisamos importar tanto a classe Car como a ElectricCar.
# Para isso criamos um novo arquivo chamado my_cars.py e importamos as duas classe do arquivo car.py
from car import Car, ElectricCar

carrinho = Car('toyota', 'hillux', 2015)
print(carrinho.get_decriptive_name())

tesla = ElectricCar('telsa',' modelo y', '2018')
print(tesla.get_decriptive_name())

# Note que foram importado as duas classes, separando elas por vírgula. Depois disso, é possível criar quantas instâncias de cada classe
# você quiser.
# No exemplo foi criado um carro da Toyota e um Tesla.

#--- Importando um módulo completo
# Também podemos importar um módulo completo e acessar as classes necessárias com a notação de ponto.
# Como toda chamada que cria uma instância de uma classe inclui o nome do módulo, não terá conflito de nomes com qualquer nome usado no arquivo atual.
# Por exemplo: Criamos um novo arquivo chamado modulo_completo.py e importamos o módulo car inteiro. E então acessamos as classes necessário por meio da sintaxe :
#    nome_do_módulo.nome_da_classe
# Então é criado as instâncias carro e tesla para características.
import car

carro = car.Car('toyota', 'corola', '2016')
print(carro.get_decriptive_name())
tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(tesla.get_decriptive_name())

#--- Importando todas as classes de um módulo
# Podemos importar todas as classes de um módulo usando a sintaxe:
from nome_do_módulo import *

# MAASS, não é recomendado por dois motivos: 1- É coveniente ser capaz de ler as instruções import no início de um arquivo e ter uma noção clara
# de quais classes um programa utiliza. Com esse abordagem não fica claro quais são as classes do módulo que você está usado. Além de resultar em confusão com nomes 
# existentes no arquivo. Se acidentalmente importar uma classe com o mesmo nome que outro item em seu arquivo, então gerará erros difíceis de serem diagnosticados.
# Apesar de não ser recomendado, ainda é possível ver em alguns códigos.
# Se precisar importar muitas classes de um módulo, é melhor importar o módulo todo e usar a sintaxe nome_do_módulo.nome_da_classe. 

#--- Importando um módulo em um módulo
# Às vezes, é desejado espalhar as classes em vários módulos para impedir que um arquivo cresça demais e evitar armazenagem de classes não relacionadas no mesmo módulo.
# Ao armazenas suas classes em vários módulo, você descobre que uma classe em um módulo depende de uma classe em outro módulo. Se isso acontecer, importe a classe necessária
# no primeiro módulo.
# Por exemplo, vamos armazenas a classe Car em um módulo de as classes ElectricCar e Battery em um módulo separado.
# Criaremos um novo módulo chamado electric_car.py - substituindo o arquivo electric_car.py(da parte 2), e então copiaremos apenas as classes Battery e ElectricCar.
from car2 import Car
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

# A classe ElectricCar precisa ter acesso à sua classe-pai Car, portanto importamos Car diretamente para o módulo.
# Se isso não for colocar o python gerará um erro. Também é preciso atualizar o módulo Car para que contenha apenas a classe Car, mas para não confundir com o arquivo de um outro exemplo,
# usaremos uma cópia do arquivo car.py chamada de car2.py, possuindo a mesma classe:
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

# Agora podemos fazer a importação de cada módulo separamente e criar o tipo de carro necessário:
# Assim como no arquivo my_cars.py, vamos criar um outro arquivo para demonstração chamado de my_cars2.py, em que colocaremos:
from car import Car
from electric_car import ElectricCar

carrinho = Car('volkswagem', 'beetle', 2016)
print(carrinho.get_decriptive_name())

tesla = ElectricCar('telsa','roadster', '2016')
print(tesla.get_decriptive_name())

# Importamos Car de seu módulo e ElectricCar de seu módulo. Em seguida foram criados os carros.

#--- Estilizando Classes
# Os nomes das classes devem ser escritos com CamelCaps. Para isso cada palavra do nome deve ter a primeira letra maiúscula
# e não deve usar underscores. Nomes de instância e módulos devem ser escritos com letras minúsculas e underscores entre as palavras.
# Toda classe é bom ter docstring depois de sua definição, ou seja, uma breve descrição do que a classe faz.