cont = 1
while cont <= 100:
       print(cont)
       cont += 1

for variavel in [2,3,5,78]:
       print (variavel)

for isso in range(1,101):
       print(isso)

for aquilo in range(5):
       print("Oi")


frase = "Girls Generation"
for letra in frase:
        print (letra)

    
def area_triang(base,altura):
       return base*altura / 2

triang1 = area_triang(4,6) 
triang2= area_triang(3,7)
print(" Área do triângulo 1 é %.2f ."%(triang1) )  
print(" Área do triângulo 2 é %.2f ."%(triang2) )

batata= 123
def func( ):
       global batata  # pedindo permissao
       print(batata)
       batata=batata * 2 # agora vai

func( )
print(batata)

def fat(n):
       if n==0:
              return 1
       else:
              return n *fat(n-1)
print("5! é igual a %i. " %(fat(5)))
print(" 2! é igual a %i. "%(fat(2)))
print(" 21! é igual a %i. " %(fat(21)))


def soma(n):
    
       if n == 0:
              return 0
       else:
              return n + (n-1)
print("Soma de 5 com o número anterior a ele (4) é %i."%(soma(5)))


print("Soma de 9 com o número anterior a ele (8) é %i."%(soma(9)))