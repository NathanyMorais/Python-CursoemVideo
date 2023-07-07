'''Escreva um programa que leia a velocidade de um carro.
Se ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por km acima do limite permitido'''

print('\n','-'*3,'Controle de Velocidade','-'*3)
v = float(input('Valor da velocidade em Km/h: '))
multa = (v-80) * 7.0
if v > 80.0:
    print(f'Você foi multado pois excedeu o limite permitido que é 80km/h.')
    print(f'Pague a multa no valor de R${multa:.2f}.')
else:
    print('Parabéns, continue respeitando os limites de velocidade permitidos.')