'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
Mostre uma listagem de preços organizando os dados em forma tabular'''


print(f'\n\033[33;1m{"TABELA DE PREÇOS":^40}\033[m')
#---------SOLUÇÃO DO PROFESSOR----------------------------------------------------------------------------------
listagem= ('Lapis', 1.75,   #Tupla criada com tipos diferentes - 'strings' e floats
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Compasso', 9.99,
            'Canetas', 22.30,
            'Livro', 34.90)
for posicao in range(0,len(listagem)):
    if posicao % 2 == 0: #se a posição for par, mostra o nome do produto
        print(f'{listagem[posicao]:.<30}', end='')#[:.<30] trata-se de 30 caracteres alinhados à esquerda preenchidos com o nome do item seguido de pontos................
    else:  #se a posição for impar, mostra o preço do produto
        print(f'R${listagem[posicao]:>7.2f}')#[:>7] trata-se de 7 caracteres alinhados à direita preenchidos com o preço seguido de 2 pontos depois da vírgula
print('*'*40)




















