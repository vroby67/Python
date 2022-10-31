#inizializzo le variabili come float
import math

caption="Il risultato è: "
error = False
area=base=altezza=1.1
#Richiedo i cateti all'utente
print("Lato triangolo equilatero: 1")
print("Area triangolo equilatero: 2")

cosa=int(input("Cosa mi dai? "))
decPlaces=int(input("Quanti decimali vuoi? "))
match cosa:
    case 1:
        lato=float(input("lato: ")) #3
        altezza=lato*math.sqrt(3)/2
        area=lato*altezza/2
    case 2:
        #futuro sviluppo
        area=float(input("area: ")) #3
        altezza=area*2/1
    case _:
        error = True
        print ("Errore")
if not error:
    print(area, altezza)
    print("Il lato vale: ", round(lato, decPlaces))
    print("L'area vale: ", round(area, decPlaces))
    print("L'altezza vale: ", round(altezza, decPlaces))

    

