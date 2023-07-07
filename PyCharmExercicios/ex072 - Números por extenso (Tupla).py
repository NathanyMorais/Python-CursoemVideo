'''Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostra-lo por extenso'''

'''digite um numero entre 0 e 20: 90
tente novamente. Digite um numero entre 0 e 20: 16
Você digitou o número dezesseis'''

tupla = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez','onze','doze','treze','catorze',
         'quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um número entre o e 20: '))
    while num < 0 or num > 20: #laço para que a pergunta se repita enquanto o usuario digitar numero inválido - menor que zero ou maior que 20
        num = int(input('Tente novamente. Digite um número entre o e 20: '))
    print(f'Você digitou o número \033[31;1m{tupla[num]}\033[m.')
    res = str(input(f'\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if res == 'N':
        break
print('*'*50,'\n')
#-------------------SOLUÇÃO DO PROFESSOR----------------------
cont = ('zero','um','dois','três','quatro','cinco','seis',
         'sete','oito','nove','dez')
while True:
    n = int(input('Digite um valor entre 0 e 10: '))
    if 0 <= n <= 10:
        break
    print('Tente novamente.', end=' ')
print(f'Você digitou o número \033[31;1m{cont[n]}\033[m.')