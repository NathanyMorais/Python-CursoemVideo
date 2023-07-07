'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves'''

dados = [] #lista temporária vazia
pessoas = [] #lista principal vazia
maior = menor = 0
while True: #laço infinito para cadastrar quantas pessoas desejar
    dados.append(str(input('Nome: '))) #cadastra nome e armazena na lista temporária 'dados'
    dados.append(float(input('Peso: '))) #cadastra peso e armazena na lista temporária 'dados'
    if len(pessoas) == 0: #se o comprimento da lista principal pessoas for igual a zero, ou seja, ninguem foi cadastrado ainda
        maior = menor = dados[1] #então o peso cadastrado será o maior e o menor (o peso está na posição 1 da lista dados)
    else: #depois que forem cadastrados, será comparado o maior e o menor pesos
        if dados[1] > maior: #comparando o Maior peso
            maior = dados[1]
        if dados[1] < menor: #comparando o Menor peso
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = str(input('Deseja continuar? [S/N] '))
    if r in 'Nn': #se usuario digitar 'nN' o programa para de cadastrar
        break
print('-='*40)
print(f'Foram cadastradas {len(pessoas)} pessoas.') #len() mostra o comprimento da lista = quantidade de pessoas cadastradas
print(f'O maior peso foi de {maior}Kg. Referente à ', end='')
for p in pessoas: #para pessoa na lista 'pessoas'
    if p[1] == maior: #se p[1] que se refere ao PESO, for o maior
        print(f'[{p[0]}]',end=' ') #imprime o p[0] que se refere ao NOME
print()
print(f'O menor peso foi de {menor}kg. Referente à ', end='')
for p in pessoas:
    if p[1] == menor: #se o p[1] que se refere ao PESO, for o menor
        print(f'[{p[0]}]',end=' ') #imprime o p[0] que se refere ao NOME
print()
