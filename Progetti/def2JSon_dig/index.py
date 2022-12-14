from genericpath import isfile
from functions import *
import os, fnmatch

benchList = []

# Richiesta percorsi di lavoro

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


# Estrazione dati e separazione in files sezione
splitAndSave(pathSrc, pathDest)

# ricavo la lista escludendo cartelle e files indesiderati
filesIn = fnmatch.filter(os.listdir(pathDest), '*.txt')

for file in filesIn:
  benchList.append([file, getElements(pathDest + file)])
  
componiJson(benchList)
#testData(benchList)

pass