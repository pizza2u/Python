'''
Descrição
Você foi contratado para desenvolver um sistema que normaliza dados de um conjunto de registros financeiros para facilitar a análise. A normalização Min-Max (Escalonamento) é especialmente útil para trazer todos os valores para uma mesma escala, facilitando a comparação entre diferentes registros. Seu objetivo é escrever um programa que receba uma lista de valores financeiros e retorne esses valores normalizados no intervalo [0, 1] usando a técnica de normalização Min-Max.

Entrada
A entrada do seu programa deve ser uma lista de números reais que representam os valores financeiros. Por exemplo:
[1500.0, 2000.0, 2500.0, 3000.0, 3500.0]

Saída
A saída deve ser uma lista de números reais normalizados no intervalo [0, 1]. Cada valor deve ser transformado de acordo com a fórmula de normalização Min-Max:
x_norm = (x - x_min) / (x_max - x_min)
'''

# Obtém os valores financeiros como uma lista de entrada do usuário,
# convertendo cada valor para float após remover espaços em branco e dividindo a entrada pelos caracteres de vírgula.
entrada = [float(valor.strip()) for valor in input().split(',')]

# Define a função de normalização Min-Max.
def min_max_normalization(data):
    # Encontra o menor e o maior valor na lista de dados.
    min_val = min(data)
    max_val = max(data)
    
    # Verifica se todos os valores são iguais.
    if max_val == min_val:
        # Se todos os valores são iguais, retorna uma lista de zeros.
        return [0.0] * len(data)
    
    # Aplica a fórmula de normalização Min-Max para cada valor na lista de dados.
    normalized_data = [(x - min_val) / (max_val - min_val) for x in data]
    # TODO: Aplique a fórmula de normalização Min-Max para cada valor na lista de dados.
    return normalized_data

# Imprime os valores normalizados.
print(min_max_normalization(entrada))