'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
n1 = float(input('Informe o valor do primeiro segmento de reta: '))
n2 = float(input('Informe o valor do segundo segmento de reta:'))
n3 = float(input('Informe o valor do terceiro segmento de reta: '))

#Verificando se os 3 segmentos podem formar um triângulo

if n1 < (n2+n3) and n2 < (n1+n3) and n3 < (n1+n2): #Se a soma de 2 segmentos for maior do que o terceiro segmento, então será um triângulo.
    print('Os três segmentos de reta formam um triângulo.')
else:
    print('Os três segmentos de reta não formam um triângulo.')    