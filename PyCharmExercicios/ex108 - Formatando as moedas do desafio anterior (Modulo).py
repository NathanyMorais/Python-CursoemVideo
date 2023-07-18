'''Adapte o código do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar
os valores como um valor monetário formatado'''

from modulo_ex108 import moeda
p = float(input('Digite o preço: R$ '))
print(f'A metade de R${moeda.moeda(p)} é R${moeda.moeda(moeda.metade(p))}')
print(f'O dobro de R${moeda.moeda(p)} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')

#Vai mostrar o valor formatado como moeda: R$ 500,00 (separado por virgula e com 2 casas decimais depois da virgula)

'''Modulo_ex108:

def metade(n): #Função metade()
    return n / 2

def dobro(n):  #Função dobro()
    return n * 2

def aumentar(n,porcent): #Função aumentar()
    q = (n * porcent) / 100
    return n + q

def diminuir(n,porcent): #Função diminuir()
    q = (n * porcent) / 100
    return n - q 
    
def moeda(n):           #Função moeda() - formata o valor numérico como moeda (separado por virgula com 2 casas decimais)
    num = f'{n:.2f}'
    return str(num).replace('.',',')    
'''

#O professor fez a função MOEDA() mais simplificada e recebendo 2 parametros:
#O parametro preço é referente ao valor que o usuario vai digitar
#O parametro sifrão que recebe o valor do real 'R$
'''def moeda(preço=0, sifrão='R$'):
    return f'{sifrão}{preço:.2f}'.replace('.',',')'''

#Ex: A função moeda vai retornar: 'R$ 10,50'

