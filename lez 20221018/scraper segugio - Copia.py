# python -m pip install requests
# python -m pip install beautifulsoup4
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.subito.it/annunci-italia/vendita/usato/?q=mtb&from=top-bar"
paginaWeb = requests.get(URL)

contenutoParsato = BeautifulSoup(paginaWeb .content, "html.parser")

biciclette = contenutoParsato.find_all("div", class_="items__item item-card item-card--small")

listaRisultati = [] 
cols=1

for bici in biciclette:
    col = []

    titolo_offerta = bici.find("h2", class_="ItemTitle-module_item-title__VuKDo")
    luogo_offerta = bici.find("span", class_="index-module_town__2H3jy")
    prezzo_offerta = bici.find("p", class_="price")
    a_tag=bici.find("a", href=True)
    link_annuncio = a_tag['href']
    
    offerta = {'titolo': titolo_offerta, 'luogo': luogo_offerta, 'prezzo': prezzo_offerta, 'link': link_annuncio}
 
    for j in range(cols):
        col.append(offerta)
    listaRisultati.append(col)
    
    a = np.array(listaRisultati)

importoMax = 2000#int(input("Quanto vuoi spendere al massimo? : "))
importoMin = 1500#int(input("Quanto vuoi spendere al minimo? : "))

for x in a:
    for y in x:
        prezzoSrc = y['prezzo']
        titolo = y['titolo']
        num = "0"
        for numero in prezzoSrc:
            if numero == '' or numero == 'S' or numero == '.':
                numero = ''
            if numero.isdigit():
                num = num + numero
            #if 
            prezzo = int(num)
            
            res=titolo.find("Viko TRK Lady")
            
            if res >= 0:
                pass
            
            if importoMin <= prezzo and prezzo <= importoMax:
                print("Ho trovato una bici che fa per te:", y['titolo'], y['prezzo'])
                print(y['link'])
                print(" ")
                break

