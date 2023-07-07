#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessároa para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2m².
alt = input('Altura da parede: ')
larg = input('Largura da parede: ')
area = float(alt) * float(larg)
print(f'Área da parede é de {area} m².')
print(f'Será necessário {area/2} litros de tinta para pintá-la.')