## ----------------- CAPÍTULO 9 - CLASSES

# SWITCH/CASE
# Para quem conhece outras linguagens, tem em mente o que é a função Switch.
# Em python nativamente não há essa função, então é necessário
# simular por meio de uma classe e de um if e elif's, onde definiremos uma varíavel com dados em forma de dicionário
# E como um dicionário trabalha com a lógica de chave:valor
from pyexpat import model


class Cor:
    vermelho = 1
    verde = 2
    azul = 3
    branco = 4
    preto = 5

# Mude a cor para testar
cor_atual = 2

if cor_atual == Cor.vermelho:
    print("Vermelho")
elif cor_atual==Cor.verde:
    print("Verde")
elif cor_atual == Cor.azul:
    print("Azul")
elif cor_atual == Cor.branco:
    print("Branco")
elif cor_atual == Cor.preto:
    print("Preto")
else:
    print("Nenhuma cor conhecida foi escolhido")

# Caso optarmos para que o usuário escolha a cor, faremos:
cor_atual2 = int(input("Digite o número da cor: "))

if cor_atual2 == Cor.vermelho:
    print("Vermelho")
elif cor_atual2==Cor.verde:
    print("Verde")
elif cor_atual2 == Cor.azul:
    print("Azul")
elif cor_atual2 == Cor.branco:
    print("Branco")
elif cor_atual2 == Cor.preto:
    print("Preto")
else:
    print("Nenhuma cor conhecida foi escolhido")


# Tudo pode ser modelado através de classes, como exemplo escreveremos uma classe simples, Dog(cachorro), sabendo que todos eles
# tem nomes, idades, que sentam e rolam, isso tudo fará parte da classe.

class Dog():        #Definição da classe
    def __init__(self, name, age):  
        self.name = name        #Definições do que a classe irá fazer
        self.age = age

    def sit(self):
        print(self.name.title()+" está agora sentado.")
    
    def roll_over(self):
        print(self.name.title()+" rolou!")

# Como notado, há um método chamado de __init__, toda função em uma classe é um método.
#  A única diferença prática é o modo como é chamado
# O método __init__() é um método especial em Python que executa automaticamente sempre que
# é criado uma nova instância baseada na classe. Esse método tem dois underscores(_) no ínicio e dois no
# final (Isso ajuda a evitar conflito com os nomes de métodos criados).
# O método __init__() é definido para ter 3 parâmetros: self, name e age. O self é obrigatório na 
# definição, uma vez que o python chama esse método , a chamada passará o argumento self automaticamente
# Toda chamada de método associada a uma classe passa self, sendo referência à própria instância, de modo automático.
# e ele dá acesso aos atributos e métodos da classe à instância individual
# self.name = name usa o valor armazenado no parâmetro name e o armazena na variável name, associada à instância criada
# O mesmo para self.age = age.
# A classe tem dois métodos sit() e roll_over(), como esses métodos não precisam de informações adicionais
# como nome e idade, simplesmente é definido o parâmetro self, ou seja, terão a capacidade de sentar e rolar.
# Criando a instância para um cachorro específico:

your_dog = Dog('toby',5) #Instância
print("O nome do seu cachorro é "+ your_dog.name.title() + ".")
print ("A idade do seu cachorro é "+ str(your_dog.age)+ ".")


# Em your_dog() é dito o nome e idade do cachorro. Quando o python lê isso, ele chama o método __init__()
# de Dog com os argumentos 'toby' e 5, ele cria uma instância que representa esse cachorro e não tem instrução
# return explícita, mas o python devolve automaticamente a instância. 

#---------- Acessando atributos
# Para acessar os atributos de uma instância utilize a notação de ponto:
your_dog.name  
# A notação de ponto é usada para encontrar o valor de um atributo, no caso, ele vê a instância your_dog e 
# encontra o atributo name associado. É o mesmo atributo referenciado como self.name na classe Dog()
# Usando a mesma abordagem para age. Como visto antes em outros capítulos, a função .title() no print, serve para
# começar o valor do atributo referente com letra maiúscula. E no segundo print, convertendo o valor para uma string.
# 
#---------- Chamando métodos
#  Depois de criar uma instância da classe Dog, pode usar a notação de ponto para chamar qualquer método da classe.
# Fazendo o cachorro sentar e rolar:
your_dog.sit()
your_dog.roll_over()

# Para chamar um método, tem que especificar a instância, no caso your_dog, e o método que quer chamar separados por um ponto
# Quando Python lê your_dog.sit(), ele procura o método sit() na classe Dog e executa o código. Do mesmo jeito para your_dog.roll_over()
# Quando atributos e métodos recebem nomes descritivos de forma apropriada como name, age, sit... pode ser mais prático para 
# identificar o que o código fará.
print("-------------------")
#---------- Criando várias instâncias
# É possível criar várias instâncias, vamos criar uma chamada my_dog
my_dog = Dog('belinha', 2)
# e agora chamaremos todas as instâncias
print("O nome do seu cachorro é " + your_dog.name.title() +".")
print("Seu cachorro tem "+ str(your_dog.age)+" anos.")
your_dog.sit()
print("\n")
print("O nome do meu cachorro é " + my_dog.name.title() +".")
print("Meu cachorro tem "+ str(my_dog.age)+" anos.")
my_dog.sit()
print("\n\n")

