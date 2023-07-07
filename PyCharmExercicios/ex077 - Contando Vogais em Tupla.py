'''Crie um programa que tenha uma tupla com varias palavras (sem acentos).
Em seguida, mostrar, para cada palavra, quais são suas vogais'''

#------------------SOLUÇÃO DO PROFESSOR-------------------------------------
tupla = ('aprender','programar','linguagem','python','curso','gratis',
            'estudar','praticar','trabalhar','mercado','programador','futuro')
for palavra in tupla: # para cada palavra na tupla:
    print(f'\nNa palavra \033[34;1m{palavra.upper()}\033[m temos as vogais ', end='')
    for letra in palavra: #para cada letra na palavra (já que cada palavra é uma lista de letras)
        if letra.lower() in 'aeiou':
            print('\033[32;1m',letra.upper(),'\033[m' ,end=' ')





