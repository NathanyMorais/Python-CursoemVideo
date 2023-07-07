'''Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se
 elas podem ou não formar um triângulo'''

print('\n','-'*3,'FORMAÇÃO DE TRIÂNGULO','-'*3)
print('Digite 3 comprimentos de retas')
a = float(input('Primeira reta: '))
b = float(input('Segunda reta: '))
c = float(input('Terceira reta: '))
if a > abs(b-c) and a < (b+c) or b > abs(a-c) and b < (a+c) or c > abs(a-b) and c < (a+b): # a função abs() coloca os números em módulo - valor absoluto
    print('Os comprimentos digitados PODEM formar um triângulo.')
else:
    print('Os comprimentos digitados NÃO podem formar um triângulo.')
print('\n')
#-----------------------------------------------------------------------------------------------------------------------------
#Outra resolução seria:
if a < b + c and b < a + c and c < a + b:
    print('Pode formar triângulo')
#------------------------------------------------------------------------------------------------------------------------------

#EXPLICAÇÃO: Condição para a formação de um triângulo
#Só irá existir um triângulo se, somente se, os seus lados obedeceram à seguinte regra:
#um de seus lados deve ser maior que o valor absoluto (módulo) da diferença dos outros dois lados
#e menor que a soma dos outros dois lados.'''
#| b - c | < a < b + c
#| a - c | < b < a + c
#| a - b | < c < a + b