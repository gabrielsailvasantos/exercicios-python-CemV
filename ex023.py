'''
numero = int(input('Digite um numero de 0 a 9999: '))
numero2 = numero.replace('', ' ').split()
print('Unidade: {}'.format(numero2[3]))
print('Dezenas: {}'.format(numero2[2]))
print('Centenas: {}'.format(numero2[1]))
print('Milhar: {}'.format(numero[0]))
'''

num = int(input('Informe o numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))