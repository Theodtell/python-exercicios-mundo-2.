#crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada o programa deverá perguntar se o usuário quer ou não continuar. No final mostre: A) quantas pessoas tem mais de 18 anos, B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos

maiores = 0
homens = 0
mulher_vinte = 0
while True:
    print(19 * '-')
    print('CADASTRE UMA PESSOA')
    print(19*'-')

    idade = int(input('Idade: '))
    #validação
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M]: ')).upper().strip()
    print(19*'-')
    #lógica de contagens
    # A) quantas pessoas tem mais de 18 anos
    if idade >= 18:
        maiores += 1
    # B) quantos homens foram cadastrados.
    if sexo == 'M':
        homens += 1
    # C) quantas mulheres tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulher_vinte += 1
    #validação de saída
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar cadastrando? [S/N]')).upper().strip()
    print(19*'-')
    if resp == 'N':
        break


print(f'Total de pessoas com mais de 18 anos: {maiores}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres menor de 20 anos: {mulher_vinte}')