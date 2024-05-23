'''Descrição
Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

Morango:
Peso mínimo: 150 gramas
Textura: Suave (smooth)
Cor: Vermelha (red)
Laranja:
Peso mínimo: 120 gramas
Textura: Suave (smooth)
Cor: Laranja (orange)
Banana:
Peso mínimo: 150 gramas
Textura: Áspera (rough)
Cor: Amarela (yellow)
Maçã:
Peso mínimo: 130 gramas
Textura: Ápera (rough)
Cor: Vermelha (red)
Importante:
É necessário que a ordem das condições elif  seja respeitada conforme a descrição do desafio. Lembrando que, no Python, a indentação é fundamental para a definição de blocos de código, como os que pertencem a loops e funções. Se a indentação estiver incorreta, o Python não conseguirá interpretar corretamente o bloco de código, resultando em erros ou comportamento inesperado.

Entrada
Seu código deve receber as seguintes entradas do usuário:

Peso da fruta (em gramas): um número real que representa o peso da fruta.
Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.
Saída
O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
150
smooth
red	A fruta é um morango!
140
rough
yellow	Não foi possível classificar a fruta.
150
smooth
orange	A fruta é uma laranja!'''

def prever_fruta(peso, textura, cor):
    if cor == "red":
        if textura == "smooth":
            if peso >= 150:
                return "A fruta é um morango!"
        elif textura == "rough":
            return "A fruta é uma maçã!"
    elif cor == "orange":
        if textura == "smooth" and peso >= 120:
            return "A fruta é uma laranja!"
    elif cor == "yellow":
        if textura == "rough" and peso >= 150:
            return "A fruta é uma banana!"
    
    return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)
