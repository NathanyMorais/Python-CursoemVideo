'''Refaça o EX035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
- equilatero = todos os lados iguais
- isosceles = dois lados iguais
- escaleno = todos os lados diferentes'''
'''Ex035: Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se
 elas podem ou não formar um triângulo'''

print('\n','\033[1;31;107m-'*3,'FORMAÇÃO DE TRIÂNGULO','-'*3,'\033[m')
a = float(input('Valor da reta 1: '))
b = float(input('Valor da reta 2: '))
c = float(input('Valor da reta 3: '))
if (a < b + c and b < a + c and c < a + b): #Condição para a formação de um triangulo
    print('Os comprimentos formam um triângulo ', end = '')
    if a == b == c: #Estrutura dentro do IF de formação de triangulo para saber o tipo de triangulo que pode ser formado
        print('\033[32mEquilátero - todos os lados iguais.\033[m')
    elif a != b != c != a:
        print('\033[32mEscaleno - todos os lados diferentes.\033[m')
    elif a == b or b == c or c == a:
        print('\033[32mIsóceles - dois lados iguais.\033[m')
else:
    print('Esses comprimentos não formam triângulo.')