# PROGRAMA SOBRE PROGRESSAO ARITIMETICA

termo1 = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razao: '))
decimo = termo1 + (10 - 1) * raz
for c in range(termo1, decimo + raz, raz):
    print('{}'.format(c), end='- ')
print('ACABOU')
