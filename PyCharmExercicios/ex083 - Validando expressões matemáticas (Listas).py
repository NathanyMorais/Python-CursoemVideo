'''Crie um programa onde o usuario digite uma expressao matematica que use PARENTESES. Seu aplicativo
 devera analisar se a expressao passada está com os parenteses abertos e fechados na ordem correta.'''

#-----------------------SOLUÇÃO DO PROFESSOR---------------------------------------------------------------------------
expressao = str(input('Digite a expressão: '))
pilha = [] #lista vazia
for simbolo in expressao: #vai analisar cada um dos símbolos da expressao
    if simbolo == '(': #se o símbolo for igual ao um parenteses abrindo
        pilha.append('(') #o parentese abrindo é incluído na lista 'pilha'
    elif simbolo == ')': #se o símbolo for igual ao um parenteses fechando
        if len(pilha) > 0: #se o comprimento da pilha for maior que zero, significa que a lista não está vazia
            pilha.pop() #.pop() remove o último elemento da lista
        else: #se a pilha estiver vazia
            pilha.append(')') #o parentese fechando é incluido na pilha,
            break             #dando sinal de que existem mais parenteses fechando do que abrindo
if len(pilha) == 0: #se o comprimento da lista é igual a 0, é sinal que cada parentese que abriu teve seu par fechando
    print('Sua expressão está válida.')
elif len(pilha) > 0: #se o comprimento da lista foi maior que zero, é sinal que tem parenteses sobrando na expressão
    print('Sua expressão está errada.')

'''Na prática o programa faz o seguinte:
Ao percorrer a expressão digitada pelo usuário, toda vez que encontra o símbolo parentese aberto "(",
o mesmo é incluído numa lista chamada pillha.
E toda vez que encontra um parentese fechado ")", o parentese aberto que estava na pilha é excluído, 
como se o par de parenteses fosse formado e excluído.
Logo, se ao percorrer toda a expressão tiver sobrado algum símbolo de parentese na pilha, 
significa que este foi digitado a mais, e por isso a expressão matemática está errada.'''










