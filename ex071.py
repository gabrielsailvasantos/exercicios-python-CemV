print('=' * 20)
print('      BANCO DEV')
print('=' * 20)
saque = 0
cinquenta = 0
vinte = 0
resto = 0
dez = 0
um = 0
while True:
    saque = int(input('Que valor voce quer sacar? '))
    cinquenta = saque // 50
    resto = saque % 50
    vinte = resto // 20
    resto = resto % 20
    dez = resto // 10
    resto = resto % 10
    um = resto // 1
    if cinquenta > 0:
        print(f'Total de {cinquenta} cedulas de R$50')
    if vinte > 0:
        print(f'Total de {vinte} cedulas de R$20')
    if dez > 0:
        print(f'Total de {dez} cedulas de R$10')
    if um > 0:
        print(f'Total de {um} cedulas de R$1')
    break
print('Fim... Volte sempre!')

