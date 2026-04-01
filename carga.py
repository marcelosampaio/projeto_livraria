import csv

def salvar_csv(dados, nome_arquivo="relatorio_livros.csv"):
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        colunas = ["titulo", "preco"]

        writer = csv.DictWriter(arquivo, fieldnames=colunas)

        writer.writeheader()
        writer.writerows(dados)

    print("Relatório CSV gerado com sucesso!")