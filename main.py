import requests
from bs4 import BeautifulSoup

# target url
URL = "http://books.toscrape.com/"

# http request
resposta = requests.get(URL)

# response status code
if resposta.status_code != 200:
    print(f"Erro no http request. Status code: {resposta.status_code}")
    exit()
    
print("Conexão bem-sucedida!")

# beatifulsoap object
soup = BeautifulSoup(resposta.text, "html.parser")

# html parsing
print(soup.title.string.strip())