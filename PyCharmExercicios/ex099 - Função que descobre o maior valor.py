'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
interops. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''
from time import sleep
maior = 0
def maior(* valor): #quando não se sabe a quantidade certa de parametros, usa-se o '*'.
    cont = maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    tot = len(valor) #informa o total de números dentro do parâmtro 'valor'
    for num in valor: #para cada número dentro de 'valor'
        print(f'{num} ', end='') #imprime o numero
        sleep(0.5)
        if cont == 0: #se o contado for igual a zero, ou seja, está no inicio da contagem
            maior = num #o maior número vai ser o primeiro que aparecer
        else: #se o contador não for zero, vamos analisar os outros numeros
            if num > maior: #se o número seguinte for maior do que o maior
                maior = num #o maior será esse novo número analisado
        cont += 1
    print(f'-> Foram informados {tot} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')
    #print(f'O maior valor informado foi {max(valor)}.') # O comando 'max()' dá erro quando não é passado nenhum
                                                         # parâmetro para a função maior. Ex: maior()

#Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 8, 0)
maior(1, 2)
maior(6)
maior()