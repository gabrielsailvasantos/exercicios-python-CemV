todos = []
impar = []
par = []
while True:
    todos.append(int(input('Digite um valor: ')))
    soun = str(input('Quer adicionar mais ? [S/N] ')).strip()[0]
    if soun in 'Nn':
        break
for n in todos:
    if n % 2 == 0:
        par.append(n)
for v in todos:
    if v % 2 != 0:
        impar.append(v)
print('=' * 40)
print(f'Os numeros digitados sao estes {todos}')
print(f'Os pares sao {par}.\nE os impares sao {impar}.')