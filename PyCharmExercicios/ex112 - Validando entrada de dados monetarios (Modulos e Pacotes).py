'''Dentro do pacote 'pacote_ex111' criado no desafio anterior, temos um modulo chamado dado.
Crie uma FUNÇÃO chamada leiaDinheiro() que seja capaz de funcionar como a função 'input()' mas com uma validação
de dados, para que aceite apenas valores que sejam monetários.'''

from pacote_ex111 import modulo_dado, modulo_moeda
#Do pacote 'pacote_ex111' importe os módulos 'modulo_dado' e 'modulo_moeda'

#Programa principal
p = modulo_dado.leiaDinheiro('Digite o preço: R$ ')
modulo_moeda.resumo(p, 80, 35)

''' Função leiaDinheiro() do meu módulo_dado (modulo que está dentro do pacote_ex111):

def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip() #O comando [.replace] vai converter qualquer virgula em ponto e o comando [.strip] vai excluir os espaços caso sejam digitados
        if entrada.isalpha() or entrada == '': #se na entrada for digitado um valor alfa OU se não for digitado nada e estiver vazio ('')
            print(f'\033[31;1mErro! "{entrada}" é um preço inválido.\033[m') #O programa não aceita e acusa o erro
        else:
            válido = True
            return float(entrada)
'''



