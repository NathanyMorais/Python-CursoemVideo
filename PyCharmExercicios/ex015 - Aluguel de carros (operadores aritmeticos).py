#Escreva um programa que pergunte a quantidade de dias e Km percorridos por um carro alugado.
#Calcule o preço a apagar sabendo que o carro custa R$60,00/dia e R$0,15/km.
print('-'*5,'Aluguel de Veículo','-'*5)
dias = int(input('Total de dias alugados: '))
km = float(input('Total de Km rodados: '))
preço = (dias * 60) + (km * 0.15)
print(f'Valor a pagar = R${preço:.2f}')
print('-'*35)
