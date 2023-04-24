#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Informe um nome de cidade: ')).strip() #Método .strip() é para remover os espaços da string

print('Analisando a incidência da palavra "Santo" no nome...')
print(cid[:5].upper() == 'SANTO')



