peso = float(input('Qual o seu peso atual? '))
alt = float(input('Qual é sua altura (com virgula) '))
imc = peso / (alt ** 2)
print('{:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Voce esta no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Voce esta com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Voce esta com obesidade!')
elif imc >= 40:
    print('Voce esta com Obesidade morbida!!!')