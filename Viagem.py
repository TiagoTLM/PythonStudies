'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

dist = float(input('Informe a distância percorrida na viagem: '))

if dist > 200:
    valor = (dist * 0.45)
elif dist <= 200:
    valor = (dist * 0.50)
    
print('Sua viagem de {}Km custará R${:.2f}'.format(dist,valor))
print('Obrigado pela preferência!')        