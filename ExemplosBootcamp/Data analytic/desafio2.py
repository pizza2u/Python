

'''
Descrição
A mediana é uma medida de tendência central que é menos sensível a valores extremos do que a média. Dada uma lista de números, você deve calcular a mediana.

Entrada
Uma lista de números (por exemplo: 10, 20, 30, 40, 50).

Saída
Um número representando a mediana (por exemplo: 30.0). O que fazer: Ordenar a lista e encontrar o valor do meio (ou a média dos dois valores do meio se a lista tiver um número par de elementos).
'''

# Solicita ao usuário uma lista de números separados por vírgula e os converte para ponto flutuante
numeros = list(map(float, input().split(',')))

# Define a função para calcular a mediana de uma lista de números
def calcular_mediana(numeros):
    # Ordena a lista de números em ordem crescente
    numeros_ordenados = sorted(numeros)
    # Obtém o comprimento da lista ordenada
    n = len(numeros_ordenados)
    # Calcula o ponto médio da lista
    ponto_medio = n // 2

    # Verifica se a quantidade de números é ímpar
    if n % 2 == 1:
        # Se for ímpar, retorna o valor no meio da lista
        return numeros_ordenados[ponto_medio]
    else:
        # Se for par, retorna a média dos dois valores do meio da lista
        return (numeros_ordenados[ponto_medio - 1] + numeros_ordenados[ponto_medio]) / 2

# Chama a função calcular_mediana com a lista de números como argumento e imprime o resultado
print(calcular_mediana(numeros))
