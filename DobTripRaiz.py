# Algoritmo que calcula o dobro, triplo e raiz quadrada de um número inserido pelo usuário.
# Inclui a biblioteca Math para realizar a operação de raíz quadrada.

import math
num = int(input('Informe um número: '))
#print('O dobro de {} é: {} , o triplo é: {} , e a raíz quadrada de {} é: {}'.format(num, (num*2), (num*3), num, (math.sqrt(num))))
# Também pode ser feito utilizando variáveis.
dob = num * 2
tri = num * 3
raiz = math.sqrt(num)
# Aí informa no print
print('O dobro de {} é: {}, o triplo é: {}, e a raíz quadra da de {} é: {}'.format(num, dob, tri, num, raiz))

