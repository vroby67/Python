# apro il file
from asyncore import write
from curses.ascii import isblank

pathSrc = "C:\\Documenti\\temPython\\input\\def.cs"
pathDest = "C:\\Documenti\\temPython\\"
pathCs = "C:\\Documenti\\Git\\v0449-shared\\v0449-shared\\CL\\DEF\\benches\\"

# estrazione dal DEF di tutte le sezioni paundiffate con estrazione del nome banco
##################################################################################
def splitAndSave(pathSrc, pathDest):
  fIn = open(pathSrc, "r")
  fOut = open(pathDest + "trash", "w")

  # scansiono tutto il file
  for fLine in fIn:
    # cerco il tag di regione banco per il cambio file
    # (estrazione sezione)
    if fLine.find("#if ")>=0 or fLine.find("#elif ")>=0:
      # apro un file per esportare la regione intera
      fOut.close()
      # genero nome file
      sectionName = fLine[fLine.index(" ") + 1 : ]
      # sectionName = fLine.split(" ")[1]
      # rimuovo il CR alla fine
      sectionName = sectionName.rstrip("\n")
      # elimino i simboli |
      sectionName = sectionName.replace("|", "_")
      # elimino gli spazi superflui
      sectionName = sectionName.replace(" ", "")
      
      # apro il file in scrittura
      fOut = open(pathDest + sectionName + ".txt", "w")
    
    # aggiungo tutte le linee della sezione
    fOut.write(fLine)
  
  
# estrazione di tutte le definizioni per ciascuna word
# restituisce una matrice con tutte le definizioni trovate per:
# input, output e allarmi
###############################################################
def getElements(filena):
  fIn = open(filena, "r")
  lines = [line.rstrip() for line in fIn]
  
  wordList = []
  appList = []
  
  # What Am I Doing = niente
  waid = "niente"
  # spazzolo tutto il buffer (file)
  for line in lines:
    # What Am I Doing
    match waid:
      # cerco a spasso qualcosa di utile
      # e non ho trovato nulla (nessun oggetto aperto)
      case "niente":
        # cerco marker apertura definizione oggetto
        if line.find("enum W")>-1:
          # rimuovo il tag 'enum ' e ricavo definizione nome
          wDef = line.rstrip()[line.index("enum W") + 5:]
          # ricavo il numero word per escludere i fonfi xxx
          wNum = wDef.rstrip()[-1:]
          # quindi, se il numero è un numero
          if wNum.isdigit():
            # ho trovato l'entry point di uno degli oggetti da estrarre
            wNum = int(wNum)
            enumList=[]  
            descrList=[]
            nickList=[]
            plcList=[]
            compList=[]
            appList = []
            waid = "caricoEnum"
            wailf = "aproGraffa"
        pass
            
      # membro 0 - enum
      case "caricoEnum":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          enumList = [wDef + "enum", appList]
          appList = []
          waid = "cercoDescr"
        
      case "cercoDescr":
        if line.find("Descr")>-1:
          # 
          secDef = line.rstrip()[line.index("Descr") - 3::8]
          waid = "caricoDescr"
          wailf = "aproGraffa"
        pass

      # membro 1 - descr
      case "caricoDescr":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          descrList = [wDef + "descr", appList]
          appList = []
          waid = "cercoNick"
        pass
          
      case "cercoNick":
        if line.find("Nick")>-1:
          # 
          secDef = line.rstrip()[line.index("Nick") - 3::8]
          waid = "caricoNick"
          wailf = "aproGraffa"
        pass

      # membro 2 - nick
      case "caricoNick":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          nickList = [wDef + "nick", appList]
          appList = []
          waid = "cercoPlc"
        pass

      case "cercoPlc":
        if line.find("Plc")>-1:
          # 
          secDef = line.rstrip()[line.index("Plc") - 3::8]
          waid = "caricoPlc"
          wailf = "aproGraffa"
        pass

      # membro 3 - PLC
      case "caricoPlc":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          plcList = [wDef + "plc", appList]
          appList = []
          waid = "cercoComp"
        pass  

      case "cercoComp":
        if line.find("Comp")>-1:
          # 
          secDef = line.rstrip()[line.index("Comp") - 3::8]
          waid = "caricoComp"
          wailf = "aproGraffa"
        pass

      # membro 4 - comp
      case "caricoComp":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          compList = [wDef + "comp", appList]
          '''if len(wordList):
            wordList.append([wDef, [enumList, descrList, nickList, plcList, compList]])
          else:
            wordList = [wDef, [enumList, descrList, nickList, plcList, compList]]
          '''
          wordList += [[wDef, [enumList, descrList, nickList, plcList, compList]]]
          waid = "altraWord"
        pass  

      case "altraWord":
          
        waid = "niente"
        pass
    
  return wordList
      

