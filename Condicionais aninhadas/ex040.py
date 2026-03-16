#Crie um programa de média, leia duas notas e calcule a sua média, mostrando uma mensagem final de acordo com a média: abaixo de 5 = reprovado; entre 05 e 6.9 recuperação; 7 ou + = aprovado

print(10*'=','\033[4;34mCALCULADORA DE NOTAS\033[m',10*'=')
aluno = str(input('Digite o nome do aluno: '))
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('\033[1;32mPARABÉNS {} VOCÊ FOI APROVADO!\033[m'.format(aluno))
elif 5 <= media <= 6.9:
    print('\033[1;33m{} Você está em RECUPERAÇÃO\033[m'.format(aluno))
else:
    print('\033[1;31m{} VOCÊ FOI REPROVADO!\033[m'.format(aluno))
