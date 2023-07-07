dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
chaves_ordenadas = sorted(dicionario.keys(), reverse=True)
for chave in chaves_ordenadas:
    print(chave, dicionario[chave])

dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}
chaves_ordenadas = sorted(dicionario.keys())
for chave in chaves_ordenadas:
    print(chave, dicionario[chave])

dict = {'cachorro': 2, 'papagaio': 3, 'elefante': 1}
print(sorted(dict)) #--> ['cachorro', 'elefante', 'papagaio'] ordenado de acordo com a 1ª letra de cada chave

dict = {'cachorro': 2, 'papagaio': 3, 'elefante': 1}
for v in sorted(dict, key=dict.get):
    print(v, dict[v])






