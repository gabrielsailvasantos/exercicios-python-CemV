# SOMA DOS NUMEROS QUE SAO PARES

soma = 0
for c in range(1, 7):
    c = int(input('Digite os numeros: '))
    if c % 2 == 0:
        soma += c
print(soma)