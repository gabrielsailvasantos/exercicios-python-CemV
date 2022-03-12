'''
from random import randint
from time import sleep
lista = [[]]
num = 0
cont = 0
print('=' * 30)
print('      JOGA NA MEGA SENA')
print('=' * 30)
quantos = int(input('Qual a quantidade de palpites: '))
print(f'===== Sorteando {quantos} Jogos =====')
while quantos != 0:
    quantos -= 1
    cont += 1
    for i in range(0, 6):
        num = randint(1, 60)
        if num not in lista[0]:
            lista[0].append(num)
        else:
            while num in lista[0]:
                num = randint(1, 60)
                lista[0].append(num)
        if i == 5:
            lista[0].sort()
            print(f'Jogo {cont}:{lista[0]}')
            sleep(1)
            for l in range(0, 6):
                lista[0].pop()
'''
'''

from random import sample
from time import sleep
quantos = int(input('Qual a quantidade de palpites: '))
for i in range(quantos):
    print(f'Jogo {i+1}: ', end='')
    print(sorted(sample(range(1, 61), 6)))
    sleep(0.5)
'''

#'''Solução do guanabara

from random import randint
from time import sleep
lista = list()
jogos = list()
print('-' * 30)
print('      JOGA NA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos voce quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-=' * 3, f' SORTEANDO {quant} JOGOS', '-=' * 3)
for i, l in enumerate(jogos):
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
print('-=' * 5, '< BOA SORTE! >', '-=' * 5)

#'''