'''Faça um programa que leia um ano qualquer e mostre se ele é Bissexto '''
import datetime

print('\n','-'*5,'ANO BISSEXTO','-'*5)
ano = int(input('Digite um ano: '))
bissexto = True
if ano ==0:
    ano = datetime.date.today().year #Importei o modulo datetime que vai considerar o ano atual sempre que o usuario digitar o numero zero
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é bissexto? {bissexto}')
else:
    print(f'O ano {ano} é bissexto? False.')

'''Para calcular os anos bissextos, utilizam-se estas regras:
- A cada quatro anos, há um ano bissexto;
- São bissextos todos os anos múltiplos de 400, exceto se for múltiplo de 100, mas não de 400, por ex: 1996, 2000, 2004, 2008, 2012, 2016, 2020;
- Não são bissextos os anos múltiplos de 100.'''
