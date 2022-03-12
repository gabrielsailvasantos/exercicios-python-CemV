# EMPRESTIMO BANCARIO (MEU MÈTOD)

valorcasa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salario? '))
anos = int(input('Em quantos anos pretende pagar? '))
parc = valorcasa /(anos * 12)
valorporcsalario = (sal * 30)/100
#print(valorporcsalario)
if parc <= valorporcsalario:
    print('O emprestimo foi aprovado!!!')
    print('O valor das parcelas será: {:.2f}'.format(parc))
else:
    print('O emprestimo nao foi aprovado!\nValor da parcela é R$ {:.2f} alta para voce!'.format(parc))


