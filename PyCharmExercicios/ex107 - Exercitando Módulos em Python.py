'''Crie um módulo chamado MOEDA.PY que tenha as funções incorporadas: aumentar(), diminuir(), dobro()
e metade(). Faça também um programa que importe esse module e use algumas dessas funções'''

from modulo_ex107 import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')

'''Modulo_ex107:

def metade(n): #Função metade()
    return n / 2
    
def dobro(n):  #Função dobro()
    return n * 2

def aumentar(n,porcent): #Função aumentar()
    q = (n * porcent) / 100
    return n + q

def diminuir(n,porcent): #Função diminuir()
    q = (n * porcent) / 100
    return n - q '''