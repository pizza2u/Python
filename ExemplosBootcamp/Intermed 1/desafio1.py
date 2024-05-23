'''Desafio
Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve solicitar apenas uma vez o valor de depósito.

Entrada
O programa deve receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.

Saída
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada	Saída
500.50	Deposito realizado com sucesso!
Saldo atual: R$ 500.50
-100	Valor invalido! Digite um valor maior que zero.
0	Encerrando o programa...'''

valor = float(input())

if valor > 0:
    saldo_formatado = "{:.2f}".format(valor).replace(',', '.')  # Formata o valor com 2 casas decimais e substitui ',' por '.'
    print("Deposito realizado com sucesso!\nSaldo atual: R$", saldo_formatado)
    
elif valor == 0:
    print("Encerrando o programa...")
   
else:
    print("Valor invalido! Digite um valor maior que zero.")