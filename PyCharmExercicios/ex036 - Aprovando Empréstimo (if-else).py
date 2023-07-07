'''Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa deve
perguntar o valor da casa, o salario do comprador e em quantos anos ele irá pagar.
Calcule o valor da prestação mensal, sabendo que ela não deve exceder 30% do salário ou então o
empréstimo será negado.'''

valor = float(input('Valor total do imóvel: R$ '))
s = float(input('Valor do seu salário atual: R$ '))
anos = int(input('Em quantos anos irá quitar o imóvel: '))
tempo = anos * 12 #Vai me dar o tempo total em meses
print('\n','\033[35;40m*'*3,'Relatório de Empréstimo','*'*3,'\033[m')
print(f'--- Valor do imóvel: R$ {valor:.2f}')
print(f'--- Total de meses para a quitação do imóvel: {tempo} meses')
parcela = (valor / tempo) #Calculo do valor da parcela mensal
prestaçao = (s*30/100) #Calculo de 30% do salario
print(f'--- Valor da prestação mensal = R$ {parcela:.2f}')
print(f'\033[30;47mPara a liberação de crédito, o valor da prestação não deve ser superior a R$ {prestaçao:.2f} por mês.\033[m')
if parcela <= prestaçao:
    print('\033[1;34mEmpréstimo aceito. Em breve seu crédito será liberado.\033[m')
else:
    print('\033[1;31mEmpréstimo negado, pois a prestação mensal excede o limite de 30% do salário atual.\033[m')

print('-'*50)