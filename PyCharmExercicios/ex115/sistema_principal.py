from biblioteca115.Interface import*  #O '*' significa que é pra importar tudo
from biblioteca115.arquivodecadastro import*
from time import sleep

arq = 'cadastrodepessoa.txt' #variável 'arq' recebe um arquivo de texto com o nome 'cadastro de pessoa'

'''CÓDIGO DE TESTE PARA VERIFICAR SE UM ARQUIVO EXISTE OU NÃO: (apenas teste, não entra no sistema principal)

if arquivoExiste(arq): #função 'arquivoExiste' para verificar se o 'cadastrodepessoa.txt' já está criado
    print('\nArquivo encontrado.')
else:
    print('\nArquivo não encontrado.')
    criarArquivo(arq)'''

#esse comando foi executado apenas na primeira vez que rodei o programa. Ele mesmo criou o arquivo txt dentro do diretório ex115.
if not arquivoExiste(arq): #caso o arquivo 'cadastrodepessoa.txt' não exista, crie um.
    criarArquivo(arq) #função para criar um arquivo

while True:
    resposta = menu(['Relatório de pessoas cadastradas', 'Novo cadastro de pessoa', 'Sair do sistema']) #função 'menu' recebe uma lista como parametro
    if resposta == 1: #se o usuario digitar 1
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq) #função para ler/mostrar o arquivo txt
    elif resposta == 2: #se o usuario digitar 2
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO') #funçao 'cabeçalho' para destacar o novo cadastro
        nome = str(input('Nome: ')) #insira o nome da pessoa
        idade = leiaInt('Idade: ') #insira a idade da pessoa - usando a funçao 'leiaInt' como um input
        cadastrar(arq, nome, idade) #funçao 'cadastrar' com os parametros indicados
    elif resposta == 3: #se o usuario digitar 3
        cabeçalho('Programa encerrado!')
        break
    else: #se o usuario digitar uma opção que não exista no menu, mostra a mensagem de erro
        print('\033[31;1mErro! Digite uma opção válida.\033[m')
    sleep(1)


