'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1       b) de 10 até 0, de 2 em 2      c) uma contagem personalizada'''

from time import sleep

def contador(i, f, p):
    if p < 0: #se o passo for menor que zero, ou seja, se for negativo
        p = p * -1 #transforma o passo em positivo
    if p == 0: #se o passo for igual a zero (que não existe pois não é possível contar de 0 em 0)
        p = 1 #transforma o passo em 1
    print('=-' * 20)
    sleep(0.5)
    print(f'Contagem de {i} até {f}, de {p} em {p}') #contagem de 'inicio' até 'fim', de 'passo' em 'passo'
    sleep(0.5)
    if i < f: #se o início for maior do que o fim
        cont = i #contador iniciando no inicio
        while cont <= f: #enquanto o contador for menor que o fim
            print(f'{cont} ', end='')
            cont += p #soma contador + passo
            sleep(0.5)
        print('FIM!')
    else: #se o fim for maior do que o início
        cont = i #contador inicia no inicio
        while cont >= f: #enquanto o contador for maior que o fim
            print(F'{cont} ', end='')
            cont -= p #subtrai contador - passo (para fazer contagem regressiva)
            sleep(0.5)
        print('FIM!')

#Código principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-'*40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)











