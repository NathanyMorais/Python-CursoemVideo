'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

dados = {} #dicionario vazio
gol = [] #lista vazia para armazenar os gols
dados['Nome'] = str(input('Nome da jogadora: ')) #armazena valor na chave 'nome' do dicionário
n = int(input(f'Quantas partidas {dados["Nome"]} jogou? ')) #variável para armazenar a qtde de partidas
for c in range(1,n+1): #laço para percorrer exatamente a qtde de partidas que o usuario digitou - começando pelo número 1
    gol.append(int(input(f'  Quantos gols na partida {c}: '))) #lista que vai armazenar quantos gols foram feitos em cada partida
dados['Gols'] = gol[:] #armazena valor em forma de lista na chave 'gols' do dicionário - é uma lista dentro do dicionário
dados['Total'] = sum(gol) #armazena valor na chave 'Total' do dicionário - o valor é calculado pela soma dos valores que estão dentro da lista 'gol'
print('='*50)
print(dados) #imprime o dicionário 'dados' na tela.
print('='*50)
for k, v in dados.items(): #percorre todas as chaves e valores do dicionário 'dados'
    print(f'O campo {k} tem valor {v}.')
print('='*50)
print(f'A jogadora {dados["Nome"]} jogou {len(dados["Gols"])} partidas.')
for i, v in enumerate(gol): #laço que percorre o índice e valores apenas da lista 'gol' onde está armazenado a qtde de gols que foram feitos em cada partida
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["Total"]} gols.')
print('='*50)





























