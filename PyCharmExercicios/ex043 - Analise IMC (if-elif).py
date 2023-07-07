'''Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status:
- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 ate 30: sobrepeso
- 30 ate 40: obesidade
- acima de 40: obesidade morbida
'''
print('\n','-'*5,'\033[1;36mCÁLCULO DO IMC\033[m','-'*5)
alt = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kg: '))
imc = (peso / (alt**2)) #peso / (altura * altura)
if imc < 18.5:
    print(f'IMC = {imc:.1f} - \033[31mAbaixo do peso \033[m')
elif imc < 25.0:
    print(f'IMC = {imc:.1f} - \033[32mPeso ideal \033[m')
elif imc < 30:
    print(f'IMC = {imc:.1f} - \033[35mSobrepeso \033[m')
elif imc < 40:
    print(f'IMC = {imc:.1f} - \033[35mObesidade \033[m')
else:
    print(f'IMC = {imc:.1f} - \033[31mObesidade Mórbida \033[m')

