from datetime import date
ano = int(input('Qual o ano em que voce nasceu? '))
anoatual = int()
anoatual = date.today().year
if (anoatual - ano) < 18:
    falta = (ano - anoatual) + 18
    print('Voce ainda nao pode se alistar!!')
    print('Ainda falta {} anos para se alistar.'.format(falta))
elif (anoatual - ano) > 18:
    falta = (anoatual - ano) - 18
    print('Ja passou o seu alistamento!!')
    print('O seu alistamento foi à {} anos!'.format(falta))
elif (anoatual - ano) == 18:
    print('Voce se alista este ano!!')