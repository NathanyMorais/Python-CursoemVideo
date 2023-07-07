#O professor quer sortear a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome de 4 alunos e mostre a ordem sorteada.

import random
from typing import Tuple

print('-'*5, 'Ordem de Apresentação dos Trabalhos', '-'*5)
n1 = (input('Aluno 1: '))
n2 = (input('Aluno 2: '))
n3 = (input('Aluno 3: '))
n4 = (input('Aluno 4: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #Random = aleatorio / Shuffle = embaralhar
print(f'Ordem de Apresentação: \n {lista}')