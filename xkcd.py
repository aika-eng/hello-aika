import bs4
import requests
import os


# exist_ok=True serve para verificar se a pasta ja existe
os.makedirs("xkcd", exist_ok=True) #makedirs cria pasta
for i in range(1,50):
    url = "https://xkcd.com/1" + str(i) #Grava a url do site
    xkcd = requests.get(url) #Importa o codigo html do site
    status = xkcd.raise_for_status() 
    soup = bs4.BeautifulSoup(xkcd.text, "html.parser") # Converte o site em html

    comic_elem = soup.select("#comic img") [0] #Localiza o id=comic e a tag img
    comic_url = "https:" + comic_elem.get("src") 

    print(f"Baixando a imagem {comic_url}...") #Aviso de download da URL
    res = requests.get(comic_url)
    res.raise_for_status

    image_file = os.path.join("xkcd", os.path.basename(comic_url))
    with open(image_file, "wb") as f:
        f.write(res.content)

print(f"Imagem salva em {image_file}")
