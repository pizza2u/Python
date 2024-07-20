## O programa abaixo deve calcular a média dos valores digitados pelo usuário.
## No entanto, ele não está funcionando bem. Você pode consertá-lo?

def calcular_media(valores):
    soma = 0.0
    for valor in valores:
        soma += valor
    tamanho = len(valores)
    if tamanho == 0:
        return 0  # Evitar divisão por zero se a lista estiver vazia
    media = soma / tamanho
    return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor:')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valores.append(float(valor))
        except ValueError:
            print("Por favor, digite um número válido ou 'ok' para calcular a média.")

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
