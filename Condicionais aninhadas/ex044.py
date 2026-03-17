"""
Elabore um programa que calcule o valor a ser pago por um produto, considerano o seu preço normal e a condição de pagamento:
à vista dinheiro/cheque - 10% de desconto
Á vista cartão - 5% de desconto
em até 2x no cartão - preço normal
3x ou mais - juros de 20%
"""

print(10*'=','CALCULADORA DE PREÇOS',20*'=')
valor = float(input('Digite o valor do produto: '))
pagamento = int(input('''Informe a forma de pagamento (digite apenas o número:
[1] - À vista dinheiro/cheque
[2] - À vista no cartão
[3] - 2X no cartão
[4] - 3X ou mais no cartão
'''))

if pagamento not in [1,2,3,4]:
    print('Opção inválida')
elif pagamento == 1:
    novo_valor = valor - (valor * 0.10)
    print('O valor a ser pago é de R$ {}'.format(novo_valor))
elif pagamento == 2:
    novo_valor = valor - (valor * 0.05)
    print('O valor a ser pago é de R$ {}'.format(novo_valor))
elif pagamento == 3:
    novo_valor = valor + (valor * 0.20)
    print('O valor a ser pago é de R$ {}'.format(novo_valor))
else:
    print('O valor a ser pago é de R$ {}'.format(valor))