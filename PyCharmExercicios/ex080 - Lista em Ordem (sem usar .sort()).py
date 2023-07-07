'''Crie um programa onde o usuario possa digitar 5 valores e armazene-os em uma lista
 JÁ NA POSIÇÃO CORRETA de inserção (sem usar o .sort()). Ao final, mostre a lista ordenada na tela'''

num = []
for c in range(0,5):
    n = (int(input('Digite um valor: ')))
    if c == 0: #se for a primeira posição, logo, é o primeiro numero digitado
        num.append(n) #inclui o numero na lista
        print('Adicionado ao final da lista...')
    elif n > num[- 1]: #se o numero digitado for maior do que o último valor da lista num[- 1], ele será então o último número
        num.append(n) #inclui o numero na lista
        print('Adicionado ao final da lista...')
    else: #agora faço a lógica para verificar os números que ficam no meio da lista
      posiçao = 0
      while posiçao < len(num): #Vai varrer toda a lista, do primeiro numero na posição 0 até o último número
          if n <= num[posiçao]: #se o numero digitado for menor ou igual ao número da lista naquela posição (começando na posição 0)
              num.insert(posiçao, n) #.insert() adiciona o número n digitado na posição que estiver testando (começa na posição 0 e percorre toda a lista)
              print(f'Adicionado na posição {posiçao} da lista.')
              break
          posiçao = posiçao + 1 #contador para ir percorrendo todas as posições da lista
print('-'*50)
print(f'Os números digitados em ordem foram: {num}.')


















