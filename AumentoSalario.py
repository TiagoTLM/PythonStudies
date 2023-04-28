'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''

sal = float(input('Informe seu salário: R$'))

if sal <= 1250:
    aumento = (sal * 15) /100
else:
    aumento = (sal * 10) /100

print('Seu aumento salarial será de: {:.2f}. Seu salario corrigido será: {:.2f}'.format(aumento, aumento + sal))    