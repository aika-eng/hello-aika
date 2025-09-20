import requests

cep = input("Digite o CEP que voce deseja consultar: ")

viaCep = f"https://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(viaCep)
data = requisicao.json()


print(f"CEP: {data["cep"]}")
print(f"Rua: {data["logradouro"]}")
print(f"Bairro: {data["bairro"]}")
print(f"Localidade: {data["localidade"]}")
print(f"Estado: {data["estado"]}")
