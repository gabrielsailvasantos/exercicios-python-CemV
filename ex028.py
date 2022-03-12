'''
import random
numusuario = int(input('Digite um numero e veja se acerta: '))
numcomp = int(random.randrange(0, 5))
print('Agora veja se voce ganhou!')
if (numusuario == numcomp):
    print('Voce ganhou! O numero que ele escolheu foi o {}'.format(numcomp))
else:
    print('Voce errou!! O programa ganhou... O numero que ele escolheu foi o {}'.format(numcomp))
print('----FIM----')
'''
from time import sleep
from random import randint
computador = randint(0, 5) # Faz o computador pensar
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero em pensei? '))# Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no nuemro {} e nao no {}!'.format(computador, jogador))