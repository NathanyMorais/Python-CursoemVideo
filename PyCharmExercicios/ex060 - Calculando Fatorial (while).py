'''Faça um programa que leia um numero qualquer e mostre o seu fatorial.
Ex: 5!= 5x4x3x2x1 = 120'''

print('\n','\033[32;4;1m','-'*5,'FATORIAL!','-'*5,'\033[m')
n = int(input('Digite um número para calcular seu fatorial: '))
print(f'{n} x', end=' ') #para que o primeiro número digitado seja impresso na tela
res = 1
while n > 1: #enquanto o número n for maior que 1:
    res = res * n  #faz a multiplicação entre os números do fatorial
    n = n - 1 #número n é igual ao número - 1 = para 'percorrer' o fatorial em ordem decrescente Ex: 5! = 5x4x3x2x1
    print(f'{n}', end=' ')
    print('x ' if n > 1 else '=', end='') #imprima 'x' na frente do número{n} se ele for maior que 1, se não imprima o sinal de '='.
print(f' {res}') #imprime o resultado final da multiplicação dos números

