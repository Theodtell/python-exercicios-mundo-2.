""" refaça o desafio 035 e acrescente o recurso de mostrar que tipo de triângulo será formado:
- equilátero - todos os lados iguais
- esóceles - dois lados iguais
- ecanelo - todos os lados diferentes
desafio035: desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo
"""

print(20*'='+'Analisador de triângulos'+ 20*'=')
reta1 = int(input('Informe o primeiro lado: '))
reta2 = int(input('Informe o segundo lado: '))
reta3 = int(input('Informe o terceiro lado: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 and reta2 == reta3:
        print('Esse é um triângulo equilátero')
    elif reta1 == reta2 != reta3 or reta2 == reta3 != reta1 or reta3 == reta1 != reta2:
        print('Esse é um tringulo Isósceles')
    else:
        print ('Esse é um triângulo escaleno')