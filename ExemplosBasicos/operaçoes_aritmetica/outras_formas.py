# formas com format
n1 = int(input(" Numero um: "))
n2 = int(input("numero dois: ")) #inserir numeros
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
divint = n1 // n2
pot = n1 ** n2
rest = n1 % n2

print('a SOMA É {}\na subtração é {}\na multiplicação é {}\n'.format(s,sub,m))
print('a divisão normal é {}'.format(d))
print('a divisao com inteiros é {}\na potencia é {}\no resto de divisão é {}\n'.format(divint,pot,rest))