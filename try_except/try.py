#tenta realizar o codigo que pode realizar erro
try: 
    #Solicita dois numeros ao usuario e realiza a operação
    num1 = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    resultado = num1 / num2

#Caso o erro seja de divisao por zero
except ZeroDivisionError: 
    print("Erro: Divisao por 0 não é permitida")
#Caso o erro seja por algum valor nao numerico como um texto
except ValueError:
    print("Erro, digitar apenas numeros inteiros")
#Caso nao aja erro mostramos o resultado
else:
    print(f"o resultado da divisão é {resultado}")
#Esse bloco sempre é executado, nao importa se houve erro ou nao
finally: 
    print("Operação finalizada. ")
