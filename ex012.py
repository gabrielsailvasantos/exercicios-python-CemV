prod = float(input('Qual o preço do produto: '))
des = float(input('Qual a quantidade de desconto: '))
var1 = prod * des
var2 = var1 / 100
print('O valor da compra com o desconto fica: {:.2f}'.format(prod - var2))