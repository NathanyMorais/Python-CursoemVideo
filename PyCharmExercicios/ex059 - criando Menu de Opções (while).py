'''Crie um programa que leia dois valores e mostre um Menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))
r = 0
while r != 5: #enquanto a resposta for diferente de 5 o laço se repete
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos números
    [5]Sair do programa''')
    r = int(input('----> Qual a sua opção? '))
    if r == 1:
        print(f'A soma entre {n1} e {n2} é \033[31;1m{n1+n2:.0f}\033[m')
    elif r == 2:
        print(f'O resultado de {n1} x {n2} é \033[32;1m{n1*n2:.0f}\033[m')
    elif r == 3:
        if n1 > n2:
            print(f'\033[33;1mO maior número digitado foi {n1}\033[m')
        else:
            print(f'\033[33;1mO maior número digitado foi {n2}\33[m')
    elif r == 4:
        print('\033[34;1mInforme os números novamente:\033[m')
        n1 = int(input('Digite o 1º valor: '))
        n2 = int(input('Digite o 2º valor: '))
    elif r == 5:
        print('\033[35;1mFinalizando...\033[m')
    else:
        print('Opção Inválida. Tente novamente')
    print('=-='*10)
    sleep(2)
print('\033[35;1mFim do Programa. Volte Sempre!\033[m')