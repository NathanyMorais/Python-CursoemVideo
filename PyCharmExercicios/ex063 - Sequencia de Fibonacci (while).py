'''Escreva um programa que leia um número N inteiro qualquer e mostre na tela
 os N primeiros elementos de uma Sequencia de Fibonacci.
 EX: 0->1->1->2->3->5->8'''

print('\n','\033[31;1m','-'*5,'Sequência de Fibonacci','-'*5,'\033[m')
n = int(input('Quantos termos deseja mostrar? '))
t1 = 0 #primeiro termo da sequencia fibonacci
t2 = 1 #segundo termo da sequencia fibonacci
print(f'{t1} - {t2} -', end=' ')
cont = 3 #contador iniciando no 3, pois já defini o 1º e 2º termo
while cont <= n: #enquanto o contador for menor ou igual ao número de termos que o usuario quer mostrar:
    t3 = t1 + t2 #terceiro termo é igual a soma dos dois números anteriores
    print(f'{t3} -', end=' ')
    t1 = t2 #após calcular o terceiro termo uma vez, o t1 passa a ser t2 enquanto o t2 passa a ser o t3.
    t2 = t3 #dessa forma a sequencia vai caminhando e somando os números anteriores corretamente
    cont = cont + 1
print('FIM')
#-----------------------------SOLUÇÃO USANDO O LAÇO 'FOR'---------------------------------------------------------------
n = int(input('Quantos termos quer mostrar? '))
t1 = 0
t2 = 1
print(f'{t1}, {t2}, ', end='')
termo = 0
for termo in range(n-2): #intervalo da qtde de termos que o usuario quer Menos os 2 termos já definidos (t1 e t2)
    t3 = t1 + t2
    print(f'{t3}, ', end='')
    t1 = t2
    t2 = t3
    termo = termo + 1
print(' FIM')

