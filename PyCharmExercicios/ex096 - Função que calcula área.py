'''Faça um programa que tenha uma FUNÇÃO chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno'''

#Função área com 2 parâmetros (largura e comprimento)
def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {a:.2f}m².')

#Código principal
print('\nControle de Terrenos')
print('-'*26)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)























