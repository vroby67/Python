#Conversione bidirezionale miglia km
#===================================

caption="Il risultato è: "
error = False
kMiles = 1.609

#Richiedo i dati all'utente
print("Miglia in Km: 1")
print("Km in miglia: 2")
cosa=int(input("Cosa mi dai? "))
decPlaces=int(input("Quanti decimali vuoi? "))

match cosa:
    case 1:
        res = float(input("Miglia ")) * kMiles 
    case 2:
        res = float(input("Km ")) / kMiles 
    case _:
        error = True
        print ("Errore selezione")


if type(decPlaces) == int and decPlaces>=0 and decPlaces<=9 and not error:
    print(caption, round(res, decPlaces))
else:
    print ("errore inserimento parametri")
    