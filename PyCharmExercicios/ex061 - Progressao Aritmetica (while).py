'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da PA, usando a estrutura WHILE'''

n = 10 #quantidade de números
a1 = int(input('Digite o 1º termo: ')) #primeiro número
r = int(input('Razão: ')) #razão = quantidade de passos
an = a1 + (n - 1) * r #formula para encontrar o último número = termo geral
print(a1, end=' ') #para mostrar o primeiro termo na tela
while a1 < an: #enquanto o termo for menor que o último número:
     a1 = a1 + r  #termo = termo + razão
     print(a1, end=' ') #imprime o termo
print('\nFIM')
#-------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------------------
print('\033[31mGerador de P.A\033[m')
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
     print(f'{termo}-', end=' ')
     termo += razao
     cont += 1
print('FIM\n')