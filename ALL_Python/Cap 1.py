#COMANDOS BÁSICOS - CAPÍTULO 1
#====================================================
# TÓPICO 1 - EXPRESSÕES E SAÍDA DE DADOS

# Soma: N + Nx                     N= Número qualquer
# Subtração: N- Nx                 Nx= Outro número
# Multiplicação: N * Nx
# Divisão inteira: N* Nx
# Divisão: N/Nx
# Divisão inteira: N // Nx
# Resto da divisão: N  % Nx
# Potenciação N**p               p= potência

#__________________________________________________
# APLICAÇÕES
# Exemplo 1:
# Converter celsius para fahrenheit
# F=(9C/5)+32
 # 23ºC em tal cidade, quando ficaria em Fº?
print(9*23/5+32) #print() - mostra o resultado obtido dentro dos parênteses
 # Resultado= 73,4

#exemplo 2:
# Funções
# f(x)=2x^2-4x+2
# Caso f(3)
print(2*3**2-4*3+2) #resultado=8
# Caso f(5)
print(2*5**2-4*3+2) #resultado=40

#-------------------------------------------------------------------------------------------------
# TÓPICO 2- VARIÁVEIS
# Variáveis são letras ou nomes que vão receber um objeto.

#_______________________________________________________
# APLICAÇÕES
# Exemplo 3:
# Vamos inserir a variável x que vai receber 5
x=5
print(x)  # e vai ser mostrada
# Agora vamos inserir em uma função
y= 2*x**2-4*x+2 #escrevi a função como y e inseri o x anterior
print (y) # vai printar o resultado da resolução com f(5) que é 32

# Exemplo 4:: Mais variáveis
horas=4
minutos= 45
segundos=12
print(horas*3600+minutos*60+segundos)

# Não é possivel começar nome de variável com numeros
# Sensiveis ao caps lock,ou seja, se eu tiver horas e Horas, vão ser coisas diferentes
#-----------
#BÔNUS:
# Além de combinar e concatear números, também dá pra fazer o mesmo com strings.
# Exemplo bônus 1:
first_n= ("Fulano")
last_n=("Silva")
full= first_n+ " " + last_n
print(full) # Que vai printar Fulano Silva
#----------------------------------------------------------------------------------------
# TÓPICO 3- ENTRADA DE DADOS
# Função input - passa uma pergunta e o comando retorna a resposta do usuário
#____________________________________________________________
# APLICAÇÕES
# Exemplo 5:
seu_nome = input('Qual seu nome bro?!\n') #\n serve para uma quebra de linha
print(seu_nome)
# FÁAAcil né
#-----------
#BÔNUS: MÉTODOS DE STRING
# Aqui vai alguns macetes para configurar strings a partir de métodos.
# EXEMPLO Bônus 2:
name= ('programar em Python é massa') 
print(name.title()) #O método title() exibe cada palavra com  uma letra maiúscula no inicio.
print(name.upper()) # upper() vai exibir todas as letras em maiusculo
print(name.lower()) # lower() vai exibidr tudo em minusculo

# EXEMPLO Bônus: 3
# Funções strip() e split(), são capazes de limpar uma string e separar uma string em uma lista,respectivamente
str_suja = "blabla\n"
print(str_suja.strip()) #Contém apenas o texto, só o que importa
nome= "Algum Nome"
print(nome.split("  ")) # Separou a string em uma lista, usando o espaço " ", como delimitador

nom="a ,b, c, d"
print(nom.split(" , "))
# Assim como em upper e lower, as variáveis originais continuam intocadas, a original continua guardada
# Esses dois métodos são especialmente úteis em exercícios de arquivos, ja que cada linha de um arquivo termina com "\n" e geralmente a gente tem várias informações por linha e queremos separar elas de alguma forma.

# EXEMPLO Bônus: 4
# Index() e find() esses métodos têm a mesma finalidade, com eles podemos saber a localização da primeira ocorrência de um caractere na string
# A diferença é que o index() retorna um erro caso o caractere não exista, enquanto find() retorna o -1
procurando="eu amo meu xbox"
print(procurando.find("a")) # 3
print(procurando.index( "a")) # 3

print(procurando.find(" i ")) # -1
#print(procurando.index( "i"))  # erro

 # O index é mais usado quando se tem certeza que existe caractere na string, com find podemos checar

