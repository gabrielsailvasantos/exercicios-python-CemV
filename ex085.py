todos = [[], []]
num = 0
for n in range(0, 7):
    num = int(input(f'Digite o {n + 1}o. valor: '))
    if num % 2 == 0:
        todos[0].append(num)
    else:
        todos[1].append(num)
todos[0].sort()
todos[1].sort()
print('=-' * 30)
print(f'Valores impares digitados {todos[1]}')
print(f'Valores pares digitados {todos[0]}')
