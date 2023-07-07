# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
# Exercício com configuração de cores no terminal:

n = int(input('Digite um número inteiro: '))
print(f'\033[36m','_'*15,'\033[m')
print(f' {n} x 1 = {n*1}\n {n} x 2 = {n*2}\n {n} x 3 = {n*3}\n {n} x 4 = {n*4}\n {n} x 5 = {n*5}')
print(f' {n} x 6 = {n*6}\n {n} x 7 = {n*7}\n {n} x 8 = {n*8}\n {n} x 9 = {n*9}\n {n} x 10 = {n*10}')
print(f'\033[36m','_'*15,'\033[m')