'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados
b) Os ultimos 4 colocados
c) Uma lista com os times em ordem alfabética
d) Em que posição está o time da Fortaleza'''

times = ('Botafogo','Palmeiras','Atlético','Gremio','Flamengo','Fluminense','AthleticoPR','Sao Paulo',
         'Fortaleza','Cruzeiro','Bragantino','Santos','Internacional','Cuiaba','Bahia','Corinthians','Goiás',
         'América','Vasco','Coritiba')
print(f'Os times classificados na Série A de 2023 são: \033[33;1m{times[1:]}\033[m.')
print(f'Os 5 primeiros colocados são: \033[35;1m{times[0:5]}\033[m')
print(f'Os 4 últimos colocados são: \033[34;1m{times[-4:]}\033[m') #fatiamento inicia no 4ºnumero de trás para frente e termina no ultimo
print(f'Classificados em Ordem Alfabética: \033[32;1m{sorted(times[1:])}\033[m')
print(f'O time da Fortaleza se encontra na {times.index("Fortaleza")+1}ª posição.')#[+1] para mostrar a posição correta do time, visto que a contagem da tupla se inicia no 0
