# Mesmo se fosse usado o mesmo nome e idade para o segundo cachorro o Python criaria uma instância separada da
# classe Dog. Desde que cada instância receba um nome de variável diferente ou ocupe uma única posição então tudo certo.
# Vou mostrar um exemplo para você mesmo escolher o nome e idade do seu doguinho:
class Dog2():        #Definição da classe
    def __init__(self, name, age):  
        self.name = name        #Definições do que a classe irá fazer
        self.age = age

nome= input("Diga o nome do seu doguinho: ")
idade= int(input("Digite a idade do seu bichinho: "))
seu_dog = Dog2(nome, idade)

print("O nome do seu cachorro é " + seu_dog.name.title() +".")
print("Seu cachorro tem "+ str(seu_dog.age)+" anos.")

#---------- Trabalhando com classes e instâncias
# Os atributos de uma instância podem ser modificados diretamente, ou escrever métodos que atualizem os atributos de formas específicas
# Faremos uma nova classe chamada Car() que terá informações sobre o tipo de carro trabalhado
#
#
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

# Na classe Car() é definido o método init com o parâmetro self primeiro, como feito em Dog(). Também é fornecido os outros 3 parâmentros:
# year, make, e model, fazendo referência ao ano, marca e modelo do carro. O método init suporta esses parâmetros e os armazena nos atributos
# que serão associados. O método get_descriptive_name() coloca os atributos year, make e model em uma string. Evitando que seja necessário exibir o valor
# de cada atributo separadamente. Para trabalhar com os valores dos atributos, usou-se self.make, self.model, e self.year.
# Depois foi criado uma instância da classe Car em novo_car, para atribuir os dados, então chamando o get_descriptive_name() para mostrar o carro que foi indentificado.

# ---------- Definindo um valor default para um atributo
# Todo atributo de uma classe precisa de um valor inicial mesmo que seja 0 ou string vazia. Por exemplo, quando definimos um valor default,
# é preciso especificar esse valor no corpo do método init; se isso for feito para atributos, então não precisa incluir parâmetro para ele.
# Acrescentaremos um atributo odometer_reading que começará com o valor 0, e um método read_odometer() que lerá  hodômetro do carro.
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

# As vezes o python chama o método init para criar uma nova instância, e então cria um novo atributo chamado odometer_reading e define seu valor inicial com 0.
# Também teve o método read_odometer() que facilita a leitura da quilometragem.

#  ---------- Modificando valores de atributos
# É possível alterar o valor de um atributo de três maneiras: por meio de instância, definir o valor com um método ou incrementá-lo.
# --- 1º: forma direta
# Isso é feito através do acesso em instância
novo_car2.odometer_reading = 25
novo_car2.read_odometer()

# Usa-se a notação de ponto para acessar o atributo odometer_reading do carro e definir o valor diretamente.
# --- 2º: Método
# É bem importante ter métodos que atualizem os atributos, em vez de acessar o atributo, passaremos o novo valor para um método que trate
# a atualização internamente

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
            
# Houve o acréscimo com update_odometer(). Esse método aceita um valor de quilometragem e o armazena em 
# self.odometer_reading. Depois é chamado o update_odometer() e é passado o valor de 20 como argumento, definindo a leitura com 25.
# A função é estendida para sempre que  a leitura do hodômetro seja modificada, então ele verifica se o novo valor do hodômetro faz sentido
# antes de modificar o atributo. Se a nova quilometragem for maior ou igual à já existente, então poderá atualizar o valor de leitura com um novo.
# Se for menor, então receberá um aviso que não pode ser modificado.

# --- 3º: Incrementenado o valor de um atributo com um método
# Às vezes, é necessário incrementar o valor de um atributo de determinada quantidade, em vez de definir um valor novo.
# Supondo que iremos comprar um carro usado e andamento 50 quilometros entre o instante que é comprado ao que é registrado.
# Um método que permite passar essa quantidade e somar o valor ao da leitura é:
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

carro_usado.increment_odometer(22)
carro_usado.read_odometer()

# Esse método increment_odometer() aceita uma quantidade de quilometros e soma esse valor a self.odometer_reading.
# É criado e definido o carro_usado, e o hodômetro está com valor de 26 KM, chamado de update_odometer() e passando-lhe o valor de 26KM
# Depois é chamado o increment_odometer() e passado um valor de 50 KM, para somar com o que já tinha de 26 KM. Resultando em 76 KM.
#
#
#