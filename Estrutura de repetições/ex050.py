#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

cont = 0
soma = 0

for c in range (1,7):
    numero = int(input(('Digite o {}° valor: '.format(c))))
    if numero % 2 == 0:
        soma += numero
        cont += 1
print ('Você digitou {} numeros pares a soma é de {}'.format(cont, soma))


