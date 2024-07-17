from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome()

navegador.get('https://www.youtube.com')
time.sleep(3)
el = navegador.find_element(By.NAME, 'search_query')

el.send_keys('Web scraping com python')

while True:
    time.sleep(1)