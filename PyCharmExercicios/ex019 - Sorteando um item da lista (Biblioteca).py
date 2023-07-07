#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que o ajude lendo o nome deles e escrevendo o nome escolhido.

import random
print('-'*5,'Sorteio de Alunos','-'*5)
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4] #Lista precisa ficar entre colchetes
sorteio = random.choice(lista)
print(f'O aluno sorteado foi: {sorteio}')