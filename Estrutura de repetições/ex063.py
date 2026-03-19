#escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos da sequencia de fibonacci. Exemplo 0-1-1-2-3-5-8

print(20*'=-')
print('SEQUENCIA FIBONACCI')
n = int(input('Quantos termos você quer mostrar? '))
#termos fixos da sequencia fibonacci
t1 = 0
t2 = 1
print ('~'*30)
print(f'{t1} -> {t2}', end='')
#iniciando o contador pq t1 e t2 são fixos
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f'-> {t3}', end='')
    #transição de valores 
    t1 = t2
    t2 = t3
    cont += 1
print('-> FIM')
