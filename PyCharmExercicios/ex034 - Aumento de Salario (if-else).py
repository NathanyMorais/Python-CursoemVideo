'''Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a 1250,00 calcule aumento de 10%.
Para salarios inferiores ou iguais, o aumento é de 15%.'''

print('\n','-'*3,'AUMENTO DE SALÁRIO','-'*3)
s = float(input('Digite o valor do salário atual: R$ '))
if s <= 1250.0:
    print(f'Com aumento de 15%, seu salário passa a ser de R$ {(s*15)/100 + s:.2f} ')
else:
    print(f'Com aumento de 10%, seu salário passa a ser de R$ {(s * 10) / 100 + s:.2f}')