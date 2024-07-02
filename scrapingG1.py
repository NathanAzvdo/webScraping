import requests
from bs4 import BeautifulSoup



response = requests.get('https://g1.globo.com/')
content = response.content

site =BeautifulSoup(content)

notice = site.find('div', attrs={'class': 'feed-post-body'})
title = notice.find('a', attrs={'class': 'feed-post-link'})
resumo = notice.find('div', attrs={'class': 'feed-post-body-resumo'})




print(title.text)
print(resumo.text)