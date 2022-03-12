veloc = float(input('Qual a velocidade do carro: '))
if (veloc <= 80):
    print('Voce esta dentro do limite!')
else:
    multa = (veloc - 80) * 7
    print('Voce foi multado!!!\nVoce receberá uma multa de R$ {:.2f}.'.format(multa))
print('---FIM---')