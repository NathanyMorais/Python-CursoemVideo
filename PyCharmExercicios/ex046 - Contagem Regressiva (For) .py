'''Faça um programa que mostre na tela uma contagem regressiva indo de 10 até 0,
com pausa de 1 segundo entre eles'''

print('\n','\033[33;1m','*'*5,'CONTAGEM REGRESSIVA','*'*5,'\033[m')
from time import sleep
for c in range(10,-1,-1): #Faz a contagem regressiva de 10 até 0
    print((c), end=' ')
    sleep(1)
print('\033[31;1mBOOOOM!!!\n\033[m')
















