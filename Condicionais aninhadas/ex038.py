#Escreva um programa que leia dois números inteiros e comprare-os, mostrando na tela uma mensagem: o primeiro valor é maior, o segundo valor é maior - não existe valor maior, os dois são iguais

n1= (int(input('Informe o primeiro número: ')))
n2 =(int(input('Informe o segundo número: ')))

if n1 > n2:
    print('{} é o maior número!'.format(n1))
elif n2 > n1:
    print('{} é o maior número!'.format(n2))
else:
    print('Os dois números são iguais!')
