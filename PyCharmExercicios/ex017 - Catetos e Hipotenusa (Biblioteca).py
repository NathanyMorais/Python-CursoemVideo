#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
#calcule e mostre o comprimento da hipotenusa

import math
c1 = float(input('Comprimento do cateto oposto: '))
c2 = float(input('Comprimento do cateto adjacente: '))
print(f'O comprimento da hipotenusa é de {math.hypot(c1,c2):.2f}')

#A hipotenusa é igual à raiz quadrada da soma dos catetos ao quadrado:
# Hipotenusa = sqrt(x*x + y*y) ou (c1**2 + c2**2)**(1/2)

