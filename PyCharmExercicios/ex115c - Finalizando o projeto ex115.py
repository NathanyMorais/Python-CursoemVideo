#Criação da função 'CADASTRAR()'
#Arrumando a função 'lerArquivo()' para mostrar um relatório formatado

def lerArquivo(nomedoarquivo): #função para ler o arquivo txt
    try: #tente abrir o arquivo e ler o texto
        a = open(nomedoarquivo, 'rt')
    except: #se der qualquer erro, mostra a mensagem de erro
        print('\033[1;mHouve um erro na leitura do arquivo!\033[m')
    else: #se o try funcionar, mostra um relatório com cabeçalho e o conteúdo do arquivo
        cabeçalho('\033[1;35mPESSOAS CADASTRADAS\033[m')
        #print(a.read())        #mostra o conteudo que está dentro do arquivo txt (ainda sem formatação)
        for linha in a: #para cada linha dentro do arquivo 'a' (chamei de 'a' no try)
            dado = linha.split(';') #dado se torna uma lista e cada linha vai ser separada por ';'.
            dado[1] = dado[1].replace('\n','') #para a lista dado na posição 1, ou seja, 'idade' - substitui a quebra de linha por vazio, para que não haja quebra de linha.
            print(f'{dado[0]:<30}{dado[1]:>3} anos')   #a quebra de linha foi usada durante o cadastro da pessoa, no comando: 'a.write(f'{nome};{idade}\n')'
           #mostra os dados formatados em forma de relatorio - dado[0] = nome e dado[1] = idade
    finally:
        a.close()

#Função criada no último vídeo do curso: ex115c - finalizando o projeto
def cadastrar(nomedoarquivo, nome='desconhecido', idade=0):
    try: #tente abrir o arquivo e adicionar novos elementos dentro dele
        a = open(nomedoarquivo, 'at') #'at' é 'append text' para adicionar elementos dentro do arquivo
    except: #se der qualquer erro, mostra a mensagem de erro
        print('\033[1;mHouve um erro na abertura do arquivo!\033[m')
    else:  #se o primeiro try funcionar e o arquivo abrir para receber novos elementos
        try: #tente escrever dentro do arquivo esses elementos
            a.write(f'{nome};{idade}\n') #função 'write' vai escrever dentro do arquivo
        except: #se der qualquer problema ao escrever os dados, mostra a mensagem de erro
            print('\033[1;mHouve um erro ao escrever os dados!\033[m')
        else: #se não der nenhum problema
            print(f'Novo cadastro de {nome} adicionado com sucesso.')
            a.close()

#-----------------------------------------------------------------------------------------------------------------------------
from biblioteca115.Interface import*  #O '*' significa que é pra importar tudo
from biblioteca115.arquivodecadastro import*
from time import sleep

#Sistema Principal
arq = 'cadastrodepessoa.txt' #variável 'arq' recebe um arquivo de texto com o nome 'cadastro de pessoa'

#esse comando foi executado apenas na primeira vez que rodei o programa. Ele mesmo cria o arquivo txt.
if not arquivoExiste(arq): #caso o arquivo 'cadastrodepessoa.txt' não exista, crie um.
    criarArquivo(arq) #função para criar um arquivo

while True:
    resposta = menu(['Relatório de pessoas cadastradas', 'Novo cadastro de pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq) #função para ler/mostrar o arquivo txt
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO') #funçao 'cabeçalho' para destacar o título 'novo cadastro'
        nome = str(input('Nome: ')) #insira o nome da pessoa
        idade = leiaInt('Idade: ') #insira a idade da pessoa - usando a funçao 'leiaInt' como um input
        cadastrar(arq, nome, idade) #funçao 'cadastrar' com os parametros indicados
    elif resposta == 3:
        cabeçalho('\033[1;32mPrograma encerrado!\033[m')
        break
    else:
        print('\033[31;1mErro! Digite uma opção válida.\033[m')
    sleep(1)
