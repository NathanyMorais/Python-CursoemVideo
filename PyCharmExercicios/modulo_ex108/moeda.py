#Modulo do exercicio 108
def metade(n):
    return n / 2
def dobro(n):
    return n * 2

def aumentar(n,porcent):
    q = (n * porcent) / 100
    return n + q

def diminuir(n,porcent):
    q = (n * porcent) / 100
    return n - q

#Para trocar o ponto do float para vírgula, você deve converter para string e substituir com o método replace.
#A sintaxe do método replace é : string.replace('antigo' , 'novo')
def moeda(n):
    num = f'{n:.2f}'
    return str(num).replace('.',',')

# A sintaxe quer dizer : string(numero).replace("elemento que vai ser substituido", "elemento substituto")

#------------------------SOLUÇÃO DO PROFESSOR--------------------------

#O professor fez a função MOEDA() mais simplificada e recebendo 2 parametros:
#O parametro preço é referente ao valor que o usuario vai digitar
#O parametro sifrão que recebe o valor do real 'R$
'''def moeda(preço=0, sifrão='R$'):
    return f'{sifrão}{preço:.2f}'.replace('.',',')'''

#Ex: A função moeda vai retornar: 'R$ 10,50'