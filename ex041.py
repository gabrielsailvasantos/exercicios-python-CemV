from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
anoatual = date.today().year
if (anoatual - ano) <= 9:
    print('Sua categoria é MIRIM!')
elif (anoatual - ano) >= 10 and (anoatual - ano) <= 14:
    print('Sua categoria é INFANTIL!')
elif (anoatual - ano) >= 15 and (anoatual - ano) <= 19:
    print('Sua categoria é Junior!')
elif (anoatual - ano) == 20:
    print('Sua categoria é SENIOR!')
else:
    print('Sua categoria é MASTER!!!')
    