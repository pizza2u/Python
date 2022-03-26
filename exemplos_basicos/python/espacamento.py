nome = input(" Fala bro : ") # Insira algo
print(" Olá amigoa {:>20}!".format(nome)) # espaçamento de 20 caracters para direita
print(" Olá amigoa {:<20}!".format(nome))# espaçamento de 20 caracters para esquerda
print(" Olá amigoa {} !".format(nome)) #normal
print(" Olá amigoa {:^20}!".format(nome)) #centralizado
print(" Olá amigoa {:=^20}!".format(nome)) #nome + sinal de = para outros caracters
print(" Olá amigoa {:0^20}!".format(nome)) # da mesma forma anterior so mudou o sinal para 0
