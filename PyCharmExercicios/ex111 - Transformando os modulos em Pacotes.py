'''Crie um PACOTE chamado 'pacote_ex111' que tenha 2 modulos internos chamados moeda e dado.
 Transfira todas as funções utilizadas nos desafios 107 até 110 para o primeiro pacote e mantenha tudo funcionando'''

from pacote_ex111 import modulo_moeda

p = float(input('Digite o preço: R$ '))
modulo_moeda.resumo(p, 80, 35)


'''FUNÇÕES que estão DENTRO do MODULO modulo_moeda (MÓDULO QUE ESTÁ DENTRO DO PACOTE pacote_ex111):

def metade(n, sit=False):
    num = n / 2
    if sit == True:
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

def diminuir(n=0, porcent=0, sit=False):
    q = (n * porcent) / 100
    num = n - q
    if sit == True:
        return moeda(num)
    else:
        return num

def moeda(preço=0, sifrão='R$'):
    return f'{sifrão}{preço:.2f}'.replace('.',',')

def resumo(n=0, aumento=10, reducao=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30)) #o titulo fica centralizado
    print('-'*30)
    print(f'{"Preço analisado:"} \t{moeda(n)}')  #o comando '\t' faz a tabulção = formatação da tabela
    print(f'{"Dobro do preço:"} \t{dobro(n,True)}')
    print(f'{"Metade do preço:"} \t{metade(n,True)}')
    print(f'{aumento}% de aumento: \t{aumentar(n,aumento,True)}')
    print(f'{reducao}% de redução: \t{diminuir(n,reducao,True):}')
    print('-'*30)
'''


















