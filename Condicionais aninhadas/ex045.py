#Crie um programa que faça o computador jogar jokenpô com você
import random

print(10*'=','\033[1;32mBEM VINDO AO JOKENPÔ\033[m',10*'=')

#1 - pedra; 2 - papel; 3 - tesoura
jogadas = ['Pedra', 'Papel', 'Tesoura']
opcao_jogador = int(input('''Escola a sua jogada:
[0]- pedra
[1]-papel
[2]-tesoura
'''))

#validação do comando

if opcao_jogador not in [0, 1, 2]:
    print('Não entendi o seu comando, tente novamente!')
else:
    opcao_pc = random.randint(0,2)

    print(f'O jogador {jogadas[opcao_jogador]}!')
    print(f'O computador escolheu {jogadas[opcao_pc]}!')

#empate

if opcao_pc == opcao_jogador:
    print('Mesma jogada para ambos, empate!')

#Jogador vence
elif opcao_jogador == 1 and opcao_pc == 3 or opcao_jogador == 2 and opcao_pc == 1 or opcao_jogador == 3 and opcao_pc == 2:
    print('\033[1;32mPARABÉNS VOCÊ VENCEU!\033[m')

#Computador vence
else:
    print('Ponto para a máquina!')





