#----------------------------------- Código 1
dia= int(input("Digite uma data:  "))
mes = int(input("Digite um mes:  "))
ano= int(input("Digite um ano:  "))

print (dia,"/",mes,"/",ano)
#-------------------------------------- Código 2
dia= int(input("Digite uma data:  "))
mes = int(input("Digite um mes:  "))
ano= int(input("Digite um ano:  "))

print(dia,mes,ano, sep = "/") #sep para inserir termos entre as vírgulas(recebe o "/")

#------------------------------- Código 3
dia= int(input("Digite uma data:  "))
mes = int(input("Digite um mes:  "))
ano= int(input("Digite um ano:  "))

print("{} / {} / {}".format(dia,mes,ano)) #-> cada chave armazena as variáveis do dia,mes,e ano