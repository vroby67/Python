# python -m pip install requests
# python -m pip install beautifulsoup4
import numpy as np
import requests
from bs4 import BeautifulSoup
import re

# moduli per generare Excel
from datetime import datetime
import xlsxwriter 

def bikeSearch(URL, importoMin, importoMax):

    current_datetime = datetime.now().timestamp()
    str_current_datetime = str(current_datetime)
    file_name = str_current_datetime + '_' + 'la_mia_lista_di_bici.xlsx'
    
    # preparo la creazione del file Excel
    lista_bici = []

    paginaWeb = requests.get(URL)

    contenutoParsato = BeautifulSoup(paginaWeb .content, "html.parser")

    biciclette = contenutoParsato.find_all("div", class_="SmallCard-module_upper-data-group__aRFDu upper-data-group")

    listaRisultati = [] 
    cols=1

    for bici in biciclette:
        col = []

        titolo_offerta = bici.find("h2", class_="ItemTitle-module_item-title__VuKDo")
        luogo_offerta = bici.find("span", class_="index-module_town__2H3jy")
        prezzo_offerta = bici.find("p", class_="price")

        if titolo_offerta.text and luogo_offerta.text and prezzo_offerta.text:
            offerta = {'titolo': titolo_offerta.text, 'luogo': luogo_offerta.text, 'prezzo': prezzo_offerta.text}
        else:
            pass

        for j in range(cols):
            col.append(offerta)
        listaRisultati.append(col)
        
        a = np.array(listaRisultati)

    for x in a:
        for y in x:
            prezzo = y['prezzo']
            if prezzo == '':
                pass
            else:
                prezzo_finale = prezzo.replace("€", "")
                prezzo_finale = re.sub("[^0-9]", "", prezzo_finale)
                prezzo_finale = int(prezzo_finale)
                
                if prezzo_finale >= importoMin and prezzo_finale <= importoMax:
                        
                    workbook = xlsxwriter.Workbook('./' + file_name)
                    worksheet = workbook.add_worksheet()
                    lista_bici.append(y['titolo'] + y['prezzo'])

            for row_num, data in enumerate(lista_bici):
                worksheet.write(row_num, 0, data)

            workbook.close()
            
bikeSearch()