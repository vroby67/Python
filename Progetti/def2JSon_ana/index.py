from genericpath import isdir, isfile
from functions import *
import os
import pathlib

benchList = []

# Richiesta percorsi di lavoro
'''
print( "Percorso e nome sorgenti: \n", pathSrc)
tmp = input()
if len(tmp) > 0:
  if os.path.isfile(tmp):
    pathSrc=tmp
  else: 
    print("File non trovato, mantengo il default")
    

print( "Percorso destinazione: \n", pathDest)
tmp = input()
if len(tmp) > 0:
  if os.path.isdir(tmp):
    pathDest=tmp
  else: 
    print("Cartella non trovata, mantengo il default")
'''

if not os.path.isdir(pathDest):
  pathlib.Path(''.join(pathDest.rpartition("\\")[0:2])).mkdir(parents=True, exist_ok=True)

# Estrazione dati e separazione in files sezione
benchList = getElements(pathSrc)


  
componiJson(benchList)
#testData(benchList)

pass