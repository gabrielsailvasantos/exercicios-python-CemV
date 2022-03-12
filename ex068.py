from random import randint
print('=-=' * 12)
print('      JOGO DO PAR OU IMPAR')
print('=-=' * 12)
comp = int(0)
play = 0
cont = 0
poui = ''
soma = 0
parouimpar = ''
while True:
    play = int(input('Digite um valor: '))
    comp = randint(1, 11)
    soma = play + comp
    poui = str(input('Par ou impar? [P/I] ')).strip().upper()
    if soma % 2 == 0:
        parouimpar = 'PAR'
    else:
        parouimpar = 'IMPAR'
    print(f'Voce jogou {play} e o PC {comp}. Total de {soma} e deu {parouimpar}')

    if poui == 'P' and parouimpar == 'PAR':
        print('\033[32mVOCE VENCEU!!!\033[m\nVamos jogar novamente...')
        cont += 1
    if poui == 'I' and parouimpar == 'IMPAR':
        print('\033[32mVOCE VENCEU!!!\033[m\nVamos jogar novamente...')
        cont += 1
    if poui == 'P' and parouimpar == 'IMPAR':
        print(f'Game Over... Voce venceu {cont} vezes.')
        break
    elif poui == 'I' and parouimpar == 'PAR':
        print(f'\033[31mGame Over...\033[m Voce venceu {cont} vezes.')
