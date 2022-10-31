n=0
trovato=False
secrWord="ppp"

while not trovato:
  risp=input("Indovina o luppamela: ")
  n+=1
  trovato = secrWord==risp
  if trovato:
    print ("Ok, ci hai preso al tentativo ", n)
