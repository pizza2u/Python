anuncio = 'snsd está\nVoltando Viu\''  
print(anuncio)
print("\n")
acompanha= '''Perna de pato
bico de pavão
meche nas minhas coisas
que eu arranco seu coração'''
print(acompanha) 

frase = "O grupo da nação está voltando!! \n"
print( frase * 10)

nome =  "Tiffany"
print("a" in nome)
print(" O nome de " +nome+ " tem: ",len(nome), "letras")

contador= str(input(" Digite um nome: "))
print ("O tamanho do nome  "+contador+" é:  ",len(contador), "\n")

print("O nome de "+nome+" começa com "+nome[0] + "\n")
print(nome[0:4])
print(nome[4:7])

lista = ['taeyeon', 'yuri', 'hyoyeon','sunny']
print(lista)
lista.insert(0, 'yoona')
print(lista)

del lista[3]
print(lista)
popped_lista=lista.pop()
print(popped_lista)


lista.sort()
print(lista)

lista.reverse()
print(lista)
