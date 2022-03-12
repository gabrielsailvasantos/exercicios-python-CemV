# NOVA TABUADA COM LAÇO FOR
import time

num = int(input('Digite um numero para saber sua tabuada: '))
time.sleep(1)
for c in range(0, 11, +1):
    print('{} x {} = {}'.format(num, c, num * c))