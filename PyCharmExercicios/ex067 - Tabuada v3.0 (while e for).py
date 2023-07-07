'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuario. O programa será interrompido quando o número solicitado for negativo'''

print('\n','\033[32;1m','*'*10,'TABUADA','*'*10,'\033[m')
c = 0 #contador usado para percorrer a tabuada
while True:
    n = int(input('\n\033[34mDigite o número: \033[m'))
    if n < 0: #se for digitado número menor que 0, ou seja, número negativo
        break #o programa é interrompido pelo comando break
    for c in range (1,10+1): #laço que percorre a tabuada
        print(f'{n} x {c:2} = {n*c}')
    print('-'*30)
print(f'\n\033[31mPrograma TABUADA encerrado. Volte sempre!\033[m')
