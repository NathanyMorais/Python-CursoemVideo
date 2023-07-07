'''Desenvolva um programa que leia o Primeiro Termo e a Razão de uma PA - progressão aritmética.
No final, mostre os 10 primeiros termos dessa progressão.'''

print('\n','\033[33;1m','='*5,'10 TERMOS DA P.A','='*5,'\033[m')
#FÓRMULA MATEMÁTICA DA Progressão Aritmética:
n = 10 #n = número de termos, ou seja, quantidade de termos que terá na P.A
a1 = int(input('Primeiro termo: ')) #a1 = 1º Termo, é o número que vai iniciar a P.A
r = int(input('Razao: ')) #r = Razão da P.A
an = a1 + (n-1)*r #an = Termo Geral, é o último número que deve 'encerrar' a P.A
for c in range(a1,an+1, r):
    print(c, end='-')
print('FIM\n')
