# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo será negado

print(10*'=','\033[1;32mSIMULADOR DE EMPRESTIMOS',10*'=\033[m')

valor = float(input('Qual é o valor da casa em R$? '))
tempo = int(input('Em quantos anos você pretende quitar a casa? '))
salario = float(input('Informe agora o seu rendimento mensal: '))

meses = tempo * 12
parcela = valor / meses
percentual = salario * 0.30

#Confere se o valor não ultrapassa 30%

if parcela <= percentual:
    print ('\033[1;32mParabéns seu emprestimo foi aprovado!\033[m')
    print ('O valor da sua parcela será de {:.2f} por {} mês durante {} anos'. format (parcela,meses,tempo))
elif parcela > percentual:
    print('\033[1;31mEmprestimo reprovado!\033[m')
    print ('A parcela é superior a 30% do seu rendimento mensal.')