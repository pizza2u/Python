'''
Descrição
Filtrar dados por palavras-chave é uma técnica útil na análise de textos, como comentários, resenhas ou respostas em pesquisas. Dada uma lista de strings e uma palavra-chave, você deve retornar uma nova lista contendo apenas as strings que contêm a palavra-chave.

Entrada
Uma lista de frases e uma palavra-chave. Por exemplo: 
o filme foi emocionante, o enredo deixou a desejar, ele emociona
emociona

Observação: A primeira entrada consiste na lista de frases e a segunda na palavra-chave.

Saída
A saída esperada é uma nova lista de frases que contêm a palavra-chave indicada (por exemplo: ['o filme foi emocionante', 'ele emociona']). Para isso, você deve iterar pela lista de frases e adicionar à nova lista apenas as frases que contêm a palavra-chave.
'''

# Recebe uma entrada do usuário e a divide em uma lista de strings utilizando ', ' como delimitador
strings = input().split(', ')
# Recebe uma entrada do usuário como a palavra-chave para filtragem
palavra_chave = input("Digite a palavra-chave para filtragem: ")

# Define a função para filtrar strings por uma palavra-chave específica
def filtrar_por_palavra_chave(strings, palavra_chave):
    # Inicializa uma lista vazia para armazenar as frases que contêm a palavra-chave
    filtradas = []
    
    # Itera sobre cada frase na lista de strings
    for frase in strings:
        # Verifica se a palavra-chave está presente na frase
        if palavra_chave in frase:
            # Se encontrou a palavra-chave na frase, adiciona à lista filtradas
            filtradas.append(frase)
    
    # Retorna a lista filtrada contendo apenas as frases que contêm a palavra-chave
    return filtradas

# Chama a função filtrar_por_palavra_chave com as strings e a palavra-chave fornecidas pelo usuário
print(filtrar_por_palavra_chave(strings, palavra_chave))
