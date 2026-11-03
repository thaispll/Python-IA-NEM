while True: #inicio o loop
    print("\n--- Calculadora ---")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("0 Sair")
    print("=" *25)

    opcao = input("Escolha uma opção:")

    if opcao == "0":
        print("Até logo!")
        break

    num1 = float(input("Digite o 1º número: "))
    num2 = float(input("Digite o 2º número: "))

    #Se o usuário escolher sair, interrompe o loop
    match opcao:
        case "1":
            print(f"Resultado: {num1 + num2}")
        case "2":
            print(f"Resultado: {num1 - num2}")
        case "3":
            print(f"Resultado: {num1 * num2}")
        case "4":
            if num2 != 0:
                print(f"Resultado: {num1 / num2}")
            else:
                print("Erro por não pode existir divisão por zero!")
        case _:
            print("Opção inválida!")
