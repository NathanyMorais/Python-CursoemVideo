'''Crie um programa que tenha uma função chamada VOTO() que vai receber como parâmetro o Ano de Nascimento de uma
pessoa, retornando um valor literal indicando se uma pessoa tem voto negado, opcional ou obrigatório nas eleições.'''

def voto(ano):
    print('-'*30)
    from datetime import datetime #biblioteca de data/ano
    atual = datetime.now().year #comando para considerar o ano atual
    idade = atual - ano #idade considera o ano atual menos o ano que a pessoa nasceu
    if idade < 16: #se idade for menor que 16
        return f'Com {idade} anos: NÃO VOTA'
    elif idade >= 18 and idade <= 65: #se idade for maior igual a 18 ou menor igual a 64
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65 : #se idade entre 16 e 18 anos ou maior que 65
        return f'Com {idade} anos: VOTO OPCIONAL'

#Programa principal
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))

















































