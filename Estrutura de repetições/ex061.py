#Progressão aritimética usando while

sair = False
print(10*'=-', 'CALCULADORA DE PA 2.0',10*'=-')
print(31*'=-')
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
decimo = primeiro_termo + (10 - 1) * razao
#mostrando a PA
while not sair:
    for c in range (primeiro_termo, decimo + razao, razao):
        print(c, end=' -> ')
    print ('FIM')
    while True:
        opcao = input('Você deseja tentar outro número? [S/N] ').upper()[0].strip()
        if opcao in ['S','N']:
            break
        else:
            print('Opção inválida')
    #decisão
    if opcao == 'N':
        sair = True
    else:
        primeiro_termo = int(input('Digite o primeiro termo: '))
        razao = int(input('Digite a razao: '))
        decimo = primeiro_termo + (10 - 1) * razao
print('Encerrando...')
print('Programa finalizado com sucesso, tenha um bom dia!')