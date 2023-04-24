#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

num = int(input('Informe um número entre 0 e 9999: '))
n = str(num)

#Encontrando a unidade... Divisão inteira por 1 e tiro o módulo com 10
u = num //  1 % 10
#Encontrando a dezena
d = num // 10 % 10
#Encontrando a centena
c = num // 100 % 10
#Encontrando o milhar
m = num // 1000 % 10

#Informando os respectivos dados
print('Analisando o número {}.'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))