'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

num = int(input('Informe um número para que eu determine se ele é par ou impar: '))
div = (num % 2)

if div == 0:
    print('O número {} é par'.format(num))
else:
    print('O número {} é impar'.format(num))
    