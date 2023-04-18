# Apenas a base para criação de crawlers personalizáveis

import requests
from bs4 import BeautifulSoup

# Aqui define a função que fará o request HTTP e fará a extração das informações do HTML


def crawl(url):
    # Requisição GET para a URL
    response = requests.get(url)

    # Verificando se a resposta foi positiva
    if response.status_code == 200:
        # Analisando o HTML da página com o método BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        '''Neste espaço poderá ser feita a adição do código para extrair as informações desejadas da página HTML
        Ex: Encontre todas as tags <Videogame> e extraia seus links'''
        links = []
        for link in soup.find_all('a'):
            links.append(link.get('href'))

        # Retornando as informações coletadas
        return {
            'url': url,
            'links': links
        }

    # Se a resposta não for bem sucedida, retorne None
    else:
        return None
