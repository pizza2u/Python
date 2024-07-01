'''
Descrição
Em muitos conjuntos de dados, valores duplicados podem distorcer análises e resultados. Dada uma lista de números, você deve remover os valores duplicados e retornar uma lista com valores únicos.

Documentação: https://docs.python.org/pt-br/3/tutorial/datastructures.html

Entrada
Uma lista de números que pode conter duplicatas. Por exemplo: 1, 2, 2, 3, 4, 4, 5.

Saída
Uma nova lista contendo apenas valores únicos. Por exemplo: [1, 2, 3, 4, 5]. O que fazer: Criar um conjunto a partir da lista para remover duplicatas e depois converter de volta para uma lista.
'''

# Recebe a lista do usuário
entrada = input()
# Converte a string de entrada em uma lista de números
lista = [int(x.strip()) for x in entrada.split(',')]

# TODO: Remova as duplicatas:
lista_unica = list(set(lista))

# É Exibido a nova lista sem valores duplicados
print(lista_unica)