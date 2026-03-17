"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto."""

sexo = str(input('Informe seu sexo: [F/M] ')).strip().upper()[0] #[0] pega apenas a primeira letra

while sexo not in 'FM':
    sexo = str(input('Dados inválidos, por favor informe novamente: ')).strip().upper()[0]
if sexo == 'F':
    sexo = 'Feminino'
else:
    sexo = 'Masculino'
print('Sexo {} registrado com sucesso!'.format(sexo))