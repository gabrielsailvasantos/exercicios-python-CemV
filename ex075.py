num = (int(input('Digite um numero: ')),
       int(input('Digite outro numero: ')),
       int(input('Digite mais um numero: ')),
       int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os Numeros: {num}')
if 9 in num:
    print(f'O numero 9 apareceu {num.count(9)} vezes.')
else:
    print(f'O numero 9 nao foi digitado.')
if 3 in num:
    print(f'O valor 3 apareceu na posicao {num.index(3) + 1}')
else:
    print('O numero 3 nao foi digitado.')
print('Os valores pares foram ', end=' ')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')


