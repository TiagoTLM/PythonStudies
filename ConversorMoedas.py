# Algortimo que converte o valor de reak para dólar. Considerando que o dólar está valendo R$5,00

carteira = float(input('Informe quanto dinheiro você tem na carteira: R$'))
dolar = carteira / 5
print('O que você tem na carteira equivale a U${:.2f} '.format(dolar))
