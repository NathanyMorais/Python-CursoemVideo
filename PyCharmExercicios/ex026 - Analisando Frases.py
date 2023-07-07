'''Faça um programa que leia uma frase pelo teclado e mostre
1- Quantas vezes aparece a letra A
2- Em que posição ela aparece a primeira vez
3- Em que posição ela aparece a última vez'''

n = str(input('Digite uma frase: ')).strip()
frase = n.upper()
letra = frase.count('A')
primeira = frase.find('A')+1
ultima = frase.rfind('A')+1 #começa a procurar a letra pelo lado direito
print(f'Sua frase possui {letra} letras "A"')
print(f'A letra "A" aparece pela primeira vez na posição {primeira}')
print(f'A letra "A" aparece pela última vez na posição {ultima}')







