'''Faça um programa que leia 5 valores numericos e guarde em uma lista. No final, mostre qual foi
 o MAIOR e o MENOR digitado e suas respectivas POSIÇÕES na lista'''

valores = [] #variavel lista vazia
maior = menor = 0 #variaveis maior e menor valendo zero
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0: #analisa o valor na posição 0
        maior = menor = valores[c] #coloca o valor da posição 0 como sendo o maior e o menor
    else: #analisa os valores nas outras posições
        if valores[c] > maior: #se na posiçao 1 o valor for maior que o valor na posiçao 0
            maior = valores[c] #o maior valor será entao o da posição 1...e assim vale para as outras posições até achar o maior
        if valores[c] < menor: #se na posiçao 1 ( e depois 2,3,4) o nº for menor que o valor na posiçao 0 (e depois 1,2,3..)
            menor = valores[c] #o menor valor será entao o da posição 1...e assim vale para as outras posições até achar o menor
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores): #Para índice e valores na lista 'valores'
    if v == maior: #se o valor for o maior da lista
        print(f'{i}..', end='') #imprima a posição i desse valor
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor: #se o valor for o menor da lista
        print(f'{i}..', end='') #imprima a posição i que esse valor está