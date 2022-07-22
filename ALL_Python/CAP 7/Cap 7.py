# CAPÍTULO 7 - ARQUIVOS & EXCEÇÕES
#ºººººººººººººººººººººººººººººººººººººº
# ARQUIVOS: Todos os programas vistos até aqui, não utilizamos nenhum dado externo. Mas, pode ser útil ler os dados de um arquivo de texto, em vez de perguntar tudo pro usuário com input().
# Por exemplo, se tiver um arquivo de texto com as notas de todos os alunos de uma turma e quiser usar sua médias.
#-----------------------------------------------
# Função Open
# Para abrir um arquivo, usamos a função open(). Passamos como parâmentro o nome do arquivo que queremos e a letra r entre aspas
arquivo = open("arquivo.txt","a")

arquivo.close()

# Importante que ele fique na mesma pasta do programa

# Depois disso, pode até conferir na pasta em que salvou o programa, o arquivo txt vai estar lá,salvo na variável arquivo.
# Abrindo o arquivo assim a gente só consegue ler, mas não consegue escrever.
# Repara que temos o arquivo.close(), essa linha é OBRIGATÓRIA, se abriu o arquivo, tem que fechar antes de finalizar o programa
# Se abre, tem que fechar

#------------------------------------------------
# Função read()
# Quando o arquivo é aberto e colocado numa variável, ele não está em formato texto, a função read() é capaz de ler o arquivo e transformar em string
outro = open("texto.txt" , "b")

em_texto = outro.read()

outro.close()

# Dessa forma, todo o texto presente no arquivo vai ser armazenado na variável em_texto. Mas é possível ler uma linha de cada vez.
#--------------------------------------------
# Função readline()
# Serve para ler uma linha do arquivo ( 1ª) e salva numa variável.

new = open("arq.txt","r")
linha= new.readline()
new.close()

# Você tem que tomar cuidado quando estiver usando arquivos, só dá para LER UM ARQUIVO UMA VEZ
# Se usar a função read() num arquivo, ela não vai funcionar de novo, se usar a readline(), na segunda vez, ela vai ler a segunda linha, e assim por diante.
new = open("arq.txt","r")
linha= new.readline()
linha2= new.readline()
linha3= new.readline()

#-----------------------------------------
# Iterando pelo arquivo
# Dá para ler o arquivo inteiro, uma linha por vez, usando o for

leitura = open("arquiv.txt","r")

for linha in leitura:
       print(linha)

leitura.close()

# Esse código exibe todas as linhas do arquivo, o for vai repetir o código que estiver dentro do seu corpo para todas as linhas do arquivo

#-------------------------------------
# Escrevendo arquivo
# Primeiro precisa trocar o parâmetros r por w

agua=open("mouse.txt","w")

# Caso o arquivo não exista, criará um novo, mas caso já exista, será subescrito
# Depois que abrir o arquivo, tem que botar permissões de escrita, usando a função write()
agua.write("primeira linha\n")
agua.write("segunda pipipi\n")
agua.write("etc etc\n")

agua.close()

#========================================================
# TRATANDO EXCEÇÕES

#-----------------------------------------
# Reconhecendo exceções

# O exemplo mais simples(I) e direto que temos e
num=int(input("Digite um número: "))
result = 50/num
print(result)
# Agora pensa comigo, se o cara digita um 0 aí, vai dar treta
# É uma exceção

#----------------------------------------
# Tratando exceções
#  O que djabo é isso? Quando um erro acontece , aparece as letras vermelhas com o erro né, então, significa que a gente quer tratar manualmente os erros
# Em vez das letras em vermelho, o código vai executar.

numero=int(input("Digite um número: "))
try:
       resultado=30/numero
except:
       print("Não foi possível calcular")
       resultado = 0
finally:
       print(resultado)

# Palavra- chave try:
# Como no inglês, try significa tentar, e é usada para criar um bloco de código que talvez dê errado. Essa palavra é a  alma do tratamento de exceções. Só da pra tratar exceções que estão no bloco try

# Palavra- chave except:
# Como no inglês except é exceção, para defiinir o que deve acontecer caso dê erro. Significa que o código desse bloco não vai ser executado caso tudo dê certo.
# Repara que no código de exemplo, a gente usou um print() dizendo que não foi possível calcular.
# Se a gente colocar o except como no código anterior, o try vai chama-lo para qualquer erro, portanto,vamos especificar

numero=int(input("Digite um número: "))
try:
       resultado=30/numero
except ZeroDivisionError:
       print("Não foi possível calcular")
       resultado = 0
finally:
       print(resultado)

# Para especificar o erro, tem que especificar o nome do erro também, mas como DIABOS VOU SABER O NOME DO ERRO?
# Caro Watson, provoque o erro de proposito e veja o nome.
# O except pode tratar mais de um error

# Palavra-chave finally:
# COMO inglês, significa finalmente, o código vai ser executado sempre, independente de dar erro ou não no bloco try
# A ideia do finally é garantir que o código vai ser executado

#----------------------------------
# Usando só dois blocos
# Não é obrigatório a gente usar os três

try:
       numero=int(input("Digite um número: "))
       resultado=30/numero
except (ValueError, ZeroDivisionError):
       print("Não foi possível calcular")
       resultado = 0


# LIÇÃO DE HOJE
# Sempre confie no finally, pois sempre vai ser executado,e se o programa for apenas o exemplo sem o try,except, ele vai parar imediatamente caso seja 0 o valor inserido

new.close()
