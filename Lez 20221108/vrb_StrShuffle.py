'''
Scrivere un programma che richiede all’utente l’inserimento di una parola: 
• Convertire la parola in maiuscolo.
• Rimuovere le vocali dalla parola.
• Concatenare le lettere rimanenti formando una stringa ed assegnarla ad una nuova variabile. Stampare la nuova variabile
'''

myDict = {ord('A') : None, ord('E') : None, ord('I') : None, ord('O') : None, ord('U') : None}

wIn = input("Dammi una parola: ")
print ("Originale", wIn)
wIn = wIn.upper()
print ("Maiuscole", wIn)
wIn = wIn.translate(myDict)
print ("Svocalato", wIn)