# Estrazione sezione word
# scarta la graffa iniziale, aggiunge tutte le definizioni
# scarta la graffa finale e ritorna la lista
##########################################################
def ricavoOggetto(line, partList, wailf, waid):

  match wailf:
    case "aproGraffa":
      # cerco marker apertura definizione oggetto
      if line.find("{")>-1:
        #wailf = "scartoCarattere"
        wailf = "collezionoElementi"
      pass
    
    case "collezionoElementi":
      if line.find("}")>-1:
        wailf = "fineOggetto"
        mancano = 16 - len(partList)
        for n in range (mancano):
          partList.append("dummy")
      else: 
        if not line.isspace():
          if waid == "caricoEnum":
            partList.append(line.replace(",", "").replace(" ", ""))
          else:
            partList.append(line.lstrip().replace(",", "").replace('"', "").rstrip())
    
    case "fineOggetto":
      wailf = "finito"
  
  return partList, wailf


# Composizione file definizione oggetti
#######################################
def testData(benchList):
  fOut = open(pathDest + "output\\tempList.txt", "w")
  
  # livello 0: banchi (387, 449a, 449b...)
  # banco è una linea di benchlist
  for banco in benchList:
    fOut.write(banco[0] + "\n")
    
    # livello 1: words (we0, we1, we2...)
    for word in banco[1]:
      fOut.write("\t - liv 1 - " + word[0] + "" + "\n")

      # livello 2: sezioni (enum, descr, nick...)
      for sezContainer in word[1]:
        fOut.write("\t\t - liv 2 - \n")

        for sezione in sezContainer:
          fOut.write("\t\t - liv 3 - " +sezione[0] + "" + "\n")

          # livello 3: 
          for field in sezione[1]:
            fOut.write("\t\t\t - liv 4 - " + field + "\n")


# Riassemblo le chiavi estratte ed ordinate nel json di configurazione
# Viene creato il modello di configurazione per ciascun impianto
######################################################################
def componiJson(benchList):
  
  # livello 0: banchi (387, 449a, 449b...)
  # banco è una linea di benchlist
  for banco in benchList:
    fOut = open(pathCs + banco[0][:-4] + "_dio.cs", "w")
    #{
    text = '''using System;
using System.Collections.Generic;
using System.Text;
using v0449_shared.CL.DEF;

namespace v0449_shared.CL.DEF.benches
{
  public class _'''
    fOut.write(text) # + "\n")
    fOut.write(banco[0][1:5] + 'dio\n\t{')

    oft = 0

    # livello 1: words (we0, we1, we2...)
    oldType=""
    for word in banco[1]:
      if oft:
        fOut.write(',\n')
      fOut.write('\n\n')

      # "Di0":{
      if word[0][0:2] != oldType:
        #se non è la prima, chiude la parentesi della precedente
        if oldType:
          fOut.write('\t\t};\n\n')
        
        oldType = word[0][0:2]
        fOut.write('\t\tpublic wBitInt[] ' + word[0][0:2] + '= new wBitInt[]\n\t\t{\n')
      #   "RegIdx": 0,
      fOut.write('\t\t\tnew wBitInt((int)wBitInt.types.' + word[0][0:2] + ', ' + word[0][-1]+', "' + word[0] +'", "' + word[0] + '", new lBitInt[]\n'+'\t'*3+'{\n')

      # livello 2: sezioni (enum, descr, nick...)
      for row in range (0, 16):
        fOut.write('\t' * 4) 
        #new fino al n° bit
        fOut.write('new lBitInt(' + str(row) + ', "')
        fOut.write(word[1][0][1][row] + '", "')
        fOut.write(word[1][1][1][row] + '")')
        if row < 15:
          fOut.write(',')
        fOut.write('\n')
      oft += 1

      fOut.write('\t\t\t})')
    fOut.write('\n\t\t};\n\t}\n}\n')
  pass
