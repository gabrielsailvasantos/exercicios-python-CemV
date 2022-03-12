while True:
    num = int(input('Quer ver a taboada de que numero? '))
    if num >= 0:
        for c in range(1, 11):
            print(f'{num} X {c} = {num * c}')
    else:
        break
print('ACABOU!!!')
