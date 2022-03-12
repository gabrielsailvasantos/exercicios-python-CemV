from datetime import date
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
pessoa['nasc'] = int(input('Ano de nascimento: '))
anoatual = date.today().year
pessoa['ct'] = int(input('Carteira de trabalho (0 nao tem): '))
while True:
    if pessoa['ct'] == 0:
        print(f'nome tem o valor {pessoa["nome"]}')
        print(f'idade tem o valor {anoatual - pessoa["nasc"]}')
        print('ctps tem o valor 0')
        break
    else:
        pessoa['anodecontra'] = int(input('Ano de contratacao: '))
        pessoa['salario'] = int(input('Salaio: R$'))
        print(f'nome tem o valor {pessoa["nome"]}')
        print(f'idade tem o valor {anoatual - pessoa["nasc"]}')
        print(f'ctps tem o valor {pessoa["ct"]}')
        print(f'contratacao tem o valor {pessoa["anodecontra"]}')
        print(f'salario tem o valor {pessoa["salario"]}')
        print(f'Aposentadoria tem o valor {(pessoa["anodecontra"] - pessoa["nasc"]) + 35}')
        break
