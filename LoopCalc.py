while True:
    print("Calculadora básica")
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

    opcao = int(input("Opção escolhida: "))

    if opcao == 0:
        print("Encerrando o programa...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if opcao == 1:
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif opcao == 2:
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    else:
        print("Opção inválida. Tente novamente.")
