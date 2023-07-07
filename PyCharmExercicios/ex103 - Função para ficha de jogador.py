'''Faça um programa que tenha uma função chamada FICHA(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
sido informado corretamente.'''

def ficha(nome=' ',gol = 0):
    if nome == '':
        nome = '<desconhecido>'
    if gol == '':
        gol = 0
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')
    print('-='*15)

#programa principal
print('-='*15)
jogador = str(input('Nome do Jogador: '))
gols = input('Número de Gols: ') #O problema de manter dessa forma, é que o programa vai aceitar qualquer caracter que o usuário digitar
ficha(jogador, gols)

#-----------------------------SOLUÇÃO DO PROFESSOR----------------------------------------------------------------------
def ficha(nome='<desconhecido>',gol = 0):
    print(f'O jogador {nome} fez {gol} gol(s) no campeonato.')

#programa principal
jog = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric(): #se o usuario digitar apenas números na variável 'gols'
    gols = int(gols) #transforma o valor em número inteiro (já que no input ele está como string)
else: #se o usuario digitar qualquer caracter que não seja numérico
    gols = 0 #transforma o valor digitado em zero
if jog.strip() == '': #se não for digitado nenhum nome para o jogador
    ficha(gol=gols) #a função vai considerar apenas a quantidade de gols
else: #se for digitado o nome do jogador
    ficha(jog, gols) #a função deve considerar todos os parâmetros







































