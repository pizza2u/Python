lista=["eu","amo","snsd"]
string="é verdade"
lista.append(string)
print(lista)

lista2=[" ainda","até agora"]
lista.extend(lista2)
print(lista)

print(lista+lista2)

print(lista.index("amo"))

if "cerveja" in lista:
    print(lista.index("cerveja"))
else:
    print("Num tem ")


tupla= ("s",2)
print(tupla)

tupla2=("e",12,3.14)
print(tupla2[1])
print(tupla2[-1:-3:-1])

(a, b ,c)= tupla2
print(a)
print(b)
print(c)

lista_new = ["carro",13,2.2]
(a,b,c,)= lista_new
print(lista_new[0])
print(lista_new[1])
print(lista_new[2])


dicion = {'chave': 'valor'}
print(type(dicion))
print(dicion)
dicio_2 = {'primeiro': 1,'segundo': 2, 'terceiro': 3}
dicio = dict(primeiro=1, segundo=2, terceiro=3)
dicio_4 = dict([('primeiro',1),('segundo',2),( 'terceiro',3)])
dicio_5 = {name: idx + 1 for idx, name in enumerate(('primeiro', 'segundo', 'terceiro'))}
dicio_6 = dict({'primeiro': 1, 'segundo':  2, 'terceiro': 3})


idade= {"Holand": 16 , "Oxe": 12 , " Fulane": 23}
print(idade["Oxe"])

pessoa={
    "Nome": "Liniker",
    "Profissão": " Cantora",
    "Viva": True,
    "Músicas":[" Via lactea","Não adianta"," Calmô"],
    (1,2,3):"fds"

}
print(pessoa["Músicas"][2])

people={"Name": "Naruto"," Profissão": "Ninja"}
print("Name" in people)