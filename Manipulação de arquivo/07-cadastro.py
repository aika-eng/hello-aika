NOME_PROGRAMA = "Agenda de contatos" # nome do programa NAO MEXA

lista = [] # lista para guardar os contatos

def cadastrar_contato(nome): 
    lista.append(nome) # adiciona o contato à agenda
    print(f"Contato '{nome}' cadastrado com sucesso")


def listar_contatos():
    print("Lista de Contatos: ")
    print(lista) # exibe a lista de contatos


def remover_contato():
    contato_removido = input("Digite o nome do contato a ser removido: ")
    if contato_removido in lista:
        lista.remove(contato_removido)
        print(f"Contato '{nome}' removido com sucesso")
    
    else:
        (f"Contato '{nome}' contato não encontrado na lista")
        
def main(): #Mostrando as opções ao usuario 
    while True: 
        print(NOME_PROGRAMA)
        print("-" * 50)
        print("Menu: ")
        print("1. Cadastrar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Sair")
        print("-" * 50)
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Digite um nome para incluir na lista: ")
            cadastrar_contato(nome)
        
        elif opcao == 2:
            listar_contatos()

        elif opcao == 3:
            remover_contato()
        elif opcao == 4:
            break

        else:
            print("Opção invalida, tente novamente")


if __name__ == "__main__":
    main()



