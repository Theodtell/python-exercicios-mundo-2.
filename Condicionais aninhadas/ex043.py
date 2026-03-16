"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa e calcule o seu IMC
18.5 - abaixo
18.5 - 25 - ideal
25 - 30 - sobrepeso
30 - 40 - obesidade
acima de 40 - obesidade morbida
"""

peso = float(input('informe o seu peso: '))
altura = float(input('Informe a sua altura:' ))

IMC = peso / (altura **2)

if IMC < 18.5:
    print('ATENÇÃO\nVocê está abaixo do peso!')
elif 18.5 <= IMC < 25:
    print('Peso ideal!')
elif 25 <= IMC < 40:
    print('ATENÇÃO\nVocê está com o sobrepeso!')
elif 30 <= IMC < 40:
    print('ATENÇÃO!\nVocê está com o obesidade!')
else:
    print('ATENÇÃO!!\n Você está com Obsidade Móbida!!')