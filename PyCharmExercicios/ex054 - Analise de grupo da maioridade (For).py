'''Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas ainda não atingiram a maioridade
 e quantas já são maiores.'''

from datetime import date
contmaior = 0 #contador usado na contagem de quantos são maiores
contmenor = 0 #contador usado na contagem de quantos são menores
atual = date.today().year #considera o ano atual
for c in range(1,8): #laço de repetição contando de 1 ao 7
    ano = int(input(f'Ano em que a {c}ª pessoa nasceu: '))
    idade = atual - ano #descobre a idade do usuário
    if idade >= 21:
        contmaior += 1   #Se tiver idade maior ou igual a 21 anos, entra na contagem de maior de idade
    else:
        contmenor = contmenor + 1 #Se tiver idade menor que 21 anos, entra na contagem de menor de idade
print(f'Ao todo, {contmaior} pessoas já atingiram a maioridade e {contmenor} pessoas ainda são menores de idade.')
print('-------------------------------------\n')

#------RESOLUÇÃO COM INFORMAÇÃO EXTRA:----------------------------------------------
cont_maior = 0
cont_menor = 0
maisvelho = 0
atual = 2023
for p in range(1, 4):  # Faixa com 3 pessoas
    ano = int(input(f'Ano que nasceu pessoa {p}: '))
    idade = atual - ano
    if p == 1:          #condição que considera que o primeiro ano digitado é o mais velho
        maisvelho = ano
    else:
        if ano < maisvelho: #condição que compara os demais anos e pega o menor ano (que consequentemente será o mais velho)
            maisvelho = ano
    if idade >= 18:
        cont_maior += 1  #contador de quantos são maiores de 18 anos
    else:
        cont_menor += 1  # contador de quantos são menores de 18 anos
print(f'Um total de {cont_maior} são maiores de 18, enquanto {cont_menor} ainda são menores de idade')
print(f'O mais velho do grupo nasceu em {maisvelho} e tem {atual-maisvelho} anos.')
