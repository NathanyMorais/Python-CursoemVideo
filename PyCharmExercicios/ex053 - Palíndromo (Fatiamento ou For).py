'''Crie um programa que leia uma frase qualquer e diga se ela é Palíndromo, desconsiderando os espaços:
Exs de palindromos = apos a sopa, a sacada da casa, a torre da derrota, o lobo ama o bolo, subi no onibus'''

print('\n','*'*5,'\033[36;4;1m','SERÁ QUE É PALÍNDROMO?','\033[m','*'*5)
#-----------------RESOLVENDO O PROBLEMA USANDO FATIAMENTO DE FORMA MAIS SIMPLES:----------------------------------------------
frase = str(input('Digite uma frase: ')).upper().strip() #vai transformar a frase toda em maiúscula e tirar os espaços que tiverem no inicio e fim
print(f'Frase que digitou = {frase}')
palavras = frase.split() #pega a frase e divide em palavras, desconsiderando os espaços internos
print(f'Palavras separadas = {palavras}')
palavrao = ''.join(palavras) #junta todas as palavras em uma só, formando um único palavrao - sem espaço
print(f'Palavras juntas = {palavrao}')
contrario = palavrao[::-1] #Fatiamento de string - identifica todas as letras (pois não especifiquei os índices[::]) com intervalo [-1] (Do fim para o início)
print(f'Frase ao Contrario = {contrario}')
if palavrao == contrario:
    print('A frase é um \033[32;1mPALÍNDROMO\033[m!, ou seja, é a mesma frase de trás para frente')
else:
    print('A frase \033[31;1mNÃO É UM PALÍNDROMO\033[m!')
print('\n')
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
#RESOLVENDO EXERCÍCIO DE FORMA MAIS COMPLEXA USANDO LAÇO DE REPETIÇÃO

frase = str(input('Digite uma frase: ')).upper().strip() #Função .strip() elimina os espaços em branco antes e depois da frase
palavras = frase.split() #Função .split() separa a frase em palavras e elimina os espaços internos
print(f'Você digitou: {palavras}')
junto = ''.join(palavras)  #Função .join() junta todas as palavras formando um conjunto só (uma palavra só)
                           #e o caractere [''] foi usado para todas as letras ficarem sem espaço entre elas
inverso = '' #variável inverso ainda vazia
for letra in range(len(junto)-1, -1, -1): #Intervalo da última letra [len(junto) -1] até a primeira letra que vai estar na posição 0, por isso usamos [-1], dando passo negativo [-1], ou seja, do fim para o começo
    #print(junto[letra], end=' ') #mostra a frase escrita de trás para frente
    inverso = inverso + junto[letra]
print(f'O inverso da frase {junto} é {inverso}')
if inverso == junto:
    print('A frase que digitou é um \033[32;1mPALÍNDROMO\033[m!')
else:
    print('A frase que digitou \033[31;1mNÃO É UM PALÍNDROMO\033[m!')






