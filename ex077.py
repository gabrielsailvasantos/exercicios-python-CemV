pala = ('APRENDER',
        'PROGRAMAR',
        'LINGUAGEM',
         'PYTHON',
        'CURSO',
        'GRATIS',
        'ESTUDAR',
        'PRATICAR',
        'TRABALHAR',
        'MERCADO',
        'PROGRAMADOR',
        'FUTURO')
for p in pala:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')