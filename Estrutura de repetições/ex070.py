#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre: A) qual é o total gasto na compra, B) quantos produtos custammais de R$ 1.000,00 C) qual é o nome do produto mais barato

print(20*'-')
print('LOJA SUPER BARATÃO')
print(20*'-')

gasto_total = 0
produto_barato = ' '
menor_preco = 0
cont_mil = 0
total_produtos = 0

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    total_produtos += 1
    #A- Qual é o total gasto na compra
    gasto_total += preco

    #B- Quantos produtos custammais de R$ 1.000,00
    if preco > 1000:
        cont_mil += 1

    #C- Qual é o nome do produto mais barato
    if total_produtos == 1:
        produto_barato = produto
        menor_preco = preco
    else:
        if preco < menor_preco:
            menor_preco = preco
            produto_barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'O total da compra foi de R$ {gasto_total:.2f}')
print(f'Temos {cont_mil} produtos custando mais de R$ 1.000,00')
print(f'O produto mais barato foi {produto_barato} que custa R$ {menor_preco}')
