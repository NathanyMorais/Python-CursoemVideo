'''Crie um programa que leia o nome completo de uma pessoa e mostre:
1- O nome com todas as letras maiúsculas
2- O nome com todas as letras minúsculas
3- Quantas letras ao todo (sem considerar os espaços)
4- Quantas letras tem o primeiro nome'''

nome = str(input('Nome completo: ')).strip()
print(f'Seu nome em maiúsculas é {nome.upper()}') #1
print(f'Seu nome em minúsculas é {nome.lower()}') #2
print(f'Seu nome completo tem {len(nome)-nome.count(" ")} letras') #3 Conta a quantidade total de caracteres MENOS(-) a quantidade de espaços
dividido = nome.split() #4
print(f'O primeiro nome tem {len(dividido[0])} letras')