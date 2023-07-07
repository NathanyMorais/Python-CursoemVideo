'''Desenvolva um programa que leia 6 números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o'''


print('\n','\033[34;4m','*'*5,'SOMA DOS PARES','*'*5,'\033[m')
s = 0 #acumulador - acumula os números e soma
cont = 0 #contador - conta a quantidade de números no intervalo
for c in range(1,6+1):
    n = int(input(f'Digite o {c} valor: '))
    if n % 2 == 0:
        s = s + n
        cont = cont + 1
print(f'Você informou {cont} números PARES e a soma entre eles é {s}.')

