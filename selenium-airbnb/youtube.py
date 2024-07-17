import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_argument('window-size=1000,800')
browser = webdriver.Chrome(options=options)

browser.get('https://www.youtube.com')
sleep(0.5)
input_place = browser.find_element(By.TAG_NAME, 'input')
input_place.send_keys('Mano deivyn')
sleep(0.5)
input_place.submit()
sleep(0.5)
chanel = browser.find_element(By.CSS_SELECTOR, '.channel-link.ytd-channel-renderer')
sleep(1.5)
chanel.click()
site_content = BeautifulSoup(browser.page_source, 'html.parser')
print(site_content.prettify())

 

