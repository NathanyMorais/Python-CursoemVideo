'''Faça um programa que tenha uma função chamada NOTAS() que pode receber várias notas de alunos e vai retornar um dicionário com
 as seguintes informações: Quantidade de notas, a maior nota, a menor nota, a média da turma, a situação (opcional).
 Adicione também as docstrings da função.'''

def notas(*n,sit=False):
    """
    --> Função para analisar notas e situações de vários alunos
    :param n: uma ou mais notas de alunos
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: retorna um dicionário com várias informações sobre a situação da turma
    """
    dict = {}
    dict['Total'] = len(n)
    dict['Maior'] = max(n)
    dict['Menor'] = min(n)
    dict['Média'] = sum(n)/len(n)
    if sit == True: #aceita também 'if sit:' (Não precisa afirmar que deve ser igual a True)
        if dict['Média'] >= 7.0: #se media maior igual a 7
            dict['Situação'] = 'BOA' #situação é boa
        elif dict['Média'] >= 5.0: #se média maior igual a 5 (e menor que 7)
            dict['Situação'] = 'RAZOÁVEL' #situação é razoavel
        else: #se média menor que 5
            dict['Situação'] = 'RUIM' #situação é ruim
    return dict #retorna o dicionário completo com todas as chaves

#Programa principal
resp = notas(2.8, 1.5, 8.3, 2.0, sit=True)
print(resp)
help(notas)

















