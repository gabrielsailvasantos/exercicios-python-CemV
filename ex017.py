''' meu metodo
from math import sqrt
catetomaior = float(input('Cateto maior: '))
catetomenor = float(input('Cateto menor: '))
somacateto = (catetomaior ** 2) + (catetomenor ** 2)
hipo = sqrt(somacateto)
print('Hipotenusa: {:.2f}'.format(hipo))
'''

''' Metodo 2
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimeito do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
'''

'''Metodo 3'''
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))