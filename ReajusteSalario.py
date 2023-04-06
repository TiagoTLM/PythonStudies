# O algoritmo irá receber o valor em R$ do salário de um funcionário, receber um valor em % a respeito do aumento salarial e devolver a informação na tela

sal = float(input('Informe o valor do salário atual do funcionário: R$'))
aument = int(input('Informe o % de aumento de salário: '))
opera = (sal * aument)/100
atual = sal + opera
print('O salário de R${:.2f} recebeu um aumento de {}% e passou para R${:.2f}'.format(
    sal, aument, atual))
