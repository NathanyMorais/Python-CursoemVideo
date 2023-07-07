'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final mostre:
- Média de idade
- Nome do homem mais velho
- Quantas mulheres tem menos de 20 anos'''

soma_idade = 0 #acumulador para ir somando as idades
idade_velho = 0 #variável int vazia para idade do homem mais velho
nome_velho = '' #variavel string vazia para nome do homem mais velho
cont_mulher20 = 0 #variavel int vazia para fazer a contagem de quantas mulheres tem menos de 20 anos
for p in range(1,5):
    print(f'------ {p}ªPESSOA -----')
    n = str(input('Nome: ')).strip().upper()
    i = int(input('Idade: '))
    s = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade = soma_idade + i #soma das idades que estão sendo digitadas
    if p == 1 and s == 'M': #condição para que o primeiro seja mais velho se for Masculino
        idade_velho = i
        nome_velho = n
    if s == 'M' and i > idade_velho: #comparação a partir dos outros dados, se sexo for masculino e se a idade for maior que a anterior (apenas do sexo masculino)
        idade_velho = i
        nome_velho = n
    if s == 'F' and i < 20: #se o sexo for Feminino e a idade for abaixo de 20 anos
        cont_mulher20 = cont_mulher20 + 1 #contador que conta quantas mulheres tem menos de 20 anos
media_idade = soma_idade / 4 #Calculo da média entre as idades digitadas
print(f'A média de idade do grupo é de \033[32;1m{media_idade:.0f} anos\033[m.')
print(f'O homem mais velho se chama \033[31;4m{nome_velho} e tem {idade_velho} anos\033[m.')
print(f'Ao todo são \033[33m{cont_mulher20} mulheres com menos de 20 anos\033[m.')
