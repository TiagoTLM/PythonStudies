# Algorítimo que informa a tabuada do valor colocado pelo usuário

num = int(input('Entre com um número: '))
# Utilizando quebra de linha
# print('Tabuada de {} é: \nx1= {}\n x2= {}\n x3= {}\n x4= {}\n x5= {}\n x6= {}\n x7= {}\n x8= {}\n x9= {}\n x10= {} '.format(num, num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10))
# Fazendo linha a linha
print('-' * 12)
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 2, num*2))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))
print('-' * 12)
# Teste
