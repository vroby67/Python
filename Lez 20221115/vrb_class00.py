class Film:
  Titolo = ''
  Regista = ''
  Anno = ''
  
  
  def __init__(self, titolo, regista, anno):
    self.Titolo = titolo
    self.Regista = regista
    self.Anno = anno

  def printOut(self):
    print('Scheda del film')
    print('\tTitolo:', self.Titolo)
    print('\tRegista:', self.Regista)
    print('\tAnno di edizione:', self.Anno)
    print ('\n')

#-----------------------------------------------------------

film_uno = Film('Swordfish', 'Dominic Sena', 2001)
film_due = Film('Snowden', 'Oliver Stone', 2016)
film_tre = Film('Taxi Driver', 'Martin Scorsese', 1976)

print("Chiamata metodo oggetto fisso")
film_due.printOut()

print("\n\nChiamata proprietà oggetto fisso")
print(film_uno.Titolo)
print(film_uno.Regista)
print(film_uno.Anno)

ml=[film_uno]
ml.append(Film('Snowden', 'Oliver Stone', 2016))
ml.append(Film('Taxi Driver', 'Martin Scorsese', 1976))

print("\n\nChiamata oggetto in lista")
print (ml[0])
print("\n\nChiamata proprietà oggetto in lista")
print (ml[0].Titolo)


print("\n\nChiamata proprietà in lista ciclata")
for f in ml:
  print(f.Titolo)
  print(f.Regista)
  print(f.Anno)

print("\n\nChiamata metodo in lista ciclata")
for f in ml:
  f.printOut()
