'''Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos.
 O programa encerra quando o usuario disser que quer mostrar 0 termos'''

n = 10
a1 = int(input('Digite o 1º termo: '))
r = int(input('Razão: '))
an = a1 + (n - 1) * r #formula para descobrir o termo geral, ou seja, o último termo da P.A
print(a1, end=' ') #imprime o 1º termo digitado pelo usuário, antes de entrar no laço de repetição
while a1 < an:    #Enquanto o termo for menor que o último número
     a1 = a1 + r
     print(a1, end=' ')
print('PAUSA')
t = 1
while t !=0: #[t] significa a qtde de termos a mais que o usuário poderá digitar
    t = int(input('\nDigite quantos termos a mais deseja mostrar: '))
    if t != 0:  #se t for diferente do número 0
        n = t    #o número de termos 'n' passa a valer 't', ou seja, a nova quantidade de termos que o usuário pediu
        an = a1 + (t - 1) * r ##formula para descobrir o último termo, agora usando o 't', que é a qtde de termos que o usuario digitou
        while a1 <= an:
            a1 = a1 + r
            print('\033[33;1m',a1,'\033[m',end=' ')
    else:
        print('\n\033[31;1mFIM\033[m')
#-------------------------------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------
primeiro = int(input('Primeiro valor: '))
razao = int(input('Razão da P.A: '))
termo = primeiro
cont = 1
total = 0 #total de termos a ser mostrado
mais = 10 #a principio deve ser mostrado 10 termos
while mais != 0: #Enquanto o usuario digitar qualquer valor diferente de 0
    total = total + mais
    while cont <= total:
        print(f'{termo}',end=' ')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA\n')
    mais = int(input('Quantos termos a mais quer mostrar? '))
print(f'Progressao aritmética encerrada com {total} termos\n')
