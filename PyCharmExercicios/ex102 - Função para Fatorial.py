'''Crie um programa que tenha uma função FATORIAL() que receba dois parametros: o primeiro que indique o numero
a calcular e o outro, chamado show, que será o valor lógico (opcional) indicando se será mostrado ou não na tela
o processo de cálculo do fatorial'''

def fatorial(n,show=False):
    """
    -> Calcula o fatorial de um número
    :param n: indica o número a ser calculado
    :param show: (opcional) mostrar ou não a conta
    :return: o valor fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1): #laço for para percorrer todos os dígitos do fatorial (inicia no n° que o usuário digitar, termina no 0, passo de -1 em -1)
        if show: #se o usuário atribuir valor para 'show'
            print(c , end='') #então será mostrada toda a conta do fatorial
            if c > 1: #se o índice for maior que 1, segue com o sinal de vezes: 'x'
                print(f' x ', end='')
            else: #se o índice for igual ou menor que 1, segue com o sinal de igual: '=' e finaliza com o resultado da multiplicação (return f)
                print(' = ', end='')
        f = f * c #faz a conta do fatorial
    return f #retorna apenas o resultado da conta

#Programa principal
print(fatorial(5, True))
print(fatorial(7, True))
print(fatorial(7, False))
print(fatorial(5))
help(fatorial)







