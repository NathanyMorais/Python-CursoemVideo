'''Faça um mini-sistema que utiliza Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'fim', o programa se encerrará.'''

from time import  sleep
#Lista de cores iniciando na posição 0 até a 4.
cores = ('\033[m',            # 0 - sem cores
         '\033[1;100;97m',    # 1 - fundo cinza, letra branca
         '\033[1;42;97m',     # 2 - fundo verde, letra branca
         '\033[1;105;30m',    # 3 - fundo rosa, letra preta
         '\033[7;1m')         # 4 - fundo branco, letra preta (inversão de cores da tela padrão)
def pyhelp(comand):
    título(f'Acessando o manual do comando \'{comand}\'', 2)
    print(cores[4], end='')
    help(comand)
    print(cores[0], end='')
    sleep(2)
def título(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~'* tam)
    print(f'  {msg}')
    print('~'* tam)
    print(cores[0], end='')
    sleep(1)


#Programa principal
comando = ' '
while True:
    título('SISTEMA DE AJUDA DO PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        pyhelp(comando)
título('PROGRAMA ENCERRADO. ATÉ BREVE!', 3)







