'''Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador.'''

jogadores = [] #lista vazia
dados = {} #dicionário vazio
gol = [] #lista vazia
while True:
    dados['Nome'] = str(input('Nome do jogador: '))
    n = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(1,n+1):
        gol.append(int(input(f'Quantos gols na partida {c}: ')))
    dados['Gols'] = gol[:]
    dados['Total'] = sum(gol)
    jogadores.append(dados.copy())
    gol.clear()
    while True:
        r = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite apenas S ou N.')    
    if r == 'N':
        break
print('='*50)
cont = 0 #contador iniciando com 0 (igual a contagem dos índices da lista)
print(f'{"Cód":<6}{"Nome":<10}{"Gols":>10}{"Total":>10}') #Cabeçalho do relatório
for jogador in jogadores: #laço que percorre a lista de jogadores
    print(f'{cont:<6}{jogador["Nome"]:<10}{str(jogador["Gols"]):>10}{jogador["Total"]:>10}') #Dados dos jogadores que preenchem o relatório
    cont += 1 #contador para preencher o código de cada jogador no relatório                #O item 'jogador["Gols"]' foi transformado em string 'str'
print('-'*40)                                                                             # apenas para permitir a formatação dos espaços ':>10'
'''print('Cód ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')       #CÓDIGO QUE O PROFESSOR USOU PRA FAZER O CABEÇALHO DO RELATÓRIO
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')        #Código usado para percorrer os valores dos dicionários e preencher o relatório
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()'''
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 interrompe): '))
    if busca == 999: #se usuário digitar 999 o programa encerra
        break
    if busca >= len(jogadores): #se usuário digitar um número maior do que a quantidade de jogadores da lista, o programa dá erro.
        print(f'Erro! Não existe jogador com o código {busca}.')
    else: #se usuário digitar um número correspondente ao índice/código de um jogador, imprime o relatório na tela
        print(f'**LEVANTAMENTO DO JOGADOR {jogadores[busca]["Nome"]}**') #mostra o Nome do jogador que está na posição que o usuário digitar
        for i, v in enumerate(jogadores[busca]['Gols']): #para índices e valores referentes aos gols do jogador que está na posição digitada pelo uruário
            print(f'- No jogo {i+1} fez {v} gols') #mostra o [índice+1] para não iniciar em 0 e a quantidade de gols cadastrados naquele índice
    print('-'*40)
print('<< Programa Encerrado! >>')

































