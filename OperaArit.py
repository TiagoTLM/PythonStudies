# Aula sobre operadores aritméticos
# Soma +, Subtração -, Multiplicação *, Divisão /, Potência **, Divisão inteira //, Resto da divisão %
# Ordem de precedência entre os operadores: 1 (), 2 **, 3 * / // e %, 4 + e -.


num1 = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
soma = num1 + num2
subt = num1 - num2
mult = num1 * num2
div = num1 / num2
potenc = num1 ** num2
divInt = num1 // num2
restDiv = num1 % num2

# Operações:
print('O resultado da soma entre {} e {} é: {}'.format(num1, num2, soma))
print('O resultado da subtração entre {} e {} é: {}'.format(num1, num2, subt))
print('O resultado da multiplicação entre {} e {} é: {}'.format(num1, num2, mult))
print('O resultado da divisão entre {} e {} é: {:.3f}'.format(num1, num2, div))
print('O resultado da potência entre {} e {} é: {}'.format(num1, num2, potenc))
print('O resultado da divisão inteira entre {} e {} é: {}'.format(num1, num2, divInt))
print('O resto da divisão entre {} e {} é: {}'.format(num1, num2, restDiv))


