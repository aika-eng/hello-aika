try:

    print("Converte Celsius para Fahrenheit")

    celsius = float(input('Digite a temperatura em Celsius: '))
    fahrenheit = (celsius * 9/5) + 32

    print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}°F')

except ValueError:
    print("Entrada inválida, por favor, digite um numero para a temperatura. Ex: 1, 2, 3...")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}. Por gavor, tente novamente")
