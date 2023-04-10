# O programa irá ler um número real e devolver ao usuário apenas a parte inteira.

import math

real = float(input('Informe um número da classe dos reais -separado por ponto . - : '))
print('A porção inteira de {} é: {}'.format(real, math.trunc(real)))