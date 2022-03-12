aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['media'] = float(input('Digite a media deste aluno: '))
if aluno['media'] >= 7:
    aluno['situacao'] = str('APROVADO!!!')
elif aluno['media'] < 7 and aluno['media'] >= 5:
    aluno['situacao'] = str('RECUPERACAO!!!')
else:
    aluno['situacao'] = str('REPROVADO!!!')
print(f'O nome do aluno(a) é {aluno["nome"]}')
print(f'A média é igual a {aluno["media"]}')
print(f'A situacao é igual a {aluno["situacao"]}')
