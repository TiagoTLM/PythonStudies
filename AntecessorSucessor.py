# Escrever um algorítimo que lê um número inteiro e mostra na tela o seu antecessor e sucessor.
#Utilizei duas formas diferentes de fazer a operação, primeiro utilizando variáveis e depois apenas com operações básicas
num = int(input('Informe um número: '))
# ant = num - 1
# suc = num + 1
# print('O antecessor de {} é: {} e o sucessor de {} é: {}'.format(num, ant, num, suc))
print('O antecessor de {} é: {} e o sucessor de {} é: {}'.format(num, (num-1), num, (num+1)))
