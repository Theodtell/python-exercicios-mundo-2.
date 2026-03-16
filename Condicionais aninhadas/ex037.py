#escreva um programa que leia um numero inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário; 2 para octal e 3 para hexadecimal

print (10*'=','Convertendo números',20*'=')

n = input('Informe um número para a conversão: ')
mensagem = input('''Você deseja converter para:
[1] Binário?
[2] octal
[3]hexadecimal?
(informe apenas o número)''')

if mensagem == '1':
    print(bin(int(n))[2:])
elif mensagem == '2':
    print(oct(int(n))[2:])
elif mensagem == '3':
    print(hex(int(n))[2:])
else:
    print('Não consegui entender o seu pedido, tente novamente.')