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
    #per capirci qualcosa, mi son cavato il link per poter vedere l'offerta dal vivo
    a_tag=bici.find("a", href=True)
    link_annuncio = a_tag['href']
    offerta = {'titolo': titolo_offerta.text, 'luogo': luogo_offerta.text, 'prezzo': prezzo_offerta.text, 'link': link_annuncio}

    for j in range(cols):
        col.append(offerta)
    listaRisultati.append(col)
    
    a = np.array(listaRisultati)

importoMax = int(input("Quanto vuoi spendere al massimo? : "))
importoMin = int(input("Quanto vuoi spendere al minimo? : "))

for x in a:
    for y in x:
        prezzoSrc = y['prezzo']
        num = "0"
        for numero in prezzoSrc:
            if numero == '':
                pass
            if numero.isdigit():
                num = num + numero
            prezzo = int(num)

        # Qualunque prezzo durante i cicli rientrasse nella forcella passava
        # anche se non erano ancora state raccolte tutte le cifre.
        if prezzo >= importoMin and prezzo <= importoMax:
            print("Ho trovato una bici che fa per te:", y['titolo'], y['prezzo'])
            print(y['link'])
            print(" ")
#            break

