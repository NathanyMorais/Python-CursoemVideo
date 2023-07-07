'''Crie um programa que tenha a função leiaInt(), que deve funcionar como a função input(), só que fazendo a validação para aceitar apenas um
 valor numérico.'''
def leiaInt(msg): #função 'leiaInt' recebe uma mensagem como parâmetro
    ok = False #variável 'ok' tem como padrão o valor - falso
    número = 0 #variável 'valor' inicia em zero
    while True:
        n = str(input(msg)) #variável 'n' vai receber o valor que o usuário digitar em forma de string
        if n.isnumeric(): #se o usuario digitar apenas números na entrada
            número = int(n) #a variável 'número' vai receber o valor digitado como sendo um nº inteiro (já que no input está como string)
            ok = True #e a variavel 'ok' passa a ser verdadeira
        else: #se o usuario digitar qualquer caracter que não seja numérico
            print('\033[31;1mErro! Digite um número inteiro válido.\033[m') #recebe a mensagem de erro
        if ok: #se ok for verdadeiro
            break #o programa encerra e retorna com o valor digitado
    return número #retorna com o valor 'n' que foi digitado

#Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')





