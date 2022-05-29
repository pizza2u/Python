# CAPÍTULO 8 -  MÉTODOS DE LISTA & TUPLAS E DICIONÁRIOS
# Já vimos várias funções para listas, mas vamos ver uns a mais
# Append() e extend()
# Respectivamente, o primeiro, serve para acrescentar um novo elemento a lista, enquanto extend() concatena duas listas
lista=["eu","amo","francês"]
string="é verdade"
lista.append(string)
print(lista)

# Acrescentamos ao fim da lista
# ALWAYS

# E se juntarmos duas listas?

lista2=[" ainda","até agora"]
lista.extend(lista2)
print(lista)

# Mas poderia usar o operador de soma tambem
print(lista+lista2)

# INDEX()
# A gente viu essa função para string, mas veremos para listas também

print(lista.index("amo"))
# Como num vetor se conta começando do 0, temos que "amo" se encontra na posição 1

# E quando não existe tal elemento:
if "cerveja" in lista:
    print(lista.index("cerveja"))
else:
    print("Num tem :( ")

#--------------------------------------
# TUPLAS E DICIONÁRIOS
# As listas são muito importantes na computação em geral porque o agrupamento de daos é necessário em todo programa.
# Então existem outros tipos de variáveis que podem agrupar dados, como tuplas e dicionários.

# Que é uma propriedade das listas que a gente fala bastante é a mutabilidade.
# A gente consegue criar uma lista e editar ela depois, apesar disso ser útil , existem casos em que a mutabilidade é ruim.
# Quando você tem um conjunto mutável de dados, você pode alterar alguma coisa sem querer e lascar tudo.
# E lá vem as tuplas

# As tuplas fazem um monte de coisas, mas pense primeiro que tuplas são listas imutáveis
tupla= ("s",2)
print(tupla)
# O processo de criação é bem parecido com a criação de listas. Só que em vez de colchetes[],usamos os parênteses()
tupla2=("e",12,3.14)
print(tupla2[1])
print(tupla2[-1:-3:-1]) # Caso não lembre o que acontece aqui, essa notação significa que queremos apenas uma parte da tupla
# A gente pegou uma fatia começando no item -1(ultimo) até o item -3, sem contar com ele.
# A gente também disse que essa fatia tem que ser copiada de -1 em -1, indo de trás para frente, o resultado ta invertido se você prestar atenção
# Mas se tentarmos editas, da mesma forma que lista, vai dar ERRO

# Uma das coisas mais úteis das tuplas é que a gente pode usa para "desempacotar" uma lista, ou outra tupla também

(a, b ,c)= tupla2
print(a)
print(b)
print(c)
# Vai printar cada elemento da tupla2

# Tammbém funcionaria se fosse uma lista
lista_new = ["carro",13,2.2]
(a,b,c,)= lista_new
print(lista_new[0])
print(lista_new[1])
print(lista_new[2])

# Mas repara que tanto nas listas quanto nas tuplas, a gente precisa saber o índice de cada item pra poder acessar ele. Mas em alguns casos

# USANDO DICIONÁRIOS EM PYTHON
# DICIONÁRIOS
# Ou também chamados de Dicts são coleções de itens (tipo listas) armazenados de forma
# não ordenada e que contém uma chave e valor nos seus elementos
# - uma chave que vai indexar determinado elemento
# - um valor que tem... um valor, mas diferentemente de listas, os índices podem ser qualquer tipo de valor imutável, como inteiros, 
# floats,strings,booleans e até tuplas.

# A sua sintaxe é básica {'chave': 'valor'}. Essas {} delimita o dicionário e chave separadas

dicion = {'chave': 'valor'}
print(type(dicio))
# Obviamente estamos conferindo o tipo da função que está na variável, do tipo dict

# Há 6 maneiras de fazer um mesmo dicionário

dicio_2 = {'primeiro': 1,'segundo': 2, 'terceiro': 3}
# também é possível utilizar a função dict do próprio Python
dicio = dict(primeiro=1, segundo=2, terceiro=3)
# utilizando a função zip para concatenar a chave:valor em um unico elemento dict
dicio_3= dict(zio(['primeiro','segundo', 'terceiro'],[1,2,3]))
# usando uma lista de tuplas com itens simbolizando chave e valor em um objeto dict
dicio_4 = dict([('primeiro',1),('segundo',2),( 'terceiro',3)])
# Por dict comprehensions também
dicio_5 = {name: idx + 1 for idx, name in enumerate(('primeiro', 'segundo', 'terceiro'))}
# e transformando uma varíavel do tipo dicionário em dicionário 
dicio_6 = dict({'primeiro': 1, 'segundo':  2, 'terceiro': 3})


# Dicionários em python são, assim como listas e tuplas, estruturas de agrupamento de dados, a principal característica é a personalização dos índices
idade= {"Holand": 16 , "Oxe": 12 , " Fulane": 23}
print(idade["Oxe"])


pessoa={
    "Nome": "Liniker",
    "Profissão": " Cantora",
    "Viva": True,
    "Músicas":[" Via lactea","Nao adianta"," Calmô"],
    (1,2,3):"fds"

}
print(pessoa["Músicas"][2])


# Operações com dicionário
#A gente pode usar o operador in, parecido com o que a gente fazia com listas
people={"Name": "Naruto"," Profissão": "Ninja"}
print("Name" in people)
# Vai retornar true, ele checa se existe alguma ket com o nome que a gente perguntou, e retornou true nesse exemplo porque existe uma key chamada name
# Quando a gente usou in em listas, ele retornou true se o valor existisse, aqui retornar True caso a Key exista
# Essa é a única diferença
