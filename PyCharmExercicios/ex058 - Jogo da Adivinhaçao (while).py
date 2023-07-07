'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forma necessários
 para vencer.'''

import random
print('\n','\033[35;4m','-'*5,'JOGO DA ADIVINHAÇÃO','-'*5,'\033[m')
maq = random.randint(0,10) #escolhe aleatoriamente entre 0 e 10
palpite = 0 #contador
resp = int(input('''Adivinhe o número que eu pensei! 
Escolha um número entre 0 e 10: '''))
while maq != resp: #enquanto o número da maquina for diferente do número que o usuario digitar:
   palpite = palpite + 1 #contador para contar quantas tentativas o usuario fez
   if maq > resp: #se o numero da maquina for maior que o numero do usuário:
      resp = int(input('\033[31;4mVocê ERROU!\033[m Escolha um número MAIOR: '))
   else: #se o numero da maquina for menor que o numero do usuario:
      resp = int(input('\033[31;4mVocê ERROU!\033[m Escolha um número MENOR: '))
print(f'\033[34;1mACERTOU MIZERAVI!\033[m O número que eu pensei foi o \033[34;1m{maq}\033[m.')
print(f'Você acertou com {palpite+1} tentativas. Parabéns!') #[palpite+1] é a quantidade de tentativas feitas pelo usuário mais aquela primeira tentativa [+1]
print('\n')                                                  # que está fora do laço de repetição e por isso não entrou na contagem do contador.

#------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------------------------------
computador = random.randint(0,10)
print('''Sou seu computador...acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
palpite = 0
while not acertou:
   jogador = int(input('Qual é o seu palpite? '))
   palpite += 1
   if jogador == computador:
      acertou = True
print(f'Parabéns, você acertou com {palpite} tentativas!')