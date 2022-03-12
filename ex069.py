idade = 0
sexo = ''.upper()
maiorde18 = 0
quanthomens = 0
mulhermenor20 = 0
sair = ''.upper()
saidafinal = 0
while True:
    print('~.~ ' * 10)
    print('         CADASTRE UMA PESSOA')
    print('~.~ ' * 10)
    idade = int(input('Idade: '))
    if idade > 18:
        maiorde18 += 1
    sexo = str(input('Sexo: [M/F] ')).upper().strip()
    if sexo != 'F' and sexo != 'M':
        while sexo != 'F' and sexo != 'M':
            sexo = str(input('Sexo: [M/F] '))
    if sexo == 'M':
        quanthomens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor20 += 1
    sair = str(input('Quer continuar? [S/N] ')).upper().strip()
    if sair == 'N':
        break
    if sair != 'S' and sair != 'N':
        while sair != 'S' and sair != 'N':
            sair = str(input('Quer continuar? [S/N]')).upper()
            if sair == 'N':
                saidafinal = 1
    if saidafinal == 1:
        break
print('===== FIM DO PROGRAMA =====')
print(f'''Total de pessoas com mais de 18 anos: {maiorde18}
Ao todo temos {quanthomens} homens cadastrados.
E temos {mulhermenor20} mulher com menos de 20 anos.
''')