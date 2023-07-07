'''Crie um programa que faça o computador jogar jokenpô com você'''

from time import sleep
import random
print('\n','\033[1;30;45m-='*10,'JOKENPÔ','-='*10,'\033[m','\n')
v = '\033[1;31m'
a = '\033[1;34m'
am = '\033[1;33m'
f = '\033[m'
lista = ['papel', 'pedra', 'tesoura']
pa = 'papel'
pe = 'pedra'
te = 'tesoura'
maq = random.choice(lista)
us = str(input('Escolha: pedra, papel ou tesoura? '))
print(f'{am}JÔ{f}',end = "-")
sleep(1)
print(f'{am}KEN{f}',end = "-")
sleep(1)
print(f'{am}PÔ{f}')
if maq == pa and us == pe or maq == pe and us == te or maq == te and us == pa:
    print(f'{v}HA-HA! Você PERDEU! O computador jogou {maq}.')
    print(f'Tente Outra vez!!{f}')
elif us == pa and maq == pe or us == pe and maq == te or us == te and maq == pa:
    print(f'{a}Você GANHOU! O computador jogou {maq}.')
    print(f'Vamos de novo!!{f}')
elif us == pa and maq == pa or us == pe and maq == pe or us == te and maq == te:
    print(f'Empatou! Vamos jogar de novo?')
else:
    print('Algo está errado, jogue novamente.')
print('-'*50)








