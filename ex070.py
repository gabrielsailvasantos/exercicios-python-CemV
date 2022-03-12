nomepro = ''
sair = ''.upper()
nomeprobarato = ''
preco = somatot = maisdemil = precobarato = 0
cont = 1
saida = 0
print('-' * 30)
print('     LOJA SUPER BARATÃO ')
print('-' * 30)
while True:
    nomepro = str(input('Nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if cont == 1:
        precobarato += preco
        cont += 1
    if cont > 1:
        if precobarato > preco:
            precobarato = 0
            precobarato = precobarato + preco
            nomeprobarato = nomepro
    if preco >= 1000:
        maisdemil += 1
    somatot = somatot + preco
    sair = str(input('Quer adicionar mais produtos? [S/N] ')).upper().strip()
    if sair == 'N':
        break
print(f'''-------- FIM DO PROGRAMA ---------
O total da compra foi R${somatot:.2f}
Temos {maisdemil} produtos custando mais de R$1000,00 
O produto mais barato foi {nomeprobarato} que custa R${precobarato:.2f}
''')

