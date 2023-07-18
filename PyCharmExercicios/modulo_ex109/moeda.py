#Modulo do exercicio 109
def metade(n, sit=False):
    num = n / 2
    if sit == True:  #se a situação for True (verdadeira), faz a formatação do número para moeda brasileira
        return moeda(num)
    else:
        return num
def dobro(n, sit=False):
    num = n * 2
    if sit == True:  #se a situação for True (verdadeira), faz a formatação do número para moeda brasileira
        return moeda(num)
    else:
        return num
def aumentar(n, porcent, sit=False):
    q = (n * porcent) / 100
    num = n + q
    if sit == True:  #se a situação for True (verdadeira), faz a formatação do número para moeda brasileira
        return moeda(num)
    else:
        return num
def diminuir(n, porcent, sit=False):
    q = (n * porcent) / 100
    num = n - q
    if sit == True:  #se a situação for True (verdadeira), faz a formatação do número para moeda brasileira
        return moeda(num)
    else:
        return num
def moeda(preço=0, sifrão='R$'):
    return f'{sifrão}{preço:.2f}'.replace('.',',')
#Para trocar o ponto do float para vírgula, você deve substituir com o método replace.
# A sintaxe do REPLACE quer dizer : .replace("elemento que vai ser substituido", "elemento substituto")

#-----------------------------------------------------------------------------------------------------------------
#O professor fez a função MOEDA() mais simplificada e recebendo 2 parametros:
#O parametro preço é referente ao valor que o usuario vai digitar
#O parametro sifrão que recebe o valor do real 'R$
'''def moeda(preço=0, sifrão='R$'):
    return f'{sifrão}{preço:.2f}'.replace('.',',')'''

#Ex: A função moeda vai retornar: 'R$ 10,50'