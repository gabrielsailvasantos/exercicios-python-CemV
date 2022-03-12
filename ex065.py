menor = 999 * 999
maior = 0
media = 0
num1 = 0
sair = ''
cont = int(0)
while sair != 'N':
    cont = cont + 1
    num1 = int(input('Digite um numero: '))
    media = media + num1
    sair = str(input('Deseja adicionar mais numeros? ')).upper().strip()
    if num1 > maior:
        maior = 0
        maior += num1
    if num1 < menor:
        menor = 0
        menor += num1

print('Maior {}, menor {} e media {}'.format(maior, menor, media / cont))
