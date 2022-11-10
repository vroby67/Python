# apro il file
from asyncore import write
from curses.ascii import isblank

pathSrc = "C:\\Documenti\\Git\\v0449-shared\\v0449-shared\\CL\defAna.txt"
pathDest = "C:\\Documenti\\temPythonAna\\"

# estrazione di tutte le definizioni delle analogiche
# restituisce una matrice con tutte le definizioni trovate
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
        if line.find("header:enum")>-1:
          # rimuovo il tag 'enum ' e ricavo definizione nome
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
          enumList=appList
          appList = []
          waid = "cercoDescr"
        
      case "cercoDescr":
        if line.find("header:descr")>-1:
          waid = "caricoDescr"
          wailf = "aproGraffa"
        pass

      # membro 1 - descr
      case "caricoDescr":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          descrList=appList
          appList = []
          waid = "cercoNick"
        pass
          
      case "cercoNick":
        if line.find("header:nick")>-1:
          waid = "caricoNick"
          wailf = "aproGraffa"
        pass

      # membro 2 - nick
      case "caricoNick":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          nickList=appList
          appList = []
          waid = "cercoLbS"
        pass

      case "cercoLbS":
        if line.find("header:labelShort")>-1:
          waid = "caricoLbS"
          wailf = "aproGraffa"
        pass

      # membro 3 - PLC
      case "caricoLbS":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          plcList=appList
          appList = []
          waid = "cercoLbL"
        pass  

      case "cercoLbL":
        if line.find("header:labelLong")>-1:
          waid = "caricoLbL"
          wailf = "aproGraffa"
        pass

      # membro 4 - comp
      case "caricoLbL":
        appList, wailf = ricavoOggetto(line, appList, wailf, waid)
        
        if wailf == "finito":
          compList=(appList)
          wordList=[enumList, descrList, nickList, plcList, compList]
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
        if not line.isspace() and len(line):
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

    #{
    # "Di0":{
    #   "RegIdx": 0,
    #   "Name" : "Di0",
    #   "Description" : "Prima word ingressi",
    #   "type": "BitInt",
    #   "Unit": "n",
    #   "Fields":{

  
def componiJson(benchList):
  
  # livello 0: banchi (387, 449a, 449b...)
  # banco è una linea di benchlist
  fOut = open(pathDest + "analog.model.json", "w")
  #{
  fOut.write("{") # + "\n")
  oft = 0

  for row in range(0, len(benchList[0])):
    
    # livello 1: words (we0, we1, we2...)
    if oft:
      fOut.write(',\n')
    fOut.write('\n\n')

    # "Di0":{
    fOut.write('\t"' + benchList[0][row] + '": {' + "\n")
    #   "RegIdx": 0,
    fOut.write('\t\t"RegIdx" : ' + str(oft) + ',' + "\n")
    #   "Name" : "Di0",
    fOut.write('\t\t"Name" : "' + benchList[0][row] + '",' + "\n")
    #   "Description" : "Prima word ingressi",
    fOut.write('\t\t"Description" : "' + benchList[1][row] + '", \n')
    #   "type": "BitInt",
    fOut.write('\t\t"type" : "analChannel",' + "\n")
    #   "Unit": "n",
    fOut.write('\t\t"Unit" : "d",' + "\n")
    #   "Fields":{
    fOut.write('\t\t"Fields" : {' + "\n\t\t\t}\n")
    # livello 2: sezioni (enum, descr, nick...)
    

    oft += 1

    fOut.write('\t\t}\n\t}')
  fOut.write('\n}\n')
  
      
        
          


  