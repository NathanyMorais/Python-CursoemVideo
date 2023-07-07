'''Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

print('\n','-'*3,'\033[32mAPENAS OS PARES\033[m','-'*3)
for c in range(1,51): #Percorre tode o laço no intervalo de 1 até 50, ou seja, percorre o laço 50 vezes
    if c % 2 == 0: #condição para considerar apenas os números pares
        print(c, end="-")
print('FIM\n')

#Outra resolução usando menos memório devido a menor quantidade de interações (percorre o laço menos vezes):
for c in range(2, 51, 2): #percorre o laço no intervalo de 2 até 50 - pulando de 2 em 2 - percorre o laço 25 vezes
    print(c, end='-')
print('FIM\n')