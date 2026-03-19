#crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)

print(20*'=','Tratando vário valores',20*'=')
soma = 0
cont = 0

while True:
    num = int(input('Informe um número inteiro [999 para parar]: '))
    #condição de parada
    if num == 999:
        break
    else:
        soma += num
        cont += 1
print(f'Você digitou {cont} números e a soma foi {soma}')
print('FIM')