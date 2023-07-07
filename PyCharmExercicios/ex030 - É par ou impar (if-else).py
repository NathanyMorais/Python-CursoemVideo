'''Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é par ou impar'''

print('\n','-'*5,'PAR OU ÍMPAR','-'*5)
num = int(input('Digite um número inteiro: '))
if num % 2 == 0:
    print(f'O número {num} é par!')
else:
    print(f'O número {num} é ímpar!')