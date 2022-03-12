print('         Controle de Terrenos')
print('-=' * 20)
def area(a, b):
    areatot = a * b
    print(f'A area de um terreno {a}x{b} é de {areatot}m')


area(a=float(input('LARGURA (m): ')), b=float(input('Comprimento (m): ')))
