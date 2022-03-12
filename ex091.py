from random import randint
from time import sleep
from operator import itemgetter
jog = list()
jogadores = {'Jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rank = list()
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k}, tirou {v}')
print('-=' * 30)
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'    {i +1} lugar: {v[0]} com {v[1]}')
