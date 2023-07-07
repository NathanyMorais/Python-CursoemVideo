#Faça um algoritmo que leia o salario de um funcionario e mostre novo valor com 15% de aumento
salario = float(input('Insira o valor do salário atual: R$ '))
aumento = (15/100) * salario
print(f'Com o aumento de 15% seu salário vai para R${salario +aumento:.2f}')