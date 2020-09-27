#CAPÍTULO 3 - TIPOS DE DADOS II
#=======================================================
# TÓPICO 1- STRINGS
# A patroa chegou!
# Okay eu sei, já mostrei sobre o \n e \t
# mas vou mostrar algo new
# A pergunta seria, podemos escrever aspas dentro da string, sendo que a string é iniciado com aspas
# valha mi deus
# Mas ai que ta, é so usar a contra barra também
# EXEMPLO 1:
oxe = 'e ai boy\nbora \' LA\''  
print(oxe)
# Isso também serve para aspas duplas usando \"
# Se colocar só uma \ na string vai dar erro então tem que ser
oxente = 'oia : \\'
print(oxente)

# String de várias linhas
# Tipo se você quiser colocar um texto tipo poema, não precisa ficar colocando \n, basta abrir e fechar o texto com três aspas simples ou três duplas
# EXEMPLO 2:
acompanha= '''Perna de pato
bico de pavão
meche nas minhas coisas
que eu arranco seu coração'''
print(acompanha) # Simples ne
 # E como foi visto nos capítulos anteriores a soma de string e operações como a multiplicação, mas vou botar mais exemplos pra você se ligar
 # EXEMPLO 3:
frase1= "Eu só queria..."
frase2= "que alguém colocasse 10000 reais na minha conta"
print( frase1+ '\n' +frase2)

# e a multiplicação
frase3= " EU NÃO SOU IRRITANTE"
print(frase3*10)
# Nem pense em usar a string para subtração ou divisão, vai ser trouxa


# ALÉM DESSES OPERADORES, podemos usar o in. Esse operador checa se existe uma letra ou substring dentro e outras string
# E lembra dos booleanos? Pois minine, vai retornar eles
#EXEMPLO 4:
nome = "Sherlock"
print("c" in nome) # True
print("a" in nome) # False
print("k" in nome) # True
# Preste atenção no serviço, esse operador NÃO é comutativo: (x in y) é diferente de (y in x)

# Agora chegue aprender mais uma funçãozinha
# Vos apresento a função len() para saber o tamanh de uma string
# OIA
# EXEMPLO 5:
fulano = "Sherlock"
print("O  tamanho do nome(ou quantidade de letras) " +fulano+" é:  ",len(fulano))

 # E se a gente botar um input aí
 #EXEMPLO 6:
contador= str(input(" Digite um nome:\n"))
print ("O tamanho do nome  "+contador+" é:  ",len(contador))

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# TÓPICO 2 - OPERAÇÕES COM STRINGS
# Ué, mas a gente não acabou de ver isso? Não more a gente aprendeu a usar
# Vamos pensar, como pegamos as letras de uma string de modo individual e como formatar?
# Se achegue
# EXEMPLO 7:
print("O nome do bixinho começa com "+nome[0])# Lembra que o nome que utilizamos foi Sherlock?! Se não, trate de lembrar porque não vou repetir
# Viu que apareceu só a incial S de Sherlock, então o colchetes [] coloca a letra específica que a gente quer
#A primeira letra tem índice 0, porque as contagens dos computadores começam em 0
# S - 0
# H - 1
# E - 2
# R - 3
# L - 4
# O- 5
# C- 6
# K- 7

# Fatiamento de String
# Oxe vamo cortar o que?
# Nam ome, preste atenção
# Além de usar colchetes para pegar só uma letra, a gente pode pegar uma fatiazinha
#EXEMPLO 8
print(nome[0:4]) # Sher
print(nome[4:8]) # Lock# os dois pontos: significa dizer que vai percorrer de tal localização a outra localização
# Mas repetiu o 4 né?! Né, mas o que quer dizer que pegamos de 0 e paramos na letra de índice 4(sem contar ela)
# E as strings são imutaveis ein, não pode editar
 

# FORMATAÇÃO
# Calma vai ser ligeiro, são só 3 que vou colocar aqui, mas vou deixar bem resumido

# .format()
# A única coisa que você precisa se esforçar pra fazer é colocar {n} dentro da sua string, com n sendo um número natural
# No final tu bota um .format(), e aí bota os valores que quer substituir dentro
# REPARE NA ORDEM VIU
# TOdo {0} no texto vai ser substituído pelo primeiro valor no .format()
# Olhe aqui EXEMPLO 9
olhe= 3.14
print(" Teste {0}".format("teste")) # teste teste
print("Teste {0}".format(2**3)) # teste 8
print("Teste {0} {1} {0}".format(olhe//3.14,"OPA")) #teste 1.0 OPA 1.0

# %
# Sim com %
# Já aviso que é a mais complicadinha
# WHY
# Porque tem que especificar o tipo do dado de acordo com isso aqui, segue o fio
# string - %s
# inteiro - %d
# float - %0.xf            Ali tem um x né, no lugar desse x tu coloca o número de casas decimais que você quer
                              # e arredonda automaticamente o número de casas decimais
# EXEMPLO 10:
exem= 2.5
print(" Teste %s"%("Oi"))
print(" Teste %d"%(3**2))
print(" Teste %.2f %s"%(exem/2,"UHLALALA"))

# Formatação com f
# APOI colocando f na frente da string, possibilita a gente colocar dentro da string{expressão}, que vai ser substituido automaticamente no texto
# EXEMPLO 11:
oto=5
print(f" Teste {oto}" ) # preste atenção que o f ta colado com as aspas
print(f"Teste {6**2}")
print(f"Teste {oto/2}")

# E FOI ISSO BENINAS,BENINOS E BENINES
#-------------------------------------------------------------------------------------------------------
#TÓPICO 3 - LISTAS
# Aguenta mais um round?
# Se sim, continue a leitura
# Foi muita informação eu sei, por isso vou TENTAR  ser o mais breve possivel

# Aqui a gente vai ver um pouco de vetores[VECTOR]
# Imagine que temos 3 notas, mas queremos agrupa-las
# As listas são como tabelas
# EXEMPLO 12:
notas=[5.8,8.9,7.5] # Os valores dentro de uma única variável
print(notas[0])
print(notas[1])
print(notas[2]) # E vai printar os números de acordo com a posição
# O mais legal é que os dados podem ser de qualquer tipo
# EXEMPLO 13:
lista = ['a','b',100, 3.60,True,[1, 2, 5, False,['texto'],60]]
print(lista[5][3]) # Para acessar False tem que indexar a mais de uma vez

# Alterando o valor dos négocio
# Mas HOW
#assim ó
lista[3] = 'psyduck'
print(lista) # E vai printar a lista com a substituição feita

# Operações com listas, ou vetores
#off: nem eu aguento mais
# Assim como as string, alguns operadores matemáticos funcionam com listas
# Bora tentar com +
# EXEMPLO 13
isso=[1,5,6]
aquilo=[7,2,0]
print(isso+aquilo) # Vai printar [ 1 5 6 7 2 0]
# SÓ DA PRA USAR ISSO COM LISTA VISSE
# Bora botar uma multiplicação pra ver o que acontece
cumbuca=isso*2
print(cumbuca) # Repetiu o vetor isso
# Aguenta um pouquinho ta acabando
# Se multiplicar por um número negativo, o vetor resultante vai ser um vetor vazio
# ********** IMPORTANTE ********
# Além dos operadores matemáticos, existem outros
# Um deles é o del, que usa para apagar itens da lista.
# EXEMPLO 14
aleat = [ 2,4,6] # O nosso 1 é o número 4
print(aleat[1])
del aleat[1]
print(aleat[1]) # Depois de deletado o 1 passa a ser o número 6

# Fora isso também tem o operador in, já visto antes
# Que vai checar se um determinado valor existe no vetor e retornar True or False
print(2 in aleat) # True
print( 4 in aleat) # False , já que foi apagado



# FIIIIIIIIIIIIIIIIIMMMMMMMMMMMMMMMMMMMMM
# EH ISTO





















