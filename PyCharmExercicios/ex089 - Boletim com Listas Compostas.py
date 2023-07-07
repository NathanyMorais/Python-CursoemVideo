'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.'''

turma = []
resultado = ' '
while True:
    nome = (str(input('Nome: ')))
    nota1 = (float(input('Nota 1: ')))
    nota2 = (float(input('Nota 2: ')))
    media = (nota1 + nota2)/2
    if media >= 7.0:
        resultado = 'Aprovadx'
    elif media <= 6.9:
        resultado = 'Reprovadx'
    turma.append([nome, [nota1, nota2], media, resultado]) #lista composta com todos os dados dos alunos
    r = str(input('Deseja continuar? [S/N]: '))
    if r in 'Nn':
        break
print(f'Ficha dos alunos cadastrados: {turma}')
print(f'Você cadastrou {len(turma)} alunos.')
print('-='*40)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8}{"RESULTADO":>13}') #"Nº" com 4 caracteres alinhados à esquerda. "NOME" com 10 caracteres alinhados à esquerda. "MEDIA" com 8  caracteres alinhados à direita
print('-'*35)
for i, a in enumerate(turma): #para índice e aluno na lista Turma
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}{a[3]:>13}') # i = o número do aluno é o índice/posição do laço
while True:                                # a[0] = informa o nome do aluno na lista turma seguindo a mesma formatação de espaço acima
    print('-'*35)                          # a[2] = informa a média do aluno na lista turma com 1 casa decimal depois da vírgula
    res = int(input('Mostrar notas de qual aluno? (999 para interromper): '))
    if res == 999:
        print('Finalizando...')
        break
    if res <= len(turma)-1: #A resposta do usuário deve ser um número menor do que a quantidade de alunos na lista - 1.
        print(f'As notas de {turma[res][0]} foram {turma[res][1]}, portanto está {turma[res][3]}')   #[-1] pois o primeiro aluno é a posição 0 e o último aluno é n-1.
print('Programa finalizado. Volte sempre!')                      #{turma[res][0]} representa o nome do aluno que está na posição 0 da lista externa
                                                                 #{turma[res][1]} mostra as notas do aluno que está na posição 1 da lista externa






























