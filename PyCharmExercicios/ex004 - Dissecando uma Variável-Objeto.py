# Faça um programa que leia algo pelo teclado e mostre na tela:
# o seu tipo primitivo e todas as informações possiveis sobre ele
a = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(a))
print('Só tem espaços?', a.isspace())
print('É numérico?', a.isnumeric())
print('É afabético?', a.isalpha())
print('É alfanumérico?', a.isalnum())
print('Está em maiúsculas?', a.isupper())
print('Está em minúsculas?', a.islower())
print('Está capitalizada, ou seja, com maiúsculas e minúsculas?', a.istitle())

# Nesse tipo de situação a "variável" 'a' na verdade é um OBJETO.
# Todo objeto tem características e realiza funcionalidades, tendo atributos e métodos ('x.is...algo')