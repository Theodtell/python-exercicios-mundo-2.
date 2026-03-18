# programa para ler um número e mostrar o seu fatorial
from math import factorial
from time import sleep

print(10*'=-','Calculadora de fatorial',10*'=-')
#validação de número inicial
while True:
    try:
        numero = int(input('Informe um número para calcular o seu fatorial: '))
        if numero >= 0:
            break
        else:
            print('Digite um número inteiro positivo.')
    except:
        print('Entrada inválida, digite um número inteiro')
sair = False
while not sair:
    fatorial = factorial(numero)
    print ('Fatorial de {} = {}'.format(numero, fatorial))
    # Validação da opção
    while True:
        opcao = input('Deseja caclular mais um número? ').strip().upper()[0]
        if opcao in ['S', 'N']:
            break
        else:
            print('Opção inválida, digite apenas S ou N.')
    if opcao == 'N':
        sair = True
    else:
        #validação do próximo número
        while True:
            try:
                numero = int(input('Informe um número para calcular o seu fatorial: '))
                if numero >= 0:
                    break
                else:
                    print('Digite um número inteiro positivo.')
            except:
                print('Entrada inválida, digite um número inteiro')
print('Programa encerrando...')
sleep(1)
print('Programa finalizado com sucesso...')