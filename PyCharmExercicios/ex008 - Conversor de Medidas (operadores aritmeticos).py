#Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
m = float(input('Insira um valor em metros: '))
dm = m * 10 #decimetro
cm = m * 100 #centimetro
mm = m * 1000 #milimetro
dam = m * 0.10 #decametro  ou m / 10
hm = m * 0.01 #hectometro  ou m / 100
km = m * 0.001 #quilometro ou m / 1000
print(f'Esse valor corresponde a: \n {dm} decímetros \n {cm} centímetros \n {mm} milímetros')
print(f' {dam} decâmetros \n {hm} hectômetros \n {km} quilômetros')