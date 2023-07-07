'''Crie um programa que leia o nome e preço de varios produtos. O programa deverá perguntar se o usuario quer ou nao
continuar. No final, mostre:
a)Qual o total gasto na compra
b)Quantos produtos custam mais de R$1000
c)Qual o nome do produto mais barato'''

print('\n\033[34;1;4m','='*10,'MERCADÃO','='*10, '\033[m')
soma = cont = caro = barato = 0
nome_prod = ''
while True:
    print('\033[33m-----CADASTRO DE PRODUTO-----\033[m')
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    c = ' ' #string vazia para receber a resposta 'sim ou nao'
    while c not in 'SN': #laço para que o programa funcione APENAS se for digitado S ou N
        c = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    soma = soma + preço #soma dos preços dos produtos
    cont = cont + 1 #conta quantos produtos estao sendo cadastrados - resposta letra A
    if preço > 1000:
        caro += 1 #contador de quantos custam mais de 1000 - resposta letra B
    if cont == 1: #assume que na primeira volta o produto registrado é o mais barato
        barato = preço
        nome_prod = nome
    else: #compara os produtos cadastrados nas demais voltas do loop
        if preço < barato: #testa o produto mais barato e armazena o preço e nome dele - resposta letra C
            barato = preço
            nome_prod = nome
    '''Essa última estrutura (if-else) também pode ser simplificada em um único IF pois os comandos são iguais. Dessa forma:
    if cont == 1 OR preço < barato:
        barato = preço
        nome_prod = nome'''
    if c == 'N': #Se digitado 'N' o programa é interrompido
        break #comando de parada
print('\033[35;1m='*10,'RELATÓRIO FINAL','='*10,'\033[m')
print(f'\033[30;107mValor total dos produtos = R$ {soma:.2f}\033[m')
print(f'\033[30;107mTotal de {caro} produtos custaram mais de R$1000,00\033[m')
print(f'\033[30;107mO produto mais barato foi {nome_prod} no valor de R$ {barato:.2f}\033[m')

