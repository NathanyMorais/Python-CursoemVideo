'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime

dados = {} #dicionario vazio
ano = 0
atual = datetime.now().year #considera o ano atual
dados['Nome'] = str(input('Nome: ')) #adiciona o valor na chave 'nome' do dicionário
ano = int(input('Ano de nascimento: '))
dados['Idade'] = atual - ano #adiciona o valor na chave 'idade' do dicionário (ano atual - ano do nascimento = idade)
dados['CTPS'] = int(input('Carteira de Trabalho (0 se não tem): ')) #adiciona o valor na chave 'ctps' do dicionário
if dados['CTPS'] != 0: #se o usuario tiver ctps, continua com os dados de trabalho
    dados['Contratação'] = int(input('Ano de contratação: ')) #adiciona o valor na chave 'contrataçao' do dicionário
    dados['Salário'] = float(input('Salário atual: R$ ')) #adiciona o valor na chave 'salario' do dicionário
    dados['Aposentadoria'] = (dados['Contratação'] + 35 - atual) + dados['Idade'] #adiciona o valor na chave 'aposentadoria' do dicionário
print('-'*30)                                                                         #com a conta para saber com quantos anos o usuario vai aposentar
print('\033[32;1m>> RELATÓRIO FINAL <<\033[m')
for k, v in dados.items(): #laço para percorrer as chaves (k) e os valores (v) do dicionario
    print(f'- {k} tem o valor {v}.')
print('-'*30)