'''
Descrição
Agrupar dados por faixas etárias é uma maneira comum de categorizar e analisar dados demográficos. Dada uma lista de idades, você deve agrupar as idades em faixas etárias e contar quantas pessoas há em cada faixa.

Entrada
Uma lista de idades (por exemplo: 15, 22, 34, 45, 52, 67, 80).

Saída
Um dicionário onde as chaves são as faixas etárias e os valores são as contagens de pessoas em cada faixa (por exemplo: {'0-18': 1, '19-35': 2, '36-50': 1, '51-70': 2, '71+': 1}). O que fazer: Definir as faixas etárias e iterar pela lista de idades, incrementando a contagem apropriada para cada faixa.
'''

# Entrada do usuário
idades = list(map(int, input().split(',')))

# Define uma função chamada agrupamento_idade que recebe uma lista de idades e retorna um dicionário com contagem de idades em grupos pré-definidos
def agrupamento_idade(idades):
    # Inicializa um dicionário com grupos de idade como chaves e contadores iniciados em zero como valores
    grupos = {'0-18': 0, '19-35': 0, '36-50': 0, '51-70': 0, '71+': 0}
    
    # Itera sobre cada idade na lista de idades
    for idade in idades:
        # Verifica em qual faixa etária a idade se encaixa e incrementa o contador apropriado
        if idade <= 18:
            grupos['0-18'] += 1
        elif idade <= 35:
            grupos['19-35'] += 1
        elif idade <= 50:
            grupos['36-50'] += 1
        elif idade <= 70:
            grupos['51-70'] += 1
        else:
            grupos['71+'] += 1

    # Retorna o dicionário com a contagem de idades em cada grupo
    return grupos

# Chama a função agrupamento_idade com a lista de idades fornecida como entrada do usuário e imprime o resultado
print(agrupamento_idade(idades))
