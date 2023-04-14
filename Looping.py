#Teste de looping

'''Looping básico com uma variável contadora:
contador = 0
while contador <= 10:
    print(contador)
    contador += 1
print('Fim do looping!')'''    

#Looping com inserção de dados e uma condição para encerrar
maior = 0
while maior < 20:
    num = int(input('Informe um número: '))
    if num >= maior:
        maior = num
        print('O maior número é: {}'.format(maior))
    else:
        print('O maior número é: {}'.format(maior))    

print('Fim!')

