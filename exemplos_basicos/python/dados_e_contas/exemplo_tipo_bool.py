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

#-------------------------------------------------- Forma lower
n = input("Digite algo: ")
print(n.islower()) #demonstra dizer para True caso o que foi digitado seja minusculo e False caso seja maisculo ou possua alguma letras maiuscula
#-------------------------------------------- Forma space
n = input("Digite algo: ")
print(n.isspace()) #demonstra dizer para True caso o que foi digitado seja apenas espaço e False caso tenha algo escrito

#-------------------------------------------- Forma capitalizada
n = input("Digite algo: ")
print(n.istitle()) #demonstra True caso tenha letras maiusculas e minusculas , e False para caso tenha somente um tipo na palavra(MA e mi)