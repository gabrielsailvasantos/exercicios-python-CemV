termo1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
cont = 10
soma = 0
while cont != 1:
    if cont == 10:
        print('{} >'.format(termo1), end='')
        soma = termo1 + raz
    else:
        soma += raz
    print(' {} >'.format(soma), end='')
    cont -= 1
print('ACABOU!!!')