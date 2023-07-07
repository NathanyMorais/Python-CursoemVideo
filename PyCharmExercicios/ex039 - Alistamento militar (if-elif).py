'''Faça um programa que leia o ano de nascimento do usuario e informe de acordo com sua idade se:
 - ele ainda vai se alistar ao serviço militar
 - se é hora de se alistar
 - se já passou do tempo do alistamento
 O programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
import datetime

print('\n','\033[4;32mALISTAMENTO MILITAR''\033[m')
ano = int(input('Digite o ano em que você nasceu: '))
ano_atual = datetime.date.today().year #considera o ano atual do PC
idade = ano_atual - ano
if ano == (ano_atual - 18):
    print(f'Você tem {idade} anos e deve se alistar ao serviço militar ainda esse ano.')
elif ano < (ano_atual - 18) :
    print(f'Você já tem {idade} anos e infelizmente passou {idade - 18} anos do prazo de se alistar.')
    print(f'Seu alistamento deveria ter sido em {ano_atual - (idade-18)}.')
elif ano > (ano_atual - 18):
    print(f'Você ainda tem {idade} anos, por isso faltam {18 - idade} anos para poder se alistar.')
    print(f'Seu alistamento será em {ano_atual + (18 - idade)}.')