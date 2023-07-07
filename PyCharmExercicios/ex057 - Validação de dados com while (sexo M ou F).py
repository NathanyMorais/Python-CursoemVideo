'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F".
 Caso esteja errado, peça a digitação novamente até obter o valor correto'''

sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0] #[0] vai considerar apenas a posição da primeira letra (para validar M ou F)
while sexo not in 'MF': #enquanto 'sexo' não estiver em 'MF'
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')





