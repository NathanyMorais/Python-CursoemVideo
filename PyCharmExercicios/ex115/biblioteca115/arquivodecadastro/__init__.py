#Módulo arquivo de cadastro

from biblioteca115.Interface import cabeçalho #importando a função 'cabeçalho' do módulo Interface

def arquivoExiste(nomedoarquivo): #função para verificar se um arquivo existe ou não
    try: #tente abrir o arquivo e fechar logo em seguida
        a = open(nomedoarquivo, 'rt') #função 'open' usada para abrir o arquivo. Recebe 2 parâmetros:
        a.close()                     #parametro 'nome do arquivo' e parametro 'rt' para ler o arquivo, ou seja 'read text'

    except FileNotFoundError: #se der erro de arquivo não encontrado
        return False #retorne falso, pois o arquivo não existe
    else: #caso o try funcione
        return True #retorne verdadeiro, pois o arquivo existe e foi aberto e fechado

def criarArquivo(nomedoarquivo): #função para criar um arquivo
    try: #tente criar o arquivo e fechar logo em seguida
        a = open(nomedoarquivo, 'wt+') #função 'open' com 2 parametros, sendo 'wt+' para escrever o arquivo em txt
        a.close()                      #'wt' é 'write text' e o simbolo '+' é usado criar um arquivo txt caso ele não exista
    except: #se der qualquer erro, mostra a mensagem de erro
        print('\033[1;mHouve um erro na criação do arquivo!\033[m')
    else: #se o try funcionar, mostra a mensagem de sucesso
        print(f'\033[1;33mArquivo {nomedoarquivo} criado com sucesso!\033[m')

def lerArquivo(nomedoarquivo): #função para ler o arquivo txt
    try: #tente abrir o arquivo e ler o texto
        a = open(nomedoarquivo, 'rt')
    except: #se der qualquer erro, mostra a mensagem de erro
        print('\033[1;mHouve um erro na leitura do arquivo!\033[m')
    else: #se o try funcionar, mostra um relatório com cabeçalho e o conteúdo do arquivo
        cabeçalho('PESSOAS CADASTRADAS')
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