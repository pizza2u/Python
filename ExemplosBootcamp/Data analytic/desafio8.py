'''
Descrição
A moda é a medida de tendência central que representa o valor mais frequente em um conjunto de dados. Em análise de dados, calcular a moda pode ajudar a identificar padrões e tendências.

Entrada
Uma lista de números (por exemplo: 1, 2, 2, 3, 3, 4, 4, 4).

Saída
Um número representando a moda ou uma lista de números se houver empate (por exemplo: 4 ou [2, 3, 4] em caso de empate). O que fazer: Contar a frequência de cada número e identificar o(s) número(s) com maior frequência.
'''

# Entrada do usuário e conversão para lista de números
lista_numeros = list(map(int, input("Digite uma lista de números separados por vírgula: ").split(",")))

def calcular_moda(lista):
    # Conta a frequência de cada número na lista
    contador = {}
    for num in lista:
        contador[num] = contador.get(num, 0) + 1
    
    # Encontra a frequência máxima
    max_frequencia = max(contador.values())
    
    # Encontra todos os números que têm a frequência máxima
    moda = [num for num, freq in contador.items() if freq == max_frequencia]
    
    # Retorna a lista de modas se houver empate, caso contrário retorna a única moda
    return moda if len(moda) > 1 else moda[0]

# Calcula e imprime a moda
print(calcular_moda(lista_numeros))
