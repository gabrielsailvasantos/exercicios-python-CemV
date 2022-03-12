# JOGO DE JOKEMPO
'''
from random import randrange
from time import sleep
print('Jogo do JOKEMPO!\nEscolha uma das 3 opçoes abaixo!')
player = int(input('1 - PEDRA\n2 - PAPEL\n3 - TESOURA\nQual sua escolha: '))
comput = int(randrange(0, 2)) # ESCOLHENDO UM NUMERO ALEATORIO PARA O NPC, UTILIZANDO RANDRANGE
if comput == 0:
    comput1 = 1
elif comput == 1:
    comput1 = 2
elif comput == 2:
    comput1 = 3
if comput == 0 and player == 3: # pedra x tesoura
    win = str('O COMPUTADOR VENCEU!!!')
    print('PROCESSANDO....')
    sleep(2)
    print('Parabens. {}'.format(win))
elif comput == 0 and player == 1:
    print('Temos um empate!!! Os dois escolheram pedra.')
elif comput == 2 and player == 2:
    win
'''
from random import randrange

print('JODO DO JOKENPÔ!!!\nEscolha uma das opçõs abaixo.')
print('1 = Pedra\n2 - Tesoura\n3 - Papel')
usuario = int(input('Qual voce quer: ')) # ARMAZENANDO MINHA ESCOLHA
comput = randrange(1, 4) # FAZENDO O PC ESCOLHER
if comput == 1 and usuario == 2:
    print('O computador ganhou, ele escolheu PEDRA e voce escolheu TESOURA!!!')
elif usuario == 1 and comput == 2:
    print('Voce ganhou, voce escolheu PEDRA e o pc escolheu TESOURA!!!')
elif usuario and comput == 1:
    print('Houve um empate, os dois escolheram PEDRA!!!')
elif comput == 2 and usuario == 3:
    print('O computador ganhou, ele escolheu TESOURA e voce escolheu PAPEL!!!')
elif usuario ==  2 and comput == 3:
    print('Voce ganhou, voce escolheu TESOURA e o pc escolheu PAPEL!!!')
elif usuario and comput == 2:
    print('Houve um empate, os dois escolheram TESOURA!!!')
elif comput == 3 and usuario == 1:
    print('O computador ganhou, ele escolheu PAPEL e voce escolheu PEDRA!!!')
elif usuario == 3 and comput == 1:
    print('Voce ganhou, voce escolheu PAPEL e o pc escolheu PEDRA!!!')
elif usuario and comput == 3:
    print('Houve um empate, os dois escolheram PAPEL!!!')





