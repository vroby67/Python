numeriDaInserire = int(input("quanti interi vuoi inserire?"))
contatore = 1
interoMax = int(input("inserisci un intero"))
while contatore < numeriDaInserire:
      intero = int(input("inserisci un intero"))
      if intero > interoMax :
          interoMax = intero
      contatore += 1
print("il massimo vale", interoMax )