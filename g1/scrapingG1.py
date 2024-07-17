import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content

site =BeautifulSoup(content)

notices = site.findAll('div', attrs={'class': 'feed-post-body'})


for notice in notices:
    title = notice.find('a', attrs={'class': 'feed-post-link'})
    resumo = notice.find('div', attrs={'class': 'feed-post-body-resumo'})
    if resumo:
        lista_noticias.append([title.text, resumo.text, title["href"]])
    else:
        lista_noticias.append([title.text,' ',title["href"]])
        

news = pd.DataFrame(lista_noticias, columns=['Título', "Resumo", "Link"])
news.to_csv('g1/noticias.csv', index=False)#index false para não salvar o índice do DataFrame
news.to_excel('g1/noticias.xlsx', index=False)

print(news)

    

