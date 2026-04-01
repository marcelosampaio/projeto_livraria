import requests
import csv

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

# procurando por livros
livros_html = soup.find_all("article", class_="product_pod")

# quantidade de livros encontrados
print(f"Quantidade de livros encontrados: {len(livros_html)}")

# lista com os dados extraídos
dados_extraidos = []

# loop pelos livros
for livro in livros_html:
    titulo = livro.h3.a["title"]
    preco = livro.find("p", class_="price_color").text.strip()
    
    # criando dicionário
    livro_dict = {
        "titulo": titulo,
        "preco": preco
    }
    
    # adicionando na lista
    dados_extraidos.append(livro_dict)

# geracao de arquivo csv
with open("relatorio_livros.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    colunas = ["titulo", "preco"]
    
    writer = csv.DictWriter(arquivo, fieldnames=colunas)
    
    writer.writeheader()
    writer.writerows(dados_extraidos)

print("Relatório CSV gerado com sucesso!")