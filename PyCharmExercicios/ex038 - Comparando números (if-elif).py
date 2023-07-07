'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- o segundo valor é maior
- Não existe valor maior, os dois são iguais'''

print('\n','\033[1;33;4m','VALOR MAIOR','\033[m')
n1, n2 = input('Digite dois números inteiros: ').split(' ')
n1 = int(n1)
n2 = int(n2)
if n1 > n2:
    print(f'O primeiro valor é maior.')
elif n2 > n1:
    print(f'O segundo valor é maior.')
else:
    print(f'Não existe valor maior, os dois são iguais.')

