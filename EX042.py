r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if (r2 - r3) < r1 < r2 + r3:
    touf1 = True
    #print('Primeira fase {}'.format(touf1))
else:
    touf1 = False
if (r1 - r3) < r2 < r1 + r3:
    touf2 = True
    #print('Segunda fase {}'.format(touf2))
else:
    touf2 = False
if (r1 - r2) < r3 < r1 + r2:
    touf3 = True
    #print('Terceira fase {}'.format(touf3))
else:
    touf3 = False
if touf1 == True and touf2 == True and touf3 == True:
    print('Todas as retas formam um triangulo!', end='')
    if r1 == r2 == r3:
        print('EQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISOSCELES!')
else:
    print('Os numeros acima nao formam um triangulo!')