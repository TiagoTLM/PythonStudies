#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase para análise: ')).upper().strip()
print('Analisando')
print('A letra "A" aparece {} vezes em sua frase'.format(frase.count('A')))
print('A letra "A" apareceu apareceu pela primeira vez na posição: {}'.format(frase.find('A')+1))
print('A letra "A" apareceu pela última vez na posição: {}'.format(frase.rfind('A')+1))