'''
Scrivere un programma che richiede all’utente l’inserimento di una parola: 
• Convertire la parola in maiuscolo.
• Rimuovere le vocali dalla parola.
• Concatenare le lettere rimanenti formando una stringa ed assegnarla ad una nuova variabile. Stampare la nuova variabile
'''

myDict = {65 : None, 69 : None, 73 : None, 79 : None, 85 : None}

wIn = input("Dammi una parola: ")
print ("Originale", wIn)
wIn = wIn.upper()
print ("Maiuscole", wIn)
wIn = wIn.translate(myDict)
print ("Svocalato", wIn)

