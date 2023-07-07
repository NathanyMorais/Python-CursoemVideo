'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de 3 e que
se encontram no intervalo de 1 até 500'''

print('\n','\033[33;1m','-'*3,'APENAS ÍMPARES MÚLTIPLOS DE 3','-'*3,'\033[m')
soma = 0 #acumulador para fazer a soma entre os números ímpares multiplos de 3.(Acumula os valores e faz a soma entre eles)
cont = 0 #contador para fazer a contagem de números impares multiplos de 3 - ou seja, quantidade de números que existem nesse intervalo
for c in range(1,501):
    if c % 2 != 0 and c % 3 == 0: #condição para números ímpares e multiplos de 3
       print(c, end=' ')
       soma = soma + c
       cont = cont + 1
print('FIM')
print(f'Total de números ímpares e múltiplos de 3 no intervalo de 1 a 500 = \033[32;1m{cont}\033[m números')
print(F'A soma de todos os números ímpares que são múltiplos de 3 é \033[31;1m{soma}\033[m')
print('\n')

#Outra maneira de resolver usando menos memória por percorrer o laço menos vezes:
soma = 0
for c in range(3,501,6): #percorre o laço de 3 ate 500, pulando de 6 em 6
    print(c, end='-')
    soma = soma + c
print('FIM')
print(F'A soma de todos os números ímpares que são múltiplos de 3 é {soma}')
