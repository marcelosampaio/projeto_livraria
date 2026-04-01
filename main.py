import requests
from bs4 import BeautifulSoup

# target url
URL = "http://books.toscrape.com/"

# http request
resposta = requests.get(URL)

# response status code
if resposta.status_code != 200:
    print(f"Erro ao acessar o site. Status code: {resposta.status_code}")
    exit()
else:
    print("Request successful!")