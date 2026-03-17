#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idades = 0
mais_velho = 0
mais_nova = 0
nome_mais_velho = ''
# ler nome, idade e sexo
for p in range(1, 5):
    nome = str(input('Informe o nome {}° da pessoa: '.format(p))).strip()
    idade = int(input('Informe a idade da {}° pessoa: '.format(p)))
    sexo = int(input('''Informe o sexo da {}° pessoa:
    [1] - Masculino;
    [2] - Feminino;
    '''.format(p)))
    if sexo not in [1, 2]:
        print('Informe um valor valido')
        break
    soma_idades = soma_idades+ idade
    # qual é o homem mais velho
    if sexo == 1:
        if mais_velho == 0 or mais_velho < idade:
            mais_velho = idade
            nome_mais_velho = nome
    # quantas mulheres tem menos de 20 anos
    if sexo == 2 and idade < 20:
            mais_nova =+ 1
if mais_velho == 0:
    print('Não há homens no grupo')
else:
    print('O homem mais velho se chama {} e tem {} anos'.format(nome_mais_velho,mais_velho))
#caclular e mostrar: media de idade do grupo
media = soma_idades / 4
print('A idade média de todos é de {} '.format(media))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mais_nova))





