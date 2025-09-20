letra = "s"
while letra.lower() == 's':  # Aceita 's' ou 'S'
    try:
        cotacao = float(input('Digite a cotação do dólar: '))

        if cotacao <= 0:
            print("A cotação do dólar deve ser um valor positivo e maior que zero. Por favor, tente novamente.")
            continue  # Volta para o início do loop

        print("---------------------------------------------------------")
        print("---------------Escolha uma Opção-------------------------")
        print("---------------------------------------------------------")

        opcao = int(input('1 - Converter dólar para real | 2 - Converter real para dólar: '))

        if opcao == 1:
            valor = float(input('Digite o valor em dólar a ser convertido para real: '))
            if valor < 0:
                print("O valor a ser convertido deve ser positivo. Por favor, tente novamente.")
                continue
            resultado = valor * cotacao
            print(f"O valor em reais é: R$ {resultado:.2f}")

        elif opcao == 2:
            valor1 = float(input('Digite o valor em reais a ser convertido para dólar: '))
            if valor1 < 0:
                print("O valor a ser convertido deve ser positivo. Por favor, tente novamente.")
                continue
            resultado1 = valor1 / cotacao
            print(f"O valor em dólar é: US$ {resultado1:.2f}")

        else:
            print('Opção inválida. Por favor, digite 1 ou 2.')
            continue

        letra = input('Deseja continuar [S/N]: ').lower()
        if letra not in ['s', 'n']:
            print("Opção inválida para continuar. O programa será encerrado.")
            break

    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")

print("Programa de conversão encerrado.")
