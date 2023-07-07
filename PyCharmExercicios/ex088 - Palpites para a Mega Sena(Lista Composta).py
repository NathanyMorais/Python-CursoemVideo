'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos
 serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint
from time import sleep

print('\n\033[31;1m','*'*10,'MEGA-SENA','*'*10,'\n\033[m')
lista = []
n = int(input('Quantos jogos deseja que eu sorteie? '))
for l in range(0,n): #laço para que sejam feitos a quantidade 'n' de jogos que o usuario digitar
    for c in range(0,6): #laço para que seja sorteado apenas 6 numeros
        num = randint(1,60) #modulo random para escolher os numeros aleatorios no intervalo de 1 a 60
        if num not in lista: #se o numero não estiver dentro da lista (para que o número não apareça repetidamente)
            lista.append(num) #os numeros vão sendo sorteados e armazenados na lista
            lista.sort() #os números vão ficar em ordem crescente
    print(f'Jogo {l+1}: {lista}')
    sleep(1) #time de 2 milissegundos entre um jogo e outro
    lista.clear() #limpa a lista para que uma nova seja feita
print('\033[33;1m','*'*10,'BOA SORTE!','*'*10,'\033[m')

#------------------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------
lista = list()
jogos = list()
totjogos = 1
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)
quant = int(input('Quantos jogos você quer que eu sorteie?  '))
while totjogos <= quant: #enquanto o contador 'total de jogos' for menor ou igual a quantidade de jogos que o usuario digitar
    cont = 0
    while True:
        num = randint(1,60) #sorteia um numero entre 1 e 60
        if num not in lista: #se o numero não estiver na lista, adicione-o. (Para que o numero não se repita dentro da lista)
            lista.append(num)
            cont += 1 #contador para contar quantos números estão sendo adicionados na lista
        if cont >= 6: #estrutura para que o contador interrompa o sorteio quando tiverem 6 números na lista
            break
    lista.sort() #coloca a lista em ordem crescente
    jogos.append(lista[:]) #lista principal que recebe uma cópia dos números sorteados
    lista.clear() #limpa a lista temporária para quando ela receber mais uma remessa de numeros
    totjogos += 1  # contador para contar a quantidade de jogos que o usuário quer sortear
print('-='*3,f'SORTEANDO {quant} JOGOS','-='*3)
sleep(1)
for i, l in enumerate(jogos): #para posição e lista na lista principal 'jogos'
    print(f'Jogo {i+1}: {l}') #mostre jogo na posição {i+1} = lista de números
    sleep(1)
print('-='*4,'< BOA SORTE! >','-='*4)


















