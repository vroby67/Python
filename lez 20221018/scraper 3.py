import requests
from bs4 import BeautifulSoup
 
# Url sito
r = requests.get('https://vbanet.eu/')
 
# analisi HTML
soup = BeautifulSoup(r.content, 'html.parser')
 
# trova tutti gli anchor tags con "href"
for link in soup.find_all('a'):
    print(link.get('href'))