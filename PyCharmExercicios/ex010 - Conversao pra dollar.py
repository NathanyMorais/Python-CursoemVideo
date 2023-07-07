#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos
#dólares ela pode comprar. Considere 1 dolar = 3.27 reais
n = float(input('Insira seu saldo: R$ '))
print(f'Com R$ {n:.2f} é possível comprar US$ {n/3.27:.2f}')