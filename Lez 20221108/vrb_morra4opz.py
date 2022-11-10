'''
Esiste una variante del gioco della Morra Cinese in cui al sasso,
carta e forbici si aggiunge la candela.

Questa ha il potere di poter bruciare la carta
non può scottare chi ha il sasso
nulla può invece contro le forbici che la tagliano in due.
In questa variante le quattro scelte non sono equivalenti, 
dato che la carta perde in due casi su tre (avendo quindi un valore 
atteso di −1/3 contro un avversario che sceglie casualmente) 
mentre le forbici vince in due casi su tre ed ha quindi un valore atteso pari a +1/3
contro la strategia casuale.

Modificare il gioco sopra in modo che sia inclusa anche la Candela.
'''

from random import randint

t = ["Carta", "Sasso", "Forbici", "Candela", "Ciao"]

# tabella di verità delle combinazioni scelte da PC e giocatore
res = [[0, 1, 2, 2],\
       [2, 0, 1, 1],\
       [1, 2, 0, 1],\
       [1, 2, 2, 0]]

# Spiegazione verbosa per il giocatore
resTl = [["Pareggio", "Vinci: carta avvolge sasso", "Perdi: forbice taglia carta", "Perdi: candela brucia carta"],\
        ["Perdi: carta avvolge sasso", "Pareggio", "Vinci: sasso rompe forbice", "Vinci: sasso resiste a candela"],\
        ["Vinci: forbice taglia carta", "Perdi: sasso rompe forbice", "Pareggio", "Vinci: forbice taglia candela"],\
        ["Vinci: candela brucia carta", "Perdi: sasso resiste a candela", "Perdi: forbice taglia candela", "Pareggio"]]
 
# Spiegazione sintetica per debug
resTs = [["pp", "Pr", "pS", "pC"],\
         ["rP", "rr", "Rs", "rc"],\
         ["Sp", "sR", "ss", "Sc"],\
         ["Cp", "cR", "cS", "cc"]]
 

computer = t[randint(0,2)]

play = True

while play:
  computer = randint(0,2)
  giocatore = input("Sasso, Carta, Forbici, Candela o Ciao? ")
  
  if giocatore in t:
    plCh = t.index(giocatore)
    if plCh > 2:
      break
    win = res[plCh][computer]
    xpl = resTl[plCh][computer]
    print ("Ho scelto",t[computer], "! -", xpl)
  else:
    print("Hai inserito una parola sbagliata, riprova!")

  


