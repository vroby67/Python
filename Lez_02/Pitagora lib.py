#inizializzo le variabili come float
import math

error = False
cat1=cat2=ipo=1.1
#Richiedo i cateti all'utente
print("Cateto-cateto: 1")
print("Cateto-ipotenusa: 2")
cosa=int(input("Cosa mi dai? "))
match cosa:
    case 1:
        cat1=float(input("Cateto 1: ")) #3
        cat2=float(input("Cateto 2: ")) #4
        res=math.sqrt((cat1 ** 2 + cat2 ** 2))
    case 2:
        cat1=float(input("Cateto 1: ")) #3
        ipo=float(input("Ipotenusa: ")) #4
        res=math.sqrt((ipo ** 2 - cat1 ** 2))
    case _:
        error = True
        print ("Errore")
if not error:
    print(res)
    

