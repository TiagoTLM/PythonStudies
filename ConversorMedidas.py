# Algoritmo para converter medidas Cm, M e Mm.

num = int(input('Informe uma medida em Metros: '))
cent = num * 100
mili = num * 1000
print('A medida {}m convertida em centímetros é: {}cm, e a conversão para milímetros é: {}mm'.format(num, cent, mili))
