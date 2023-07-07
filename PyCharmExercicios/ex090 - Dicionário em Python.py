'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.'''


dados = {} #dicionario vazio

dados['Nome'] = str(input('Nome: ')) #adiciona valor a chave 'nome' do dicionario
dados['Média'] = float(input(f'Média de {dados["Nome"]}: ')) #adiciona valor a chave 'média' do dicionario
dados['Situação'] = ' ' #chave situação ainda não possui valor e será testado na estrutura IF
if dados['Média'] >= 7: #se a média for maior que 7
    dados['Situação'] = 'Aprovado' #adiciona o valor 'Aprovado' a chave 'situação' do dicionário
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
else: #se a média for menor que 5
    dados['Situação'] = 'Reprovado' #adiciona o valor 'Reprovado' a chave 'situação' do dicionário
 #adiciona uma cópia do dicionario 'dados' na lista composta 'ficha'
print('=-'*5, f'\033[1mRELATÓRIO FINAL\033[m','=-'*5)
for k, v in dados.items(): #laço que percorre cada item do dicionário (as chaves e os valores)
    print(f'{k} é igual a {v}.')
print('=-'*19)











