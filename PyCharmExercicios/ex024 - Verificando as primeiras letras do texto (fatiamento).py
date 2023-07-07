'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome (Santo)'''

nome = (input('Digite o nome de uma cidade: ')).strip().lower()
city = nome[0:5] == 'santo' #significa que no nome da cidade, na posição de 0 a 4 (exclui o último índice) as letras devem ser iguais a "santo"
print(f'A cidade começa com "Santo"? {city}')












