''' ordem de precedência
1 -> ()(quem estiver em parenteses)
2-> **(potencia)
3-> *(multiplicação); /(divisao); //(divisao inteira); %(resto de divisao)
4-> +(soma); -(subtração)'''

# exemplos

#---------------------- SOMA
n1 = int(input(" Numero um: "))
n2 = int(input("numero dois: ")) #inserir numeros
s = n1 + n2
print(" soma é ",s)

#------------------------- subtração
n1 = int(input(" Numero um: "))
n2 = int(input("numero dois: ")) #inserir numeros
s = n1 - n2
print(" subtração é ",s)

#------------------------------ multiplicação
n1 = int(input(" Numero um: "))
n2 = int(input("numero dois: ")) #inserir numeros
s = n1 * n2
print(" o resultado é ",s)

#----------------------------- divisão normal
n1 = int(input(" numerador: "))
n2 = int(input("divisor: ")) #inserir numeros
s = n1/ n2 #o resultado pode ser um numero fracionário
print(" a divisao normal é ",s)

#----------------------------------- Potência
n1 = int(input(" Numero : "))
n2 = int(input("numero da potencia: ")) #inserir numeros
e = n1 ** n2
print(" a potencia é {}".format(e))


#-------------------------- Divisão inteira

n1 = int(input(" numerador: "))
n2 = int(input("divisor: ")) #inserir numeros
s = n1// n2 # o resultado será um numero inteiro
print("o resultado da divisao inteira é ",s)

#---------------------------------- resto de divisao
n1 = int(input(" numerador: "))
n2 = int(input("divisor: ")) #inserir numeros
s = n1 %n2 # % para mostrar o resto da divisao
print(" o restante da divisão é ",s)