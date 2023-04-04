# Exercício 004: Dissecar uma variável.

algo = input('Informe alguma palavra ou número. Qualquer coisa: ')
print('O tipo primitivo deste valor é:', type(algo))
print('Foi informado um valor contendo apenas espaços em branco?', algo.isspace())
print('É um número? ', algo.isnumeric())
print('É alfabético?', algo.isalpha())
print('É alfanumérico?', algo.isalnum())
print('Está em maiúscula? ', algo.isupper())
print('Está em minúscula?', algo.islower())
# Verificando se está "capitalizado", ou seja, se possui caracteres maiúsculos e minúsculos junto.
print('Está capitalizada? ', algo.istitle())



