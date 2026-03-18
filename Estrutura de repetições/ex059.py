#programa de menu interativo utilizando while
from time import sleep
# Controla a execução do menu até o usuário optar por sair
print(10*'=','Menu com while',10*'=')
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
sair = False
# Exibe as opções disponíveis para o usuário
while not sair:
    # Garante que a opção esteja dentro do intervalo válido do menu
    while True:
        try:
            opcao = int(input('''
[1] somar;
[2] multiplicar;
[3] maior;
[4] Novos números
[5] sair do programa
'''))
            if opcao in [1,2,3,4,5]:
                break
            else:
                print('Não reconheci o seu pedido, tente novamente.')
        except:
            print('Entrada inválida, digite apenas números')
# Executa a operação escolhida com base na opção selecionada
    if opcao == 1:
        soma = valor1 + valor2
        print('-=' * 30)
        print('{} + {} = {}'.format(valor1, valor2, soma))
        print('-='*30)
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('-=' * 30)
        print('{} X {} = {}'.format(valor1, valor2, multiplicacao))
        print('-=' * 30)
    elif opcao == 3:
        if valor1 > valor2:
            print('-=' * 30)
            print ('O maior valor é {}'.format(valor1))
            print('-=' * 30)
        elif valor1 < valor2:
            print('-=' * 30)
            print('O maior valor é {}'.format(valor2))
            print('-=' * 30)
        else:
            print('-=' * 30)
            print ('Os dois números são iguais')
            print('-=' * 30)
    elif opcao == 4:
        print('-=' * 30)
        valor1 = int(input('Digite um novo valor: '))
        valor2 = int(input('Digite o segundo novo valor: '))
        print('-=' * 30)
    elif opcao == 5:
        sair = True
        print('-=' * 30)
        print('Encerrando o programa...')
    sleep(2)
print('Até a próxima')