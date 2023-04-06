# O algoritmo pedirá a altura e largura de uma parede e informará quanto de tinta será necessário para pinta-la. Cada 1l de tinta pinta 2m de parede.
print('=' * 100)
print('Por favor, utilize o ponto "." ao invés da vírgula"," ao informar as medidas em metros')
alt = float(
    input('Informe a altura, em metros, da parede que você deseja pintar: '))
comp = float(
    input('Informe o comprimento, em metros, da parede que você deseja pintar: '))
area = alt * comp
tinta = area / 2
print('A área total a ser pintada é de {:.2f}m.' .format(area))
print(
    'Você precisará de {:.2f}l de tinta para concluir a pintura.'.format(tinta))
print('=' * 100)
