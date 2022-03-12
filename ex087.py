num = numpares = terceira = 0
matriz = [[], [], []]
for n in range(0, 3):
    num = int(input(f'Digite um valor para [0, {n}]: '))
    matriz[0].append(num)
    if num % 2 == 0:
        numpares += num
    if n == 2:
        terceira += num
for u in range(0, 3):
    num = int(input(f'Digite um valor para [1, {u}]: '))
    matriz[1].append(num)
    if num % 2 == 0:
        numpares += num
    if u == 2:
        terceira += num
for m in range(0, 3):
    num = int(input(f'Digite um valor para [2, {m}]: '))
    matriz[2].append(num)
    if num % 2 == 0:
        numpares += num
    if m == 2:
        terceira += num
print('=-' * 30)
print(f'{matriz[0]}\n{matriz[1]}\n{matriz[2]}')
print('=-' * 30)
print(f'A soma dos valores pares é {numpares}')
print(f'A soma dos valores da terceira coluna é {terceira}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')

'''

SOLUÇÃO GUANABARA

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-=' * 30)
print(f'A soma dos valores pares e {spar}')
for l in range(0, 3):
    scol += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0:
        mai = matriz[1][c]
    elif matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'O maior valor da segunda linha é {mai}.')

'''