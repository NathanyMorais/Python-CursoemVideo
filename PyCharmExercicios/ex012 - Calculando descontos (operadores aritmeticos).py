#Faça um algoritmo que leia o preço de um produto e mostre:
# o seu novo valor com 5% de desconto para pagamento a vista.
# valor com 8% de aumento para pagamento parcelado
p = float(input('Insira o preço do produto: R$ '))
desconto = p*(5/100)
aumento = p*(8/100)
print('='*15)
print(f'Para pagamento à vista, o valor do produto é de R$ {p-desconto:.2f} com desconto de 5%.')
print(f'Para pagamento parcelado, o valor do produto é de R$ {p+aumento:.2f} com aumento de 8%.')
print('='*15)