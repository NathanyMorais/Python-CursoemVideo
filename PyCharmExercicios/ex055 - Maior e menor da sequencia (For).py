'''Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e
o menor peso lidos.'''

#Minha solução: (só funciona pois tenho uma faixa de pessoas específica - 5 pessoas. Caso contrário, seria melhor a outra solução.)
print('\n','-'*5,'\033[37;1;40mMAIOR E MENOR\033[m','-'*5)
lista = [] #a variavel lista será usada para armazenar os valores digitados dentro dela
for c in range (1,6):
    n = float(input(f'Peso da {c}ª pessoa: '))
    lista.append(n) #Função .append() para adicionar os valores dentro da variavel lista
    lista.sort(reverse=True) #Função .sort() para colocar os valores em ordem e 'reverse=True' para decrescente - do Maior para o Menor
print(lista)
print(f'O maior peso lido foi {lista[0]}Kg e o menor peso lido foi {lista[4]}kg')

#-------OUTRA SOLUÇÃO (do professor)----------------------------------------------------------------------------------------------------
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:   #Se o peso lido for igual a 1, no caso, o primeiro peso lido vai ser tanto o maior quanto o menor pois ainda não houve comparação.
        maior = peso
        menor = peso
    else:        #A partir do segundo peso lido, já pode haver comparação entre os valores e decisão de quem é maior e quem é menor
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')













