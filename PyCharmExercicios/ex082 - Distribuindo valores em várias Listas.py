'''Crie um programa que vai ler vários numeros e colocar em uma lista. Depois, crie duas listas extras que
vão conter apenas os valores pares e os valores impares digitados, respectivamente. Ao final, mostre
o conteudo das 3 listas geradas'''

lista = list()
impar = list()
par = list()
while True:
    num = (int(input('Digite um valor: ')))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('-='*50)
print(f'A lista completa de numeros digitados é {lista}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {impar}.')
print('-='*50,'\n')

#----------------------------------SOLUÇÃO DO PROFESSOR---------------------------------------------------------
lista = []
impar = []
par = []
while True:
    lista.append(int(input('Digite um valor: ')))
    res = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if res in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa de numeros digitados é {lista}.')
print(f'A lista de pares é {par}.')
print(f'A lista de ímpares é {impar}.')

