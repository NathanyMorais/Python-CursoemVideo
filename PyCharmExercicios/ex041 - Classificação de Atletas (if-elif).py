'''A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
a sua categoria de acordo com a idade:
- ate 9 anos = mirim
- ate 14 = infantil
- ate 19 = junior
- ate 25 = senior
- acima = master'''

from datetime import date
print('\n','\033[33m Relatório da Confederação Nacional de Natação\033[m')
nome = str(input('Nome do atleta: '))
ano = int(input('Ano de nascimento: '))
x = date.today().year #Considera o ano atual
idade = x - ano
print('\033[1;31m Classificação do atleta \033[m')
print(f'Atleta: {nome.title()}')
if idade <= 9:
    print(f'{idade} anos: Categoria Mirim')
elif idade <= 14:
    print(f'{idade} anos:  Categoria Infantil')
elif idade <= 19:
    print(f'{idade} anos: Categoria Júnior')
elif idade <= 25:
    print(f'{idade} anos: Categoria Sênior')
else:
    print(f'{idade} anos: Categoria Master')
print('-'*40)


