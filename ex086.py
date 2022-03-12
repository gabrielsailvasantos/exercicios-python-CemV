matriz = [[], [], []]
for n in range(0, 3):
    matriz[0].append(input(f'Digite um valor para [0, {n}]: '))
for u in range(0, 3):
    matriz[1].append(input(f'Digite um valor para [1, {u}]: '))
for m in range(0, 3):
    matriz[2].append(input(f'Digite um valor para [2, {m}]: '))
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')

'''
Solução do Guanabara!!!

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
'''