#Funções para resolver a segunda parte do exercício

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
        print(f'\033[1;34mArquivo {nomedoarquivo} criado com sucesso!\033[m')

def lerArquivo(nomedoarquivo): #função para ler o arquivo txt
    try: #tente abrir o arquivo e ler o texto
        a = open(nomedoarquivo, 'rt')
    except: #se der qualquer erro, mostra a mensagem de erro
        print('\033[1;mHouve um erro na leitura do arquivo!\033[m')
    else: #se o try funcionar, mostra um relatório com cabeçalho e o conteúdo do arquivo
        cabeçalho('\033[1;36mPESSOAS CADASTRADAS\033[m')
        print(a.read()) #mostra o conteudo que está dentro do arquivo txt (ainda sem formatação)
#---------------------------------------------------------------------------------------------------------------------------------------------------

#Programa principal
arq = 'cadastrodepessoa.txt' #variável 'arq' recebe um arquivo de texto com o nome 'cadastro de pessoa'

''' CÓDIGO DE TESTE PARA VERIFICAR SE UM ARQUIVO EXISTE OU NÃO: (apenas teste, não entra no sistema principal)

if arquivoExiste(arq): #função 'arquivoExiste' para verificar se o 'cadastrodepessoa.txt' já está criado
    print('\nArquivo encontrado.')
else:
    print('\nArquivo não encontrado.')
    criarArquivo(arq)'''

if not arquivoExiste(arq): #caso o arquivo 'cadastrodepessoa.txt' não exista, crie um.
    criarArquivo(arq) #função para criar um arquivo