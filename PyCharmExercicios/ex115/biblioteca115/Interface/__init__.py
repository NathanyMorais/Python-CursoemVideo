#Módulo Interface

#Função leiaInt copiada do ex104
def leiaInt(msg): #função 'leiaInt' recebe uma mensagem como parâmetro
    ok = False #variável 'ok' tem como padrão o valor - falso
    número = 0 #variável 'numero' inicia em zero
    while True:
        n = str(input(msg)) #variável 'n' vai receber o valor que o usuário digitar em forma de string
        if n.isnumeric(): #se o usuario digitar apenas números na entrada
            número = int(n) #a variável 'número' vai receber o valor digitado como sendo um nº inteiro (já que no input está como string)
            ok = True #e a variavel 'ok' passa a ser verdadeira
        else: #se o usuario digitar qualquer caracter que não seja numérico
            print('\033[31;1mErro! Digite uma opção válida.\033[m') #recebe a mensagem de erro
        if ok: #se ok for verdadeiro
            break #o programa encerra e retorna com o valor digitado
    return número #retorna com o valor 'n' que foi digitado

def linha(tam = 42): #função 'linha' para fazer o tracejado, recebe o parametro 'tamanho' e tem valor 42 como padrão
    return '-' * tam

def cabeçalho(txt): #função 'cabeçalho' para fazer título/cabeçalho
    print(linha()) #utilização da função linha para fazer os tracejados
    print(txt.center(42)) #texto alinhado no centro - considerando o tamanho padrão da linha (42)
    print(linha())

def menu(lista):    #função 'menu' para fazer o menu principal do sistema
    cabeçalho('MENU PRINCIPAL') #utilização da funçao cabeçalho para destacar o titulo do menu
    cont = 1 #contador iniciando em 1 para fazer a contagem de intens da lista
    for item in lista: #para cada item da lista (já que a função menu recebe uma lista como parametro)
        print(f'\033[1;33m{cont}\033[m - \033[1;34m{item}\033[m') #mostra o número do contador seguido do item da lista que estiver na posição do contador
        cont += 1 #contador + 1 para cada volta no laço 'For'
    print(linha()) #utilização da função linha
    opcao = leiaInt('\033[1;33mSua opção: \033[m') #utilização da função 'leiaInt' para o usuario digitar a opção do menu
    return opcao


