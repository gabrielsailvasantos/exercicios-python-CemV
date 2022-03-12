num = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

while True:
    num2 = int(input('Digite um numero entre 0 e 20: '))
    if num2 > 20:
        print('!!!ERRO 404!!!')
        num2 = int(input('Digite novamente um numero entre 0 e 20: '))
    if num2 == 0:
        print('Voce digitou o numero zero')
    elif num2 == 1:
        print('Voce digitou o numero um')
    elif num2 == 2:
        print('Voce digitou o numero dois ')
    elif num2 == 3:
        print('Voce digitou o numero tres ')
    elif num2 == 4:
        print('Voce digitou o numero quatro ')
    elif num2 == 5:
        print('Voce digitou o numero cinco ')
    elif num2 == 6:
        print('Voce digitou o numero seis ')
    elif num2 == 7:
        print('Voce digitou o numero sete')
    elif num2 == 8:
        print('Voce digitou o numero oito')
    elif num2 == 9:
        print('Voce digitou o numero nove')
    elif num2 == 10:
        print('Voce digitou o numero dez')
    elif num2 == 11:
        print('Voce digitou o numero onze')
    elif num2 == 12:
        print('Voce digitou o numero doze')
    elif num2 == 13:
        print('Voce digitou o numero treze')
    elif num2 == 14:
        print('Voce digitou o numero quatorze')
    elif num2 == 15:
        print('Voce digitou o numero quinze')
    elif num2 == 16:
        print('Voce digitou o numero dezesseis')
    elif num2 == 17:
        print('Voce digitou o numero dezesete')
    elif num2 == 18:
        print('Voce digitou o numero dezoito')
    elif num2 == 19:
        print('Voce digitou o numero dezenove')
    elif num2 == 20:
        print('Voce digitou o numero vinte')

    if num2 in num:
        break