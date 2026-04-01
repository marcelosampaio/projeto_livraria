import requests

def extrair_html(url):
    resposta = requests.get(url)

    if resposta.status_code != 200:
        print(f"Erro ao acessar o site. Status code: {resposta.status_code}")
        return None

    return resposta.text