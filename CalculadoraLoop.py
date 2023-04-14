# Teste de uma calculadora em looping
while True:
    print('='*20)
    print('Escolha uma operação')
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('0 - Sair do programa')

    opera = input('Opção escolhida: ')

    if opera == '0':
        print('Fim da execução!')
        break  # Saindo do looping

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opera == '1':
        result = num1 + num2
        print('{} + {} = {}'.format(num1, num2, result))

    elif opera == '2':
        result = num1 - num2
        print('{} - {} = {}'.format(num1, num2, result))

    elif opera == '3':
        result = num1 * num2
        print('{} x {} = {}'.format(num1, num2, result))

    elif opera == '4':
        result = num1 / num2
        print('{} / {} = {}'.format(num1, num2, result))

    else:
        print('Opção inválida, tente novamente!')
