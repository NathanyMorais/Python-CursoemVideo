#Crie um programa que leia um número real qualquer e mostre na tela sua porção inteira.
#Por exemplo: digite um número - 6.127. O número 6.127 tem a parte inteira 6.

from math import trunc
n = float(input('Digite um número: '))
print(f'O número {n} tem a parte inteira {trunc(n)}')

#É possível resolver o exercício sem importar a Biblioteca Math:
'''n = float(input('Digite um número: '))
print(f'O número digitado foi {n} e sua porção inteira é {int(n)}.')'''