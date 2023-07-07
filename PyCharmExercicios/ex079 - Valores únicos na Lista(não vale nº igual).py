'''Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
 Caso o numero ja exista lá dentro, ele não deverá ser adicionado. No final, serão exibidos todos os
 valores únicos digitados, em ordem crescente.'''

print('\n\033[40;4m','*'*5,'NÚMEROS EM ORDEM CRESCENTE','*'*5,'\033[m')
valores = []
res = 'S'
while res == 'S':
    valor = (int(input('Digite um número: ')))
    if valor in valores:
        print('\033[32;1mValor duplicado, não vou adicioná-lo à lista.\033[m')
    else:
        valores.append(valor)
        valores.sort()
        print('\033[33;1mValor adicionado à lista.\033[m')
    res = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('-='*30,'\n')
print(f'\033[34;1mVocê digitou os valores: {valores}\033[m')
print('\n')
#--------------------------------------------SOLUÇÃO DO PROFESSOR----------------------------------------------
numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso..')
    else:
        print('Valor duplicado. Tente outro número.')
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
numeros.sort()
print(f'Você digitou os valores {numeros}.')


























