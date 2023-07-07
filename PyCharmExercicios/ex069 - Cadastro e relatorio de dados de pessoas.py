'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuario quer ou não continuar. No fim, mostre:
a) Quantas pessoas acima dos 18 anos
b) Quantos homens foram cadastrados
c) Quantas mulheres tem menos de 20 anos'''

cont_maior = 0 #contador para maiores de 18
cont_hom = 0 #contador para homens
cont_mul = 0 #contador para mulheres com menos de 20
while True:
    print('\n\033[33;1m','='*6,'CADASTRO DE PESSOA','='*6,'\033[m')
    idade = int(input('Idade: '))
    sexo = ' '  #string vazia para receber a resposta 'M ou F'
    while sexo not in 'FfMm': #laço para que o programa funcione APENAS se for digitado M ou F
        sexo = str(input('Sexo [F/M]: ')).strip()[0]
    if idade >= 18:
        cont_maior += 1 #contador para maiores de 18
    if sexo in 'Mm':
        cont_hom += 1 #contador para homens
    if sexo in 'Ff' and idade < 20:
        cont_mul += 1 #contador para mulheres com menos de 20
    c = ' ' #string vazia para receber a resposta 'N ou S'
    while c not in 'SN': #laço para que o programa funcione APENAS se for digitado S ou N
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if c == 'N': #se digitado 'N' o programa é interrompido
        break #comando de parada
print('\033[34;1;4m========== RELATÓRIO FINAL ==========\033[m')
print(f'\033[32mTiveram {cont_maior} pessoas com mais de 18 anos. ')
print(f'Foram cadastrados {cont_hom} homens.')
print(f'Um total de {cont_mul} mulheres possuem menos de 20 anos\033[m')

