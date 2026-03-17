#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
import time

print(10*'-','CONTAGEM REGRESSIVA',10*'-')

cont = 10

for c in range (0,11):
    print(cont)
    cont -= 1
    time.sleep(1)
print(10*'*','FOGOS ESTOURANDO!!',10*'*')
