sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o seu sexo: ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('\33[31mDigite novamente ou a letra M ou F !!!\33[m')
print('\33[32m----FIM----')
