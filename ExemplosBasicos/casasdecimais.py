# Código com uso de format
n = float(input('number :  '))

print("Número normal: ", n )
print('Número com casas decimais:{:.4f} ' .format(n))   #:. xf -> casas decimais   ;   .format(algo) -> para funções com  numeros
print('Número com casas decimais e zero na frente:{:08.4f} ' .format(n))

