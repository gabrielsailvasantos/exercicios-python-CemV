dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km foram rodados: '))
tdias = dias * 60
tkm = km * 0.15
print('Total a pagar fica: {:.2f}'.format(tdias + tkm))