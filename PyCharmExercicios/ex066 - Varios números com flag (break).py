'''Crie um programa que leia vários números inteiros. O programa só vai parar quando o usuário digitar o valor 999.
No final, mostre quantos números foram digitados e qual é a soma entre eles (desconsiderando o flag=999)'''

soma = cont = 0
while True: #loop infinito
    n = int(input('Digite um valor ou 999 para parar: '))
    if n == 999: #condição de parada
        break #comando para interromper o loop infinito
    soma += n #acumulador para somar os numeros digitados
    cont += 1 #contador para contar quantos números foram digitados
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
