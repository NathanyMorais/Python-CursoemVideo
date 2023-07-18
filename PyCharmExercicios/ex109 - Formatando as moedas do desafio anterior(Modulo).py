'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais,
informando se o valor retornado por eles vai ser ou não formatado pela função moeda(), que foi desenvolvida
no desafio 108.'''

from modulo_ex109 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, False)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, False)}')

#Quando True, mostra o valor da moeda formatado com virgula e 2 casas decimais
#Quando False, mostra o valor da moeda sem a formatação

'''Modulo ex109:

def metade(n, sit=False):
    num = n / 2
    if sit == True:  #se a situação for True (verdadeira), faz a formatação do número para moeda brasileira
        return moeda(num)
    else:
        return num
        
def dobro(n, sit=False):
    num = n * 2
    if sit == True: 
        return moeda(num)
    else:
        return num
        
def aumentar(n, porcent, sit=False):
    q = (n * porcent) / 100
    num = n + q
    if sit == True:
        return moeda(num)
    else:
        return num
        
def diminuir(n, porcent, sit=False):
    q = (n * porcent) / 100
    num = n - q
    if sit == True: 
        return moeda(num)
    else:
        return num
        
def moeda(preço=0, sifrão='R$'):   #Função Moeda()
    return f'{sifrão}{preço:.2f}'.replace('.',',')
'''


