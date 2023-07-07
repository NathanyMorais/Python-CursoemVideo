'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''

dados = {}
ficha = []
media = soma = 0
while True:
    dados.clear() #limpa os dados sempre que volta para o inicio do loop para que cadastre uma nova pessoa
    dados['Nome'] = str(input('Nome: '))
    while True: #laço para fazer a validação de F ou M
        dados['Sexo'] = str(input('Sexo [F/M]: ')).upper()[0]
        if dados['Sexo'] in 'FM': #O usuário precisa digitar F ou M para que o programa saia do loop infinito e continue
            break
        print('Erro! Digite apenas M ou F.') #Se digitar uma letra errada o programa permanece no loop infinito
    dados['Idade'] = int(input('Idade: '))
    soma = soma + dados['Idade'] #soma de todas as idades que forem cadatsradas
    ficha.append(dados.copy()) #Adiciona uma cópia dos dados na lista 'ficha'
    while True: #laço para fazer a validação de S ou N
        r = str(input('Quer continuar? [S/N] ')).upper()[0]
        if r in 'SN': #O usuário precisa digitar S ou N para que o programa saia do loop infinito e continue
            break
        print('Erro! Digite apenas S ou N.') #Se digitar uma letra errada o programa permanece no loop infinito
    if r == 'N': #Se digitar a letra 'N' o programa interrompe
        break
print(ficha)
print('='*50)
print(f'A) O grupo tem {len(ficha)} pessoas cadastradas.') #comando len() mostra a quantidade de elementos que tem na lista 'ficha'
media = soma/len(ficha) #calculo da média de idade do grupo
print(f'B) A média de idade do grupo é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')
for pessoa in ficha: #laço para percorrer a Lista 'ficha'
    if pessoa['Sexo'] == 'F': #Se o valor para a chave 'sexo' for F
       print(f'{pessoa["Nome"]} ', end='') #mostra o nome da pessoa (ou seja, mostra o valor que está na chave 'nome')
print()
print(f'D) Lista de pessoas que estão acima da média: ')
for pessoa in ficha: #laço para percorrer a lista novamente
    if pessoa['Idade'] >= media: #se o valor que estiver na chave 'Idade' for maior que a média que foi calculada
        for k, v in pessoa.items(): #laço que percorre cada chave e valor do dicionário
            print(f' {k} = {v}', end=' ') #mostra a chave e o valor apenas das pessoas que tiverem idade acima da média
        print()
print('='*50)
print('<<< ENCERRANDO >>>')






















































