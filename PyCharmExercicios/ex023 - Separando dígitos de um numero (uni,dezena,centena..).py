'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
Ex: Digite um numero -  1834
Unidade: 4  Dezena: 3  Centena: 8 Milhar: 1'''

num = int((input('Digite um número de 0 a 9999: ')))
print(f'Analisando o número {num}: ')
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'Unidade = {uni}')
print(f'Dezena = {dez}')
print(f'Centena = {cen}')
print(f'Milhar = {mil}')









