'''A confederação nacional de natação precisa de um programa que lei o ano de nascimento de uma atleta e mostre a sua categoria de acordo com a idade:
até 9 - mirim
até 14 - infantil
ate 19 - junior
até 20 - sênior
Acima - master
'''

from datetime import date

anoatual = date.today().year

print(10*'=','CATEGORIAS',10*'=')

ano = int(input('Digite o ano de nascimento:'))
idade = anoatual - ano

if idade <= 9:
    print('Categoria: MIRIM')
elif 9 < idade <= 14:
    print('Categoria: INFANTIL')
elif 14 < idade <= 19:
    print('Categoria: JUNIOR')
elif 19 < idade <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')