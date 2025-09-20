try:

    base = int(input("Digite a base para ver sua tabuada: "))
    inicio = int(input("Digite o início da tabuada: "))
    fim = int(input("Digite o fim da tabuada: "))
    i = 1

    print(f"Tabuada do {base}")
    while i <= fim:
        if i >= inicio:
            print(f"{base} x {i} = {base * i}")
        i += 1

except ValueError:
    print("Entrada invalida! Digite apenas numeros para a base, inicio e fim.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}. Por favor tente novamente.")
