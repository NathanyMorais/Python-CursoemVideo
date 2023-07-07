'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma Tupla.
Em seguida mostre a listagem de números gerados e também indique o menor e o maior valor.'''
import random
tupla = [] #nesse caso NÃO é tupla e sim uma lista, já que é entre []
for c in range(1,6):
    n = random.randint(1, 50)
    tupla.append(n)
print(f'A tupla formada foi: \033[34;1m{tupla}\033[m')
sorted(tupla)
print(f'O MAIOR valor foi \033[33;1m{max(tupla)}\033[m e o MENOR valor foi \033[32;1m{min(tupla)}\033[m.')
print(f'*'*50,'\n')
#-------------------------SOLUÇÃO DO PROFESSOR USANDO TUPLA--------------------------------------------------------------------------
tupla = (random.randint(1,10),random.randint(1,10),random.randint(1,10),
     random.randint(1,10),random.randint(1,10)) #vai sortear 5 valores e armazenar na tupla
print(f'Eu sorteei os valores: {tupla}')
print(f'O maior valor sorteado foi {max(tupla)}.')
print(f'O menor valor sorteado foi {min(tupla)}.')