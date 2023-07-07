'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

print('\n','\033[97;40;1m','-> É PAR OU É ÍMPAR? <- \033[m')
conquista = 0 #variavel para contar a quantidade de ganhos
soma = 0 #variavel para somar o numero do usuario com o numero da maquina
while True:
    maq = randint(0,10) #valor escolhido aleatoriamente pela maquina
    n = int(input('Digite um valor: '))
    soma = maq + n
    jog = ' ' #variável string vazia para receber a resposta
    while jog not in 'PI': #laço para que o programa só funcione se o jogador escolher P ou I
        jog = str(input('Você quer par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {n} e o computador jogou {maq}. Total de {soma}.')
    if soma % 2 == 0 and jog == 'P': #se a soma dos numeros usuario + maquina for PAR e o usuario escolher par, ele ganha e o loop continua
        print('\033[33;1mVocê GANHOU!\033[m')
        print('='*30)
        conquista += 1 #contador para contar qtde de conquista
    elif soma % 2 != 0 and jog == 'I': ##se a soma dos numeros usuario + maquina for IMPAR e o usuario escolher impar, ele ganha e o loop continua
        print('\033[33;1mVocê GANHOU!\033[m')
        print('='*30)
        conquista += 1 #contador para contar qtde de conquista
    else: #se as condições acima nao forem satisfeitas o usuario perde e o loop é interrompido pelo comando break
        print('\033[31;1mAh não, você perdeu!\033[m')
        break
print(f'\033[34;1;4mMas você teve {conquista} conquistas! Parabéns :)\033[m')
