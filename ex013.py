sal = float(input('Qual o salario: '))
alm = float(input('Qual a porcentagem de almento: '))
#var1 = sal * alm
#var2 = var1 / 100
#print('O Salario de {:.2f}, com o almento de {:.0f}%, fica agora {:.2f}'.format(sal, alm, sal + var2))

novosal = sal + (sal * alm / 100)
print('Novo salario: {:.2f}'.format(novosal))