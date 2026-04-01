from extracao import extrair_html
from transformacao import extrair_livros
from carga import salvar_csv

# target url
URL = "http://books.toscrape.com/"

def main():
    print("início ETL")

    html = extrair_html(URL)

    if not html:
        print("Nenhuma informação extraída.")
        return

    dados = extrair_livros(html)

    # persistir dados em arquivo csv
    salvar_csv(dados)

    print("Processo finalizado!")


if __name__ == "__main__":
    main()