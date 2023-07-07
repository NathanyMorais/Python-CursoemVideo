'''Crie um programa que leia vários números inteiros pelo teclado. O programa deve perguntar
ao usuario se ele quer ou não Continuar a digitar valores. No final da execução, mostre a
MEDIA ENTRE TODOS os valores e qual foi o Maior e o Menor valores lidos.'''

r = 'S'
lista = [] #variavel lista vazia
soma = cont = 0 #variáveis soma e cont recebendo o valor Zero
while r == 'S': #enquanto a resposta for 'sim'
    n = int(input('Digite um valor: '))
    lista.append(n) #função .append() para armazenar os números digitados dentro da lista
    soma = soma + n #acumulador para somar os números digitados
    cont += 1 #contador para contar quantos numeros foram digitados
    r = str(input('Deseja continuar? [S/N] ')).upper().strip()[0] #[0] vai considerar apenas a posição da primeira letra (para validar S ou N caso digitem 'sim ou nao')
print(f'Você digitou {cont} números e a média foi \033[33;1;4m{soma/cont:.2f}\033[m')
print(f'O maior valor foi \033[34;4m{max(lista)}\033[m e o menor foi \033[32;4m{min(lista)}\033[m.')
#---------------------SOLUÇÃO DO PROFESSOR------------------------------------------------------------------------------
p = 's'
soma = cont = maior = menor = 0
while p == 's':
    n = int(input('Digite um número: '))
    p = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    soma += n
    cont += 1
    if cont == 1: #se o contador for igual a 1
        maior = menor = n #o número digitado é o maior e também é o menor
    else: #a partir de outros valores digitados, tem-se a comparação:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print(f'A média entre os números digitados foi {soma/cont:.2f}')
print(f'O maior foi {maior} e o menor foi {menor}.')
