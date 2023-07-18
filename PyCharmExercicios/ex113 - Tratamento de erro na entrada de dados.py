'''Reescreva a função leiaInt() que fizemos no ex 104, incluindo agora a possibilidade da digitação de um
numero de tipo invalido. Aproveite e crie tambem uma função leiaFloat() com a mesma funcionalidade.'''

def leiaInt(msg): #função leiaInt (vai funcionar como input e por isso recebe uma mensagem)
    while True: #loop infinito
        try: #tratamento de erros - tente fazer a operação abaixo
            num = int(input(msg)) #variavel 'num' deve receber um número inteiro digitado pelo usuario
        except (ValueError, TypeError): #se ocorrer algumas dessas exceções, o programa mostra a mensagem de erro
            print(f'\033[1;33mErro! Por favor, digite um número Inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt): #se ocorrer essa exceção, o programa mostra a mensagem referente a interrupção
            print(f'\n\033[1;33mPrograma interrompido pelo usuário.\033[m')
            return 0 #e retorna com um valor padrão, no caso, o zero
        else: #caso o try funcione corretamente o programa retorna com o numero inteiro digitado pelo usuario
            return num

def leiaFloat(msg): #função leiaFloat que vai funcionar como input
    while True: #loop infinito
        try:  #tratamento de erros - tente fazer a operação abaixo
            num = str(input(msg)).replace(',','.') #variavel 'num' tratada como string apenas para que a virgula seja aceita e substituida por ponto caso o usuario a digite
            real = float(num) #a variavel 'real' transforma o numero que for digitado em numero real
        except (ValueError, TypeError): #se ocorrer algumas dessas exceções, o programa mostra a mensagem de erro
            print(f'\033[1;31mErro! Por favor, digite um número Real válido.\033[m')
            continue
        except (KeyboardInterrupt): #se ocorrer essa exceção, o programa mostra a mensagem referente a interrupção
            print(f'\n\033[1;31mPrograma interrompido pelo usuário.')
            return 0 #e retorna com um valor padrão, no caso, o zero
        else:  #caso o try funcione corretamente o programa retorna com o numero Real digitado pelo usuario
            return real

#Programa principal
inteiro = leiaInt('Digite um  número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}.')















