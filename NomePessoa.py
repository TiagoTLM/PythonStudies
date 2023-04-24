#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Informe seu nome: ')).strip()
print('Analisando seu nome...')
print('Verificando a incidência do nome "Silva"...')
print('Seu nome tem a palavra "Silva"? {}'.format('SILVA' in nome.upper()))


