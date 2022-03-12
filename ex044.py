# CALCULO SOBRE UM PRODUTO X, E SUAS FORMAS DE PAGAMENTO!!!

prod = float(input('Valor do produto, ou o total dos produtos: ')) # valor do produto
print('Digite a opção desejada abaixo!\nForma de pagamento. ')
print('1 = Dinheiro ou cheque.\n2 = C.Credito ou Debito à vista.\n3 = C.Credito parcelado.')
formdpag = int(input('Qual opção deseja: '))
quantparc = int(0)
if formdpag == 1:
    total = prod - ((prod * 10) / 100)
    print('O total da compra de R$ {:.2f} fica R$ {:.2f} com 10% de desconto!'.format(prod, total))
elif formdpag == 2:
    total = prod - ((prod * 5) / 100)
    print('O total da compra de R$ {:.2f} fica R$ {:.2f} com 5% de desconto!'.format(prod, total))
elif formdpag == 3:
    quantparc = int(input('Quantas parcelas: '))
if quantparc == 2:
    print('O total da compra é R$ {:.2f}, fica {}x parcelas de R$ {:.2f}'.format(prod, quantparc, prod / 2))
elif quantparc >= 3:
    total = prod + ((prod * 20) / 100)
    print('O total da compra de {:.2f}, com 20% de juros fica {:.2f}.\nVoce parcelou em {}x vezes de R$ {:.2f}'.format(prod, total, quantparc, total / quantparc))
