# Converter celsius para fahrenheit
# F=(9C/5)+32
# Digite a temperatura que está agora em sua cidade:
temperatura = int(input("Diga ai quantos graus está aí: "))
fahrenheit = 9*temperatura/5+32
print("Faz " + str(fahrenheit) + "º Fahrenheit")

# Função quadratica
# Digite os valores de a,b, e c da sua função:
a = int(input("Digite o valor de 'a': "))
b = int(input("Digite o valor de 'b': "))
c = int(input("Digite o valor de 'c': "))
x = int(input("Digite o valor para x: "))
fx = (a*x**2) + b*x + c
print("O resultado da sua função é: "+ str(fx))

# Definindo nomes
primeiro_nome = input("Diga seu primeiro nome: ")
segundo_nome = input("Diga seu segundo nome: ")
print(f'Nome completo:  {primeiro_nome + " " + segundo_nome}')

#Ou 

full_name = primeiro_nome + " " + segundo_nome
print(full_name)

# Mudança no tamanho das letras
print(full_name.title()) 
print(full_name.upper())
print(full_name.lower())

print(full_name.find("o")) 
print(full_name.index( "z"))
