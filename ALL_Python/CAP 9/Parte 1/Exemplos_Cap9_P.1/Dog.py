class Dog2():        
    def __init__(self, name, age):  
        self.name = name        
        self.age = age

    def sit(self):
        print(self.name.title()+" está agora sentado.")
    
    def roll_over(self):
        print(self.name.title()+" rolou!")

nome= input("Diga o nome do seu doguinho: ")
idade= int(input("Digite a idade do seu bichinho: "))
seu_dog = Dog2(nome, idade)

print("O nome do seu cachorro é " + seu_dog.name.title() +".")
print("Seu cachorro tem "+ str(seu_dog.age)+" anos.")
seu_dog.roll_over()
seu_dog.sit()