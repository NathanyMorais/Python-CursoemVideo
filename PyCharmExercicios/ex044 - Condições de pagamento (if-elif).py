'''Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
- a vista dinheiro: 10% desconto
- a vista cartao: 5% desconto
- ate 2x no cartao: preço normal
- 3x ou mais no cartao: 20% de juros'''

prod = float(input('Valor do produto: '))
quant = int(input('Quantidade: ')) #quantos itens do produto foram comprados
tot = prod*quant #total a pagar
print('''Escolha a condição de pagamento: 
[A] À vista no dinheiro 
[B] À vista no cartão 
[C] Em 2x no cartão
[D] Em 3x ou mais no cartão''')
cond = str(input('Sua opção: ').lower())
a = (tot - (tot*10)/100) #10% de desconto a vista no dinheiro
b = (tot - (tot*5)/100) #5% desconto a vista no cartao
c = tot/2             #valor normal se pago em 2x no cartao
d = ((tot*20)/100 + tot) #valor com juros de 20% se pago em 3x ou mais
print('\n','*'*4,'\033[1;33mRECIBO PROVISÓRIO\033[m','*'*4,)
print(f'---- Preço unitário = R${prod:.2f}')
print(f'---- Qtde de itens = {quant}')
print(f'---- Total = R${tot:.2f}')
print('\033[32m','-'*3,'TOTAL A PAGAR','-'*3,'\033[m')
if cond == 'a':
    print(f'Desconto de 10% à vista no dinheiro: R$ {a:.2f}')
elif cond == 'b':
    print(f'Desconto de 5% à vista no cartão de crédito: R$ {b:.2f}')
elif cond == 'c':
    print(f'Pagamento no cartão de crédito em 2X de: R$ {c:.2f}')
elif cond == 'd':
    parcelas = int(input('Quantidade de parcelas: '))
    print(f'Pagamento a prazo com 20% juros: {parcelas}X de R${d/parcelas:.2f} ')
else:
    print('Opção de pagamento inválida')
print('-'*40)

