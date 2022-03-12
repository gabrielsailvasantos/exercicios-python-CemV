notas[] = int
soma = 0
for i in range(4):
    notas.append(input(f'Digite a {i + 1} nota: '))
    
for nota in notas:
    soma = soma + nota
print(f'A média deste aluno é {soma / len(notas)}')
