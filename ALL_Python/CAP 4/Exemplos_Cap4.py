Sherlock=False
Enola= True
Mycroft = True
Sherlock_e_Enola= Sherlock and Enola
print(Sherlock_e_Enola)

Sherlock_e_Mycroft= Sherlock or Mycroft
print(Sherlock_e_Mycroft)

nao_Sherlock= not Sherlock
print(nao_Sherlock)

if 1==1:
       print("1 é realmente 1") 
       
if 5==4:
       print("4 não é 5") 

idade=int(input("Idade: \n"))
if idade < 18:
       print(" Você é menor de idade!")  
print(" Sua idade é "+str(idade))


a= 55;
b=155;
c=1050;

if a>b or a>c:
    print("A variável 'a' é maior que todos")
elif a<b or b<c:
    print("A variável 'b' é maior que 'a' e menor que 'c'")


    var1=0
var2= int(input("Diga aí boy um número diga: "))

if var2>var1:
    print('Número maior que zero')
    if var2==1:
        print('O número foi 1')
    elif var2==2:
        print('O número foi 2')
    elif var2==3:
        print('O número foi 3')
    else:
        print('O número é maior que 3')
else:
    print("Número inválido")
