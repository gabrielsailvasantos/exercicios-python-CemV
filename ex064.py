sair = 0
soma = 0
cont = -1
num = 0
while num != 999:
    num = int(input('Digite um numero: '))
    soma = soma + num
    cont += 1
print('Foram digitados {} numeros e a soma deles é {}'.format(cont, soma - 999))