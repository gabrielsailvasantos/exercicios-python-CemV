nume1 = int(input('Digite um numero: '))
nume2 = int(input('Digite o segundo numero: '))
if nume1 == nume2:
    print('Nao existe valor maior, os dois sao iguais!')
elif nume1 > nume2:
    print('O primeiro numero é maior {} > {}'.format(nume1, nume2))
else:
    print('O segundo é maior {} > {}'.format(nume2, nume1))