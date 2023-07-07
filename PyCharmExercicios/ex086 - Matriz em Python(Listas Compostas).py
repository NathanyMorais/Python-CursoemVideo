'''Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.'''

matriz = []
for i in range(0,3): #para cada linha posicionada de 0 ate 2
    linha = [] #a lista 'linha' vai receber os numeros digitados de acordo com o numero de colunas, no caso, 3
    for j in range(0,3): #para cada coluna posicionada de 0 ate 2
        linha.append(int(input(f'Digite um valor para {[i,j]}: '))) #digite um valor que sera armazenado na lista linha
    matriz.append(linha[:]) #matriz recebe uma cópia das listas 'linha' que foram formadas
for i in range(0,3): #estrutura para percorrer todas as linhas e colunas da matriz
    for j in range(0,3):
        print(f'[{matriz[i][j]}]',end='') #imprime a matriz na tela, cada número dentro de []
    print()
print('\n','*'*50)
#Exemplo de resultado da minha matriz não formatada:
    #[12][13][14]
    #[5][6][7]
    #[89][90][91]

#-------------------------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------
matriz = [[0,0,0], [0,0,0], [0,0,0]] #matriz declarada já com valores (não precisa usar .append() nesse caso pois já tem valores)
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha},{coluna}]: '))
print('-='*30)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]',end='') #imprime a matriz formatada com os números centralizados dentro de 5 espaços/caracteres
    print()
#Exemplo de resultado da matriz formatada:
    #[ 78  ][ 98  ][ 85  ]
    #[ 159 ][ 357 ][ 852 ]
    #[1234 ][5678 ][9101 ]