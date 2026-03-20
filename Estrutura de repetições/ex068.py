#faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele consquistou no final do jogo
import random

print(20*'~','JOGO PAR OU IMPAR',20*'~')
contador = 0
soma = 0
vitorias = 0

while True:
    numnero_jogador = int(input('Escolha um número: '))
    jogada_computador = random.randint(1, 10)
    soma = jogada_computador + numnero_jogador

    #limpando a escolha
    escolha_jogador =' '

    while escolha_jogador not in 'PI':
        escolha_jogador = str(input('Par ou Impar? [P/I]: ')).upper().strip()[0]
    print(f'Você jogou {numnero_jogador} e o computador jogou {jogada_computador}. O total foi {soma}', end=' ')
    print('deu par' if soma % 2 == 0 else 'deu impar')

    #analisando as jogadas e somano vitórias
    if escolha_jogador == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print ('Você PERDEU!')
            break
    elif escolha_jogador == 'I':
        if soma% 2 != 0:
            print('VOCÊ VENCEU!')
            vitorias += 1
        else:
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {vitorias} vezes')
