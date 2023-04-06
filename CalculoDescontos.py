# O algoritmo irá receber o valor de um produto e informará seu valor reajustado com o desconto definido pelo usuário posteriormente

valor = float(input('Informe o valor do produto: R$'))
desc = float(input('Informe em % de desconto do produto: '))
opera = (valor * desc)/100
total = valor - opera
print('Seu produto teve R${:.2f} de desconto. O valor final será de R${:.2f}.'.format(
    opera, total))
