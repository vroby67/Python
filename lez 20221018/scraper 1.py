import requests
from bs4 import BeautifulSoup

# Url sito
r = requests.get('https://ahrefs.com/blog/it/cannibalizzazione-parole-chiave/')
# Analisi HTML
soup = BeautifulSoup(r.content, 'html.parser')
# title tag
print(soup.title)
# h1
print(soup.h1)
# h2
print(soup.h2)
# h3
print(soup.h3)