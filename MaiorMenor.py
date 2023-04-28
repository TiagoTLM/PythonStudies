'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
num3 = int(input('Informe o terceiro número: '))

#Verificando o maior
maior = num1 #Simplificando o código, removendo um If
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3

#Verificando o menor
menor = num1 #Mesma coisa, tirei um If
if num2 < num1 and num2 < num3:
    menor = num2    
if num3 < num1 and num3 < num2:
    menor = num3
print('O número {} é o menor!'.format(menor))        
print('O número {} é o maior!'.format(maior))