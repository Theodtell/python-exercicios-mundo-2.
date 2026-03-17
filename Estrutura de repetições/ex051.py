#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = primeiro_termo + (10 - 1) * razao

for c in range(primeiro_termo, decimo + razao,razao):
    print(c, end=' -> ')

print('Fim')
