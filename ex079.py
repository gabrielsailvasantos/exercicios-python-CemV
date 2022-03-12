num = 0
num1 = []
while True:
    num = int(input('Digite um valor: '))
    if num in num1:
        print('Voce digitou um numero ja existente!')
    if num not in num1:
        num1.append(num)
        soun = str(input('Deseja adicionar mais numeors? S/N ')).strip()[0]
        if soun in 'Nn':
            break
num1.sort()
print(f'Os numeros que voce digitou sao {num1}')