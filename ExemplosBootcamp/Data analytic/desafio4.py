'''
Descrição
Em análise de dados, a identificação de valores ausentes (nulos) é crucial, pois pode afetar a integridade e a qualidade dos dados. Dada uma lista de valores, você deve contar quantos desses valores são None, que representam dados ausentes.

Documentação: https://docs.python.org/pt-br/3/tutorial/datastructures.html

Entrada
Uma lista de valores númericos positivos e valores None. Por exemplo: 1, None, 2, None, 3, None .

Saída
Um número inteiro que indica quantos valores nulos estão presentes na lista. Por exemplo: 3. O que fazer: Conte quantos elementos são None usando a função count do Python.
'''
# Receber a lista do usuário
entrada = input()

# Converter a string de entrada em uma lista de valores
lista = [int(x.strip()) if x.strip().isdigit() else None for x in entrada.split(',')]

# TODO: Conte quantos elementos são None usando a função count:
contador_nulos = lista.count(None)

# Exibir o resultado
print(contador_nulos)