'''Escreva um programa que leia um número inteiro qualquer e peça ao usuário para escolher qual será
a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

n = int(input('Digite um número inteiro: '))
print('''Escolha a base de conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opçao = int(input('Sua opção: '))
v = '\033[31m'
f= '\033[m'
if opçao == 1:
    print(f'{n} convertido para Binário é igual a {v}{bin(n)[2:]}{f}.') #[2:] é para o resultado ignorar e excluir as 2 primeiras posições.
elif opçao == 2:
    print(f'{n} convertido para Octal é igual a {v}{oct(n)[2:]}{f}.') #[2:] é para o resultado ignorar e excluir as 2 primeiras posições.
elif opçao == 3:
    print(f'{n} convertido para Hexadecimal é igual a {v}{hex(n)[2:]}{f}') #[2:] é para o resultado excluir as 2 primeiras posições e mostrar a partir da terceira posição.
else:
    print(f'Digite uma opção válida.')