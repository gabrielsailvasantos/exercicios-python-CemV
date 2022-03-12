from datetime import date
ano = date.today()
maior = 0
menor = 0
cont = 0
anos = 0
for c in range(1, 8):
    cont += 1
    print('Em que ano a {}'.format(cont), end='')
    anos = int(input(' pessoa nasceu? '))
    res = ano.year - anos
    if res >= 21:
        maior += 1
    else:
        menor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade'.format(menor))
