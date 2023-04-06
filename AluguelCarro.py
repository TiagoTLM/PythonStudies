# O algoritmo irá perguntar por quantos dias e quantos Km deteminado carro alugado percorreu e informará o preço final.

print(' '*100)
print(' '*100)
dia = int(input('Informe a por quantos dias o veículo esteve alugado: '))
km = float(input('Informe quantos Km o veículo percorreu durante o aluguel: '))
print('='*100)
print('Diária do veículo = R$60,00')
print('Valor por Km percorrido = R$0,15')
total = (dia * 60) + (km * 0.15)
print('O valor total do aluguel será de: R${:.2f}'.format(total))
