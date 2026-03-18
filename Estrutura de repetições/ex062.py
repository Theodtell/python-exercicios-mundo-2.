#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print(10*'=-', 'CALCULADORA DE PA 3.0',10*'=-')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
mais = 10
total = 0
while mais != 0:
    contador = 0
    total += mais
    while contador < mais:
        print('{} -> '.format(termo), end='')
        termo += razao
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Progressão finalizada com {} termos mostrados.'.format(total))