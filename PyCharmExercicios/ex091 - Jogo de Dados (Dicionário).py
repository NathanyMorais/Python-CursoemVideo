'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.  No final, coloque esse dicionário em ordem,
sabendo que o vencedor tirou o maior número no dado.'''

from random import randint
from time import sleep

lista = list() #lista vazia
jogo = dict() #dicionario vazio
jogo['jogador1'] = randint(1,6) #dicionário 'JOGO' adicionando um valor aleatório na chave 'jogador1'..e assim por diante
jogo['jogador2'] = randint(1,6)
jogo['jogador3'] = randint(1,6)
jogo['jogador4'] = randint(1,6)
lista.append(jogo.copy()) #adicionando uma cópia do dicionário 'jogo' na lista composta
print(f'\033[33mVALORES SORTEADOS\033[m')
for i in lista: #laço que percorre a lista
    for k, v in i.items(): #laço que percorre cada chave e valor do dicionario
        print(f'O {k} tirou {v}')
        sleep(1)
print('-'*25)
print('\033[34;1mRANKING DOS JOGADORES\033[m')
sleep(2)
for i in lista: #laço que percorre a lista
    cont = 1 #contador para fazer a contagem do rankin (1º lugar, 2º lugar, etc)
    for v in sorted(jogo, key=jogo.get, reverse=True): #comando para colocar os 'values' do dicionário em ORDEM DECRESCENTE
        print(f'{cont}º lugar: {v} com {jogo[v]}') #nesse caso, a chave [v] do dicionário vai acompanhar a ordem em que os valores estão,
        cont += 1                                  #do maior valor para o menor.
        sleep(1)
    print()
print('---------------------------FIM------------------------\n')
#--------------------------------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------------
from random import randint
from time import sleep
from operator import itemgetter #Biblioteca usada para colocar o dicionário em ordem
ranking = list() #lista vazia
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),  #Dicionário que armazena um número aleatorio sorteado para cada jogador.
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
print('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #vai criar uma lista ordenada dos valores (que estão na posição [1] do dicionário)
print('   ===RANKING DOS JOGADORES===')                            #com o reverse=True a ordem será do maior para o menor
for i, v in enumerate(ranking):                                   #se quisesse ordenar pelas chaves do dicionário, era só usar a posição 0.
    print(f'    {i+1}º Lugar: {v[0]} com {v[1]}.') #Laço FOR para percorrer os índices e valores da lista 'ranking'.














