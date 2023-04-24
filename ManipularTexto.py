'''Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome completo: ')).strip() #.strip() para utilizar a contagem dos espaços sem incluir os espaços
# nome[9:21:2] [começa no caracter 9: vai até o 21: pulando de 2 em 2]
# print('A nona string é o: {}'.format(nome[9]))
# Contando quantas letras O apareceram dentro do intervalo
# print(nome.count('o',0,20))
print('Analisando seu nome...')
print('Seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em letras minúsculas é: {}'.format(nome.lower()))

#format(len(nome)- nome.count(' ') foi utilizado para descontar os espaços em branco
print('Seu nome tem ao todo {} letras.'.format(len(nome)- nome.count(' ')))

#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
#Metodo para separar o nome em uma lista
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))