#Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantqas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de 50, 20, 10 e 1

print(15*'=-')
print('{:^30}'.format('CAIXA ELETRÔNICO'))
print(15*'=-')

while True:
    valor = int(input('Qual valor você quer sacar? '))
    total = valor
    ced = 50
    totalced = 0
    while True:
        if total >= ced:
            total -= ced
            totalced += 1
        else:
            if totalced > 0:
                print(f'Total de {totalced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totalced = 0
            if total ==0:
                break
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja sacar outro valor? [S/N] ')).upper().strip()
    if opcao == 'N':
        break
print('Volte sempre!')
