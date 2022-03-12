distanciakm = float(input('Digite a distancia em Kilometros: '))
if (distanciakm <= 200):
    print('Voce vai percorrer {:.0f}KM, e vai ter que pagar R$ {:.2f} no total.'.format(distanciakm, distanciakm * 0.50))
else:
    print('Voce vai percorrer {:.0f}KM, e vai ter que pagar R$ {:.2f} no total.'.format(distanciakm, distanciakm * 0.45))

