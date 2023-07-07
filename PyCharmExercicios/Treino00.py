'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
- Média de idade
- Nome do homem mais velho
- Quantas mulheres tem menos de 50 anos'''
import random

age = 0 #usado para somar as idades que forem digitadas
maisvelho = 0 #idade do homem mais velho
nomevelho ='' #nome do homem mais velho
contM = 0
for p in range(1,4+1):
    print(f'----PESSOA nº{p}----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo [F/M]: '))
    age = age + idade #soma as idades
    if p == 1 and sexo in 'Mm':
        maisvelho = idade
        nomevelho = nome
    else:
        if maisvelho < idade and sexo in 'Mm':
            maisvelho = idade
            nomevelho = nome
    if sexo in 'Ff' and idade < 50:
        contM = contM + 1

print(f'A média entre as idades do grupo é de {age/3:.0f} anos.')
print(f'O homem mais velho tem {maisvelho} anos e se chama {nomevelho}.')
print(f'No grupo existem {contM} mulheres com menos de 50 anos.')
print('------------------------------------\n')
#-----------------------------------------------------------------------------------------------------------------------
'''Faça um programa que leia o peso de 3 pessoas. No final, mostre qual foi o maior e
o menor peso lidos.'''

maior = 0
menor = 0
for p in range(1,3+1):
    peso = float(input(f'Peso da pessoa {p}: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Maior peso é {maior}kg e menor peso é {menor}kg')
print('\033[31mFIM!!!!\033[m')

#-----------------------------------------------------------------------------------------------------------------------
'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10.
 Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites forma necessários
 para vencer.'''

import random
machine = random.randint(0,10)
print(machine)
palpite = 0
print('Adivinhe qual o número que eu pensei entre 0 e 10!')
player = int(input('Qual o seu palpite: '))
while machine != player:
    palpite += 1
    if machine < player:
        player = int(input('Menor...tente outra vez: '))
    elif machine > player:
        player = int(input('Maior...tente outro número: '))
print(f'Acertou mizeravi! Você precisou de {palpite+1} tentativas!')