'''
termo1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
cont = 10
soma = 0
dec = 0
soun = ''
while cont != 1:

    if cont == 10:
        print('{} >'.format(termo1), end='')
        soma = termo1 + raz
    else:
        soma += raz
    print(' {} >'.format(soma), end='')
    cont -= 1
    if cont == 1:
        soun = str(input('\nVoce deseja colocar mais termos? [S/N] ')).upper()
        if soun == 'S':
            cont = int(input('Mais quantos: '))
            termo1 = 0
            termo1 = (termo1 + soma)

print('ACABOU!!!')
'''

print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostras a mais ? '))
print('Progressao finalizada com {} termos mostrados.'.format(total))