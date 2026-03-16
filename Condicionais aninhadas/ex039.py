"""faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
se ele aind avai se alistar
se é a hora de se alistar
se já passou do tempo de alistamento
seu programa também deverá mostrar o tempo que falta ou que passou do prazo
"""
from datetime import date

print(10*'=','ALISTAMENTO MILITAR',20*'=')

nome = str(input('Digite seu nome completo: '))
ano_nascimento = int(input('Digite o seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
prazo = idade - 18
if idade < 18:
    falta = 18 - idade
    print('Ainda não está na hora de se alistar! Ainda faltam {} anos'.format(falta))
elif idade == 18:
    print('Está na hora de se alistar!!')
else:
    print ('Você já deveria ter se alistado há {} anos atrás!!'.format(prazo))
