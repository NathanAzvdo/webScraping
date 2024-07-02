import requests
from bs4 import BeautifulSoup
import pandas as pd


url_base="https://lista.mercadolivre.com.br/"
produto = input('Qual produto você deseja?')

response = requests.get(url_base+produto)
print(response)

site = BeautifulSoup(response.text, 'html.parser')

products = site.findAll('div', attrs={'class': 'andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16 andes-card--animated'})
lista_produtos = []
for product in products:
    link = site.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link__title-card ui-search-link'})
    titulo = site.find('h2', attrs={'class': 'ui-search-item__title'})
    preco = site.find('span', attrs={'class': 'andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript'})
    lista_produtos.append([titulo, preco, link])

DF_produtos = pd.DataFrame(lista_produtos, columns=["Título", "Preço","Link"])

print(DF_produtos)