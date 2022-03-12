'''
ano = int(input('Digite um ano: '))
if (ano % 4 == 0):
    print('Ano Bissexto!')
else:
    print('Ano nao Bissexto!')
'''

from datetime import date # Importando uma biblioteca de cata/hora etc...import
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # Pega o ano atual da maquina.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
