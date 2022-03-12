nopes = list()
pessoas = list()
while True:
    nopes.append(str(input('Nome: ')))
    nopes.append(float(input('Peso: ')))
    pessoas.append(nopes[:])
    nopes.clear()
    soun = str(input('Quer adicionar mais alguem? [S/N] '))
    if soun in 'Nn':
        break
print(f'A quantidade de pessoas cadastradas foi {len(pessoas)}')
print('Pessoas mais pesadas: ', end='')
for p in pessoas:
    if p[1] >= 100:
        print(f'{p[0]} com {p[1]}...', end=' ')
print()
print('=-' * 30)
print('Pessoas mais leves: ', end='')
for p in pessoas:
    if p[1] <= 75:
        print(f'{p[0]} com {p[1]}...', end='')
