'''Crie um programa que simule o funcionamento de um caixa eletronico. No inicio pergunte ao usuario qual valor será
sacado (numero inteiro) e o programa vai informar quantas cédulas de cada valor serao entregues.
- Considere que o caixa possui cédulas de 50, 20, 10 e 1 real.'''

print('\n\033[35;1m','=-='*3,'CAIXA ELETRÔNICO','=-='*3,' \033[m')
num = int(input('Digite o valor que deseja sacar: R$'))
cinq = int(num / 50)
vin = int((num - (cinq * 50))/20)
dez = int((num - (cinq * 50) - (vin * 20))/10)
uni = int((num - (cinq * 50) - (vin * 20) - (dez * 10))/1)
print('='*40)
print(f'Total de {cinq} cédulas de R$50')
print(f'Total de {vin} cédulas de R$20')
print(f'Total de {dez} cédulas de R$10')
print(f'Total de {uni} cédulas de R$1')
print('='*40)
print(f'\nVolte sempre!')

#-------------------SOLUÇÃO DO PROFESSOR--------------------------------------------------------------------------------
'''A logica é pegar o montante que quer sacar e ir subtraindo as notas até não dar mais, 
começando das maiores cédulas até as menores:'''

valor = int(input('Que valor você quer sacar? R$'))
montante = valor #o montante é o tanto que quer sacar
cedula_atual = 50 #considera a cédula de maior valor
totalced = 0 #variável para saber o total de cédulas de uma determinada cédula
while True: #o loop vai ser infinito enquanto o montante não for igual a zero
    if montante >= cedula_atual: #se o valor que quero sacar for maior que a cedula atual (ou seja, a qtde de cédulas que pode ser retirada desse valor)
        montante = montante - cedula_atual #No loop, o programa vai subtrair a cedula_atual (R$50) do montante total quantas vezes for possível
        totalced = totalced + 1 #cada vez que for retirada uma cedula de 50, o contador vai contando quantas cédulas estão sendo retiradas
    else: #se não der para retirar cedulas de $50 do montante, o programa vai verificar qual a próxima cedula_atual.
        if totalced > 0: #condição para imprimir a mensagem apenas se o total de notas for maior que zero
            print(f'Total de {totalced} notas de R${cedula_atual}')
        if cedula_atual == 50: #se a cedula atual for de 50, é sinal que não posso mais retirar 50 do montante
            cedula_atual = 20 #então a próxima cedula atual vai ser a de 20
        elif cedula_atual == 20: #se a cedula atual for de 20, é sinal que não posso mais retirar 20 do montante
            cedula_atual = 10 #então a próxima cedula atual vai ser a de 10
        elif cedula_atual == 10: #se a cedula atual for de 10, é sinal que não posso mais retirar 10 do montante
            cedula_atual = 1 #então a próxima cedula atual vai ser a de 1
        totalced = 0 #cada vez que muda uma nota, o total de cedulas deve voltar a 0 para fazer a contagem certa de cada cedula
        if montante == 0: #Se o montante total, após retirar todas as cédulas for igual a zero, o programa para.
            break