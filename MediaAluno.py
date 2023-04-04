# Algoritmo que soma duas notas de um aluno e calcula a média.

nome = input('Informe o nome do aluno: ')
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
med = (n1 + n2) / 2
print('A média das notas do aluno {} é: {}'.format(nome, med))

if med >= 7:
    print('O aluno {} está aprovado!'.format(nome))
elif med < 7:
    print('O aluno {} está reprovado!'.format(nome))
