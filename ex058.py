from random import randint

comp = 0
player = 1
cont = 0
print('----- JOGO DO ADIVINHA -----')
while comp != player:
    cont += 1
    player = int(input('Digite um numero de 0 a 10: '))
    comp = randint(0, 10)
    print('\033[1;31mOPSS... Voce errou!!!\033[m\nSua escolha foi {} e a do PC foi {}'.format(player, comp))
    if comp != player:
        print('TENTE NOVAMENTE\n')
    else:
        print('\033[1;33m\nPARABENS... Voce ganhou!!!\033[m\nVoce escolheu {} e o PC {}'.format(player, comp))
        print('Voce precisou de {} tentativas para ganhar'.format(cont))