jogador = {}
gols = []
totgols = 0
jogador['nome'] = str(input('Qual o nome do jogador: '))
quantpart = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for g in range(quantpart):
    temp = int(input(f'Quantos gols na partida {g}? '))
    totgols += temp
    gols.append(temp)
print('=-' * 30)
jogador['gols'] = gols
jogador['total'] = totgols
print(jogador)
print('=-' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('=-' * 30)
print(f'O jogador {jogador["nome"]} jogou {quantpart} partidas.')
for p in range(quantpart):
    print(f'    => Na pertida {p}, fez {gols[p]}.')
print(f'Foi um total de {totgols} gols.')
