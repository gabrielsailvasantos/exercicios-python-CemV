'''
num = []
menor = 0
maior = 0
posmenor = 0
posmaior = 0
for c in range(0, 5):
    num.append(int(input('Digite 5 valores: ')))
    if c < 1:
        maior += num[0]
        menor += num[0]

    for val in num:
        if val >= maior:
            posmaior += val.index()
            maior = 0
            maior += val

        elif val <= menor:
            menor = 0
            menor += val


print(f'Maior {maior}, menor {menor} e a posicao do menor ')
'''


'''
#Metodo do guanabara

listanum = []
mai = 0
men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum [c] < men:
            men = listanum[c]
print('=-' * 30)
print(f'Voce digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {men} nas posicoes ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}...', end='')
print()
'''


num = []
for c in range(0, 5):
    num.append(int(input('Digite um numero: ')))

print(f'O maior valor foi o {max(num)}, e esta na posição {num.index(max(num))}')
print(f'O menor valor foi o {min(num)}, e esta na posição {num.index(min(num))}')
