'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar
quando o usuario digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS números
foram digitados e qual foi a SOMA entre eles.(desconsiderando o flag = 999)'''

n = cont = soma = 0  #São 3 variáveis distintas [n, cont e soma] que possuem o mesmo valor, por isso podem ser escritas dessa forma
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    if n != 999: #condição para que o flag(condição de parada) não seja considerado pelo contador e pelo acumulador
        cont += 1 #contador para somar a quantidade de números digitados
        soma += n #acumulador para somar os números que forem digitados
print(f'Você digitou \033[31;1m{cont}\033[m números e a soma deles foi \033[34;1m{soma}\033[m.')