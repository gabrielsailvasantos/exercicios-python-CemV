'''
temp = dict()
pessoas = list()
totpessoas = 0
totmulher = list()
media = med = 0
while True:
    temp['nome'] = str(input('Nome: '))
    temp['sexo'] = str(input('Sexo: [F/M] '))
    if temp['sexo'] in 'Ff':
        totmulher.append(temp['nome'])
    temp['idade'] = int(input('Idade: '))
    media += temp['idade']
    totpessoas += 1
    soun = str(input('Deseja continuar? [S/N]: '))
    if soun in 'Nn':
        break
print('=-' * 30)
med = media / totpessoas
print(f'-> O grupo tem {totpessoas} pessoas.')
print(f'-> a média de idade é {med:.2f} anos.')
print(f'-> As mulheres cadastradas foram:', end=' ')
for m in totmulher:
    print(m, end=' ')
print(f'\n-> Lista de pessoas que estao acima da media: ')
print(f'media = {med}')
for i in pessoas:
    if i['idade'] >= med:
        print(f'{i["nome"]} que tem {i["idade"]}')


'''

# CODIGO DO GUANABARA

galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO!!! Por favor, digite apenas M ou F ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO!!! Responda apenas S ou N ')
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print(f'As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print('Lista de pessoas que estao acima da media: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}: ', end='')
        print()
print('<<< ENCERRADO >>>')