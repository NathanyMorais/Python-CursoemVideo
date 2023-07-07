'''Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça
ao usuario para tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuario acertou ou não.'''

from random import randint
from time import sleep
print('\n','Vou pensar em um número entre 0 e 5. Tente adivinhar qual é...')
n = randint(0,5)
num = int(input('\nEm que número eu pensei? '))
sleep(2)
if num == n:
    print(f'Você acertou! Eu pensei no número {n}')
else:
    print(f'Você errou! Eu pensei no número {n}. Tente novamente!')