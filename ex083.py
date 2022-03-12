exp = str(input('Digite sua expressao: '))
parfec = 0
parabert = 0
for letra in exp:
    if letra == '(':
        parabert += 1
    elif letra == ')':
        parfec += 1
if parabert == parfec:
    print('Sua expressao é valida!')
else:
    print('Sua expressao é invalida!')