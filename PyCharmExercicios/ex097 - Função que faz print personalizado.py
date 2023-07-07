'''Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre
uma mensagem com tamanho adaptável.
Ex:          escreva(‘Olá, Mundo!’)
Saída:          ~~~~~~~~~
                Olá, Mundo!
                 ~~~~~~~~~
'''
def escreva(texto):
    tamanho = len(texto) + 4 #Tamanho é o tamanho do texto com mais 4 caracteres
    print('~' * tamanho)
    print(f'  {texto}') #o texto tem espaçamento de 2 caracteres para ficar sempre centralizado entre os '~~~~'
    print('~' * tamanho)

#Código principal
n = str(input('Digite um texto: '))
escreva(n)
escreva('CURSO EM VÍDEO')
escreva('Olá, Mundo!')
escreva('Nathany Kássia Morais')




















