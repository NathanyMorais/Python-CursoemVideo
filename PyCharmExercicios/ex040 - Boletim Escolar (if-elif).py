'''Crie um programa que leia 2 notas de um aluno e calcule a media, mostrando a mensagem no final:
- media abaixo de 5 = reprovado
- media entre 5 e 6.9 = recuperação
- media 7 ou superior = aprovado'''

nome = str(input('Nome do aluno: '))
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
print('\n','\033[1;90;40m-'*10,'BOLETIM ESCOLAR','-'*10,'\033[m')
print(f'Nome: {nome.upper()}')
print(f'--- 1ºBimestre: {n1}')
print(f'--- 2ºBimestre: {n2} ')
print(f'---- MÉDIA: {m:.1f} ----')
if m < 5.0:
    print('Você foi\033[1;31m REPROVADX\033[m.')
elif m >= 5.0 and m <= 6.9:
    print('Você está de\033[1;33m RECUPERAÇÃO\033[m.')
elif m >= 7.0:
    print('Parabéns, você foi\033[1;34m APROVADX\033[m.')
print('-'*40)

