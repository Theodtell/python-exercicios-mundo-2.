"""Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer."""
import random

print(20*'*','JOGO DA ADVINHAÇÃO',20*'*')
# gerador de número aleatório
n = random.randint(1,10)
contador = 1
#pede a primeira tentativa
print('Olá! Sou o seu computador e acabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar?!')
tentativa = int(input('Qual é o seu palpite? '))
while tentativa != n:
    #Validação
    while tentativa < 0 or tentativa > 10:
        tentativa = int(input('Opa, o palpie é entre 0 e 10, tente novamente: '))
    #lógica do jogo
    if tentativa < n:
        print ('Não foi dessa vez... tente um número MAIOR')
    else:
        print ('Não foi dessa vez... tente um número MENOR')
    #nova tentativa
    tentativa = int(input('Qual é o seu palpite? '))
    contador += 1
print('PARABENS VOCÊ VENCEU!')
print('Você usou um total de {} tentativas'.format(contador))



