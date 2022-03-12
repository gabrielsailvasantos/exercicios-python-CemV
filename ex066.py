soma = 0
cont = 0

while True:
    num = int(input('Digite um numero: 999 para parar'))
    if num == 999:
        break
    else:
        cont += 1
        soma = soma + num
print(f'A soma de {cont} numeros foi {soma}')