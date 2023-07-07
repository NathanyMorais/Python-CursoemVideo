'''Faça um programa que leia um número inteiro e diga se ele é ou não número Primo'''

print('\n','\033[35;1;4m','SERÁ QUE É PRIMO?\033[m')
n = int(input('Digite um número qualquer: '))
cont = 0 #contador usado para contar a quantidade de números divisíveis
for c in range(1,n+1): #laço percorre intervalo de 1 até o número que o usuário digitar
    if n % c == 0: #condição para saber quais números são divisíveis dentro do intervalo
        print('\033[34;1m', end=' ') #Os números que forem divisíveis vão ficar na cor azul
        cont = cont + 1  #contador para contar quantidade de números divisíveis
    else:
        print('\033[33m', end=' ') #Os números que NÃO forem divisiveis vão ficar amarelos
    print(c, end=' ')
print(f'\n\033[mO número {n} foi divisível {cont} vezes')
if cont == 2: #Se a quantidade de divisíveis for igual a 2, o numero é primo (dividido por 1 e por ele mesmo)
    print(f'Logo, o número {n} é \033[1;31;4mPRIMO\033[m!')
else:
    print(f'Logo, o número {n} \033[1;31;4mNÃO É PRIMO\033[m!')
print('\nFIM\n')

#------------------------------RESOLUÇÃO MAIS SIMPLES E DIRETA:-----------------
'''n = int(input('Digite um número: '))
cont = 0
for c in range(1,n+1): #mostra intervalo de 1 até o número digitado pelo usuario
    if n % c == 0: #se n dividido por c for igual a 0 (mostra os números que são divisíveis)
        print(c, end=' ')
        cont = cont + 1 #contador que conta a quantidade de números divisíveis
if cont == 2: #para ser primo o número só pode ser divisível por 2 números - por 1 e por ele mesmo
    print('\nÉ número Primo')'''