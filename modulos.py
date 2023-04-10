# Testando os módulos do python

# import [módulo] -> Importa o módulo inteiro
# from [módulo] import [função] -> Importa função específica

# import math
import random
# aí não precisa utilizar o comando informando o nome da lib antes (math.sqrt), apenas chama a função
from math import sqrt, ceil

# num = random.random() #gera um número aleatório entre 0 e 1
num = random.randint(0, 10)
raiz = sqrt(num)
print('A raíz de {} arrendodado para cima é: {:.2f}'. format(num, ceil(raiz)))
