'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

numeros = []
par = []
impar = []
for c in range(1,8): #faixa de 7 valores para o usuario digitar
    n = int(input(f'Digite o {c}º número: '))
    if n % 2 == 0: #se o valor digitado for par
        par.append(n) #adiciona na lista par
    else: #se o valor for impar
        impar.append(n) #adiciona na lista impar
numeros.append(par[:]) #adiciona uma cópia da lista par na lista composta 'numeros'
numeros.append(impar[:]) #adiciona uma cópia da lista impar na lista composta 'numeros'
par.sort() #coloca a lista par em ordem crescente
impar.sort() #coloca a lista impar em ordem crescente
print(f'Você digitou os números pares e ímpares: {numeros}.')
print(f'Os valores pares em ordem crescente foram: {par}.')
print(f'Os valores ímpares em ordem crescente foram: {impar}.')

#------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------------------------
num = [[], []] #lista composta principal com 2 listas dentro, todas vazias
valor = 0
for c in range(1,8):
    valor = int(input(f'Digite um {c}º valor: '))
    if valor % 2 == 0: #se o valor digitado for par
        num[0].append(valor) #o valor digitado vai ser adicionado na lista principal 'NUM' na posição 0 (onde esta o primeiro colchete)
    else: #se o valor digitado for impar
        num[1].append(valor) #o valor digitado vai ser adicionado na lista principal 'NUM' na posição 1 (onde esta o segundo colchete)
print(f'Todos os valores: {num}')
num[0].sort() #coloca a lista par em ordem crescente
num[1].sort() #coloca a lista impar em ordem crescente
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
