from bs4 import BeautifulSoup

def extrair_livros(html):
    soup = BeautifulSoup(html, "html.parser")

    livros_html = soup.find_all("article", class_="product_pod")

    dados_extraidos = []

    for livro in livros_html:
        titulo = livro.h3.a["title"]
        preco = livro.find("p", class_="price_color").text.strip()

        dados_extraidos.append({
            "titulo": titulo,
            "preco": preco
        })

    return dados_extraidos