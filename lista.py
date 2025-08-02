# Lista inicial
nomes = ["Joaquim", "Maria", "Ana"]
print("Lista inicial: ", nomes)
print("-" * 50)

# Adicionando elementos
nomes.append("Carlos") # Adiciona ao final
print("Após o append: ", nomes)
print("-" * 50)

nomes.insert(1, "Fernanda") #Adiciona a fernanda na posicao 1
print("Após o insert: ", nomes)
print("-" * 50)

# Modificando elementos
nomes[2] = "Paulo" # Modifica o elemento no indice 2
print("Após a modificação: ", nomes)
print("-" * 50)

# Removendo os elementos
del nomes[3] #remove o elemento do indice 3
print("Após del: ", nomes)
print("-" * 50)

nomes.remove("Carlos") # Remove a primeira ocorrencia de Ana
print("Após remove: ", nomes)
print("-" * 50)

item_removido = nomes.pop(2) # Remove e retorna o elemento do indice 2
print(f"Após pop (removido '{item_removido}): '", nomes)
print("-" * 50)

nomes.clear() # Esvazia a lista
print("Após o clear: ", nomes)
print("-" * 50)
