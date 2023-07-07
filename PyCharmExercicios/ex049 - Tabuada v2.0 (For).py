'''Refaça o desafio 009 mostrando a TABUADA de um número que o usuário digitar, porém usando o laço de repetição FOR'''


n = int(input('Digite um número: '))
print(f'\n','\033[36;1;4m','-'*5,'TABUADA','-'*5,'\033[m')
for c in range(1,10+1):  #Laço para percorrer do número 1 ao 10
    print(f'{n} X {c:2} = {n*c}') #Uso [:2] para alinhar os números na tabuada