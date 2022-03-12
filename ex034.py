salario = float(input('Qual o salario do funcionario: '))
if salario < 1250:
    salario = salario +((salario * 15) / 100)
    print('O seu salario agora almentou para {:.2f}'.format(salario))
else:
    salario = salario +((salario * 10) / 100)
    print('O seu salario agora almentou para {:.2f}'.format(salario))
print('FIM')