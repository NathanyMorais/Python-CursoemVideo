'''Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla.
Em seguida, mostre:
a) Quantas vezes apareceu numero 9
b) Em que posição foi digitado o primeiro valor 3
c) Quantos foram os numeros pares'''

par = 0
tupla = [] #nesse caso NÃO é tupla e sim uma LISTA, já que é entre []
for c in range(1,5):
    num = int(input('Digite um valor: '))
    tupla.append(num)
    if num % 2 == 0:
        par += 1
print(f'Você digitou os números:\033[31m {tupla}\033[m')
print(f'Valor 9 apareceu \033[1;4m{tupla.count(9)} vezes\033[m.')
if tupla.count(3) > 0:
    print(f'Valor 3 apareceu pela primeira vez na \033[4;1mposição {tupla.index(3)+1}\033[m.')#[+1] para mostrar a posição correta do nº, visto que a contagem da tupla se inicia no 0
else:
    print(f'Valor 3 \033[4mnão\033[m apareceu em nenhuma posição.')
if par > 0:
    print(f'Nessa tupla existem \033[4;1m{par} números pares\033[m.')
else:
    print(f'Não existem números pares nessa tupla.')
print('*'*50,'\n')
#--------------------------SOLUÇÃO DO PROFESSOR USANDO TUPLA-------------------------------------------------------------------------
tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')),
         int(input('Digite o último valor: ')))
print(f'Você digitou os números: {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu {tupla.index(3)+1}ª posição')
else:
    print(f'O número 3 não apareceu.')
print(f'Os valores pares digitados foram', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')