'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.'''

vel = int(input('Informe a velocidade percorrida: '))

if vel > 80:
    multa = ((vel - 80) * 7) + 150 
    print('Você excedeu o limite de 80Km/h')
    print('O valor base da multa de velocidade é de R$150,00 + R$7,00 para cada Km/h excedido!')
    print('Multado em: {}'.format(multa))
else:
    print('Se safou da multa')    