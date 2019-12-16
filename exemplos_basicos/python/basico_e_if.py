nome = input("Seu nome:   ")
idade = int(input("Sua idade por favor: "))
curso = input ("Escreva seu curso: ")
if idade > 30:
    print("Você é velho")
elif idade < 20 :
    print("Não tao novo")
elif idade < 16:
    print("Você é novo")

print ('Oi',nome, '.Sua idade é :', idade , '.Está no curso de ', curso)

nota1 = int(input("Primeira nota: "))
nota2 = int(input ("Segunda nota: "))
nota3 = nota1 + nota2
print('{} / {} = '.format(nota3,2))
print(nota3 / 2)