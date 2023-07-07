'''Desenvolva um programa que pergunte a distancia de uma viagem em km. Calcule o preço da passagem,
cobrando 0.50 por km para viagens de até 200km e 0.45 para viagens mais longas'''

print('\n','-'*3,'VALOR DA PASSAGEM','-'*3)
d = float(input('Informe a distância da viagem em Km: '))
if d <= 200.0:
    print(f'Para a distância de {d}km, o valor da passagem é de R${(d * 0.5):.2f}.')
else:
    print(f'Para a distância de {d}km, o valor da passagem é de R${(d * 0.45):.2f}.')
print('\n')

#Uso de OPERADOR TERNÁRIO para resolver o exercício:
d = float(input('Informe a distância da viagem em Km: '))
preço = d * 0.5 if d <=200 else d * 0.45
print(f'O preço da sua passagem será de R$ {preço:.2f}')