n = bool(input("Digite algo: "))

print(n) 
# Lógica bool -> caso seja digitado algo o valor retorna como True, se nada for digitado o valor retorna False


#--------------------------------------------------- Forma numerica
n = input("Digite algo: ")
print(n.isnumeric()) # .isnumeric representa uma pergunta do tipo "é numerico?" caso seja ele retorna True, caso não retorna False
# também diz se é possivel converter o valor em um numero do tipo primitivo int antes dele

#------------------------------------------------- Forma alpha
n = input("Digite algo: ")
print(n.isalpha()) #.isalpha() possui a mesma logica para um alfabetico

#------------------------------------------------ Forma alpha numerico
n = input("Digite algo: ")
print(n.isalnum()) #isalnum()retorna True para alfabeticos e numericos, retorna False em por exemplo ' '

#---------------------------------------------- Forma is upper
n = input("Digite algo: ")
print(n.isupper()) #isupper é uma função para retornar True casos as palavras ou letras escritas estiverem em maiusculo e False caso alguma esteja em minusculo.