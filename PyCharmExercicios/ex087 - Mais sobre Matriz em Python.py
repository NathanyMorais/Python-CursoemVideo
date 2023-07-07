'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = []
pares = 0
soma = 0
for l in range(0,3): #para cada linha nas posições de 0 ate 2
    linha = [] #lista linha vazia que vai receber cada linha de números digitados
    for c in range(0,3): #para cada coluna nas posições de 0 ate 2
        linha.append(int(input(f'Digite o valor para {[l,c]}: '))) #usuario vai digitar os numeros para cada linha e coluna
    matriz.append(linha[:]) #no final do loop as 3 listas 'linha' vão ser armazenadas na lista 'matriz'
for l in range(0,3): #para cada linha nas posições de 0 até 2
    print(matriz[l]) #imprime no formato de matriz = 3 linhas com 3 colunas uma embaixo da outra
print('-='*40)
for l in range(0,3): #laço para percorrer cada linha e coluna novamente
    for c in range(3):
        if matriz[l][c] % 2 == 0: #se o número que estiver na linha e coluna testada for par
            pares = pares + matriz[l][c]  # entra na soma dos pares
        if c == 2: #se estiver testando a coluna na posição 2, ou seja, a terceira coluna
            soma = soma + matriz[l][2] #os números que estiverem nessa coluna serão somados
        if l == 1: #se estiver testando a linha na posição 1, ou seja, a segunda linha da matriz
            if c == 0: #se coluna na posição 0, ou seja, é a primeira coluna
                maior = matriz[1][c] #então o número que estiver na linha 1, coluna 0 será o maior
            elif matriz[1][c] > maior: #testando os números nas próximas colunas e comparando qual é o maior deles
                maior = matriz[1][c]
print(f'A soma dos valores pares digitados é {pares}.') #imprime a soma dos pares
print(f'A soma dos valores da terceira coluna é {soma}.')
print(f'O maior valor da segunda linha é {maior}.')
print('-='*40)
#-----OUTRA MANEIRA DE VERIFICAR OS VALORES PARES----------------------------------------------------------------------
'''for linha in matriz: #para cada linha da matriz
    for valor in linha: #analisando o valor em cada linha
        if valor % 2 == 0: #se o valor for par
            pares = pares + valor #soma apenas os valores pares'''
#-------------------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------
matriz = [[0,0,0], [0,0,0], [0,0,0]]
par = maior = soma = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para [{l},{c}]: '))
print('*'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0: #se o valor exibido na tela for par, entra na soma dos valores pares
            par = par + matriz[l][c]
    print()
print('*'*30)
print(f'A soma dos valores pares é: {par}')
for l in range(0,3): #estrutura para percorrer apenas as linhas da matriz, pois a coluna tem posição fixa
    soma = soma + matriz[l][2] # no caso, soma os números que estão na posição [2] que se refere a terceira coluna
print(f'A soma dos valores da terceira coluna é: {soma}')
for c in range(0,3): #estrutura para percorrer apenas as colunas da matriz, pois a linha tem posição fixa
    if c == 0:
        maior = matriz[1][c]
    elif matriz [1][c] > maior:
        maior = matriz[1][c]
print(f'O maior número da segunda linha é {maior}')
































