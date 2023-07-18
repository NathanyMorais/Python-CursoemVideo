'''Crie um código em python que teste se o site Pudim está acessível pelo computador usado.'''

import urllib                 #importação da Biblioteca urllib
import urllib.request  #importação do módulo request que pertence a biblioteca urllib


try: #tratamento de erros - tente abrir o site abaixo
    site = urllib.request.urlopen("http://pudim.com.br/") #comando para a biblioteca acessar o URL
except (urllib.error.URLError): #principal erro que pode ocorrer caso esteja sem internet ou a URL esteja quebrada
    print('\n\033[1;31mErro na conexão com o site ou a URL não foi encontrada.\033[m')
else: #se o try funcionar, ou seja, se o site abrir, mostra a mensagem abaixo
    print('\n\033[1;34mConexão estabelecida com sucesso!\033[m')
    print('O código HTML desse site é: \n')
    print(f'{site.read()}') #o comando .read() mostra o código html do URL em questão








