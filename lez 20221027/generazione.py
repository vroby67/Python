import numpy

nascita = input("Anno di nascita: ")
annas=int(nascita)
generaz=-1

if annas>1960 and annas<1970:
  generaz=0

if annas>1970 and annas<1980:
  generaz=1

if annas>1980 and annas<1990:
  generaz=2

if annas>1990 and annas<2000:
  generaz=3


print (generaz)