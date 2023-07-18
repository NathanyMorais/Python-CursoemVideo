
#Função criada para o exercicio 112 - Validando a entrada de dados

#-------------------------SOLUÇÃO DO PROFESSOR------------------------------------------------------------------------
def leiaDinheiro(msg):
    válido = False #variável 'VÁLIDO' tem por padrão o valor 'False'
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip() #O comando [.replace] vai converter qualquer virgula em ponto e o comando [.strip] vai excluir os espaços caso sejam digitados
        if entrada.isalpha() or entrada == '': #se na entrada for digitado caracteres do alfabeto OU se não for digitado nada e estiver vazio ('')
            print(f'\033[31;1mErro! "{entrada}" é um preço inválido.\033[m') #O programa não aceita e acusa o erro
        else:
            válido = True
            return float(entrada)

