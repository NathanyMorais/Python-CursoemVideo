'''Faça um programa que leia tres numeros inteiros e mostre qual é o maior e qual é o menor'''

print('\n','-'*5,'MAIOR E MENOR','-'*5)
print('Digite 3 números inteiros:')
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
lista = [n1, n2, n3]
if n1==n2 or n2==n3 or n3==n1:
    print('Digite números diferentes')
else:
    print(f'O maior número digitado foi: {max(lista)}')
    print(f'O menor número digitado foi: {min(lista)}')

#Outra resolução para o exercício:
'''n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
elif n3>n1 and n3>n2:
    maior = n3
print(f'O maior número é {maior}.')
menor = n1
if n2<n1 and n2<n3:
    menor = n2
elif n3<n1 and n3<n2:
    menor = n3
print(f'O menor número é {menor}.')'''

