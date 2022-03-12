num = 0
lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    soun = str(input('Quer adicionar mais numeros? [S/N] ')).strip()[0]
    if soun in 'Nn':
        break
print(f'Os numeros digitados foram {lista}')
print(f'A quantidade de numeros digitados foi {len(lista)}')
lista.sort(reverse=True)
print(f'Os numeros em ordem decrescente {lista}')
if 5 in lista:
    print('O numero 5 tem sim na lista!')
else:
    print('O numero 5 nao tem na lista!')
