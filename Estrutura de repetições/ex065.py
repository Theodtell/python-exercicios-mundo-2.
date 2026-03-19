#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os valores e qual foi o maior e o menor dos valores lidos. O programa deve perguntar ao usuário se ele quer ou não continua digitando valores

print (20*'=','Calculadora de médias',20*'=')
contador = soma = maior = menor = 0

while True:
    valor = int(input('Informe o valor desejado: '))
    soma += valor
    contador += 1
    media = soma / contador
    #validação opção
    while True:
        opcao = input('Deseja continua? [S/N]').upper().strip()[0]
        if opcao in 'SN':
            break
        print('Não entendi o seu pedido, digite S ou N')
    if opcao == 'N':
        break
    #maior e menor
    if contador == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
print(f'Você digitou {contador} números')
print(f'O valor total dos seus valores foi: {soma}')
print(f'O maior número informado foi o {maior} e o menor {menor}')
print(f'E por fim a média de todos os números digitados foi de: {media}')