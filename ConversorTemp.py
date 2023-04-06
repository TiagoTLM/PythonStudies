# O algoritmo irá converter a temperatura de Graus Celcius para Fahrenheit.
# Fórmula retirada do Google:   °C -> °F =>   (°C * 9)/5 + 32
# Fórmula retirada do Google:  °F -> °C = >   ((°F - 32)*5)/9
print('=' *150)
print('=' *150)
print('Conversor °C -> °F  e  °F -> °C')
opcao = input(
    'Digite "1" para converter de °C para °F -ou- Digite "2" para converter de °F para °C: ')

if opcao == '1':
    grau = float(input('Informe a temperatura em Graus Celcius: '))
    faren = (grau * 9)/5 + 32
    print('A temperatura {}°C é equivalente à {}°F'.format(grau, faren))

elif opcao == '2':
    faren = float(input('Informe a temperatura em Graus Fahrenheit: '))
    grau = ((faren - 32)*5) / 9
    print('A temperatura {}°F é equivalente à {:.2f}°C'.format(faren, grau))

else:
    print('Opção inválida!')
