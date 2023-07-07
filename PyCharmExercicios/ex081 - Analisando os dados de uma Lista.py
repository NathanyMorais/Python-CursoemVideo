'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
a)Quantos numeros foram digitados
B)A lista ordenada de forma descrescente
c)Se o valor 5 foi digitado e está ou não na lista'''

lista =[]
res = ' '
while res not in 'N':
    n = int(input('Digite um valor: '))
    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    lista.append(n)
    lista.sort(reverse=True)
print('-'*40)
print(f'\033[33mVocê digitou \033[1;4m{len(lista)}\033[m \033[33mnúmeros no total.\033[m')
print(f'\033[32mOs valores digitados em ordem decrescente foram: \033[4;1m{lista}\033[m')
for i, v in enumerate(lista):
    if 5 in lista:
        if v == 5:
                print(f'\033[35mO número 5 foi digitado e está na \033[4;1m{i+1}ª posição\033[m \033[35mda lista.\033[m')
    else:
        print('\033[34mO número \033[4;1m5 não foi digitado\033[m\033[34m e por isso não aparece na lista.\033[m')
        break
print('-'*40,'\n')
#-----------------------SOLUÇÃO DO PROFESSOR---------------------------------------------------------------------------
valores = []
while True:
    valores.append(int(input('Digite o valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}.')
if 5 in valores:
    print(f'O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')












