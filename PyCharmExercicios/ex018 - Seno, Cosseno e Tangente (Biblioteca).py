#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de:
#seno, cosseno e tangente.

import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'Para o ângulo {ang}: \n Seno = {sen:.2f} \n Cosseno = {cos:.2f} \n Tangente = {tan:.2f}')

#math.sin(x) - Retorna o seno de x radianos - Precisa usar o modulo 'math.radians' para converter graus em radianos
#math.cos(x) - Retorna o cosseno de x radianos.
#math.tan(x) - Retorna o tangente de x radianos.