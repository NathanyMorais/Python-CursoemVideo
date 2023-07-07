'''Faça um programa que leia o nome completo de uma pessoa e
 em seguida mostre o primeiro e último nome separadamente'''

n = str(input('Digite o seu nome completo: ')).strip().title()
nome = n.split()
print(f'Seu nome é: \033[1;36m{n.title()}\033[m')
print(f'Seu primeiro nome é \033[33m{nome[0]}\033[m')
print(f'Seu último nome é \033[35m{nome[-1]}\033[m ')
# o [-1] pode ser utilizado para se referir ao último objeto de uma lista, assim como [-2] seria a penúltima e assim por diante.
print(f'Seu nome completo tem \033[4m{len(n) - n.count(" ")} letras\033[m')
print(f'Seu nome em maiúsculas é \033[1;40m{n.upper()}\033[m')
print(f'Seu nome em minúsculas é \033[7;40m{n.lower()}\033[m')
