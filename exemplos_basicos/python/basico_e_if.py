nome = input("Seu nome:   ") #-> input serve para pegar o dado escrito pelo usuário
idade = int(input("Sua idade por favor: "))
curso = input ("Escreva seu curso: ")
if idade > 30: #-> segue a mesma lógica de c e c++ : condição SE
    print("Você é velho")
elif idade < 20 :
    print("Não tao novo")
elif idade < 16:
    print("Você é novo")

print ('Oi',nome, '.Sua idade é :', idade , '.Está no curso de ', curso) #-> Imprime os dados obtidos

nota1 = int(input("Primeira nota: ")) #-> INT antes do INPUT: converse o número somente para inteiro
nota2 = int(input ("Segunda nota: "))
nota3 = nota1 + nota2   #-> nota 3 é o resultado da soma entre as notas inseridas
print('{} / {} = '.format(nota3,2)) #-> função para divisão
print(nota3 / 2) #->imprime a média(nota 3)
