#Escreva um programa que converta a temperatura de ºC para ºF e Kelvin.
print('-'*5,"Conversor de Temperatura",'-'*5)
c = float(input('Insira a temperatura em ºC: '))
f = c * 1.8 + 32
k = c + 273
print(f'A temperatura {c}ºC equivale a  {f:.1f}ºF e {k:.1f}K')
print('-'*37)