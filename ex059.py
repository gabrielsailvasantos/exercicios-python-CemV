from time import sleep
num1 = int(input('Primeiro numero: '))
num2 = int(input('Segundo numero: '))
sair = 0
soum = 0

while sair != 5:
    print('''\033[4;32m--- MENU ---\033[m
\033[1;34m[1]\033[m SOMAR
\033[1;35m[2]\033[m MULTIPLICAR
\033[1;36m[3]\033[m MAIOR
\033[1;33m[4]\033[m NOVOS NUMEROS
\033[1;31m[5]\033[m SAIR DO PROGRAMA''')
    sair = int(input('Digite o que deseja: '))
    if sair == 1:
        soum = num1 + num2
        print('A soma dos numeros é {}.\n'.format(soum))
        sleep(3)
    if sair == 2:
        soum = num1 * num2
        print('A multiplicação dos numeros é {}\n'.format(soum))
        sleep(3)
    if sair == 3:
        if num1 > num2:
            print('O numero primeiro numero {} é maior que o segundo {}'.format(num1, num2))
        elif num2 > num1:
            print('O segundo numero {} é maior que o primeiro {}'.format(num2, num1))
        else:
            print('Os dois numeros sao iguais {} e {}'.format(num1, num2))
        sleep(3)
    if sair == 4:
        num1 = int(input('Digite o novo primeiro numero: '))
        num2 = int(input('Digite o novo segundo numero: '))
        sleep(3)
    if sair > 5:
        print('\033[1;31m!!!OPÇÂO INVALIDA!!!\033[m')
        sleep(2)
print('PROGRAMA FINALIZADO COM SUCESSO')