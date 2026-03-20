#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado foi negativo

print (20*'~', 'TABUADA',20*'~')

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    else:
        for c in range(1, 11):
            print(f'{n} X {c} = {n*c}')
print ('TABUADA ENCERRADA')