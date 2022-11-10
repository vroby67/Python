# Gioco Carta Forbici Sasso.
# Il programmatore del gioco ha commesso una distrazione e il bug impedisce 
# l'esecuzione corretta del programma.
# Individuare il bug e far funzionare correttamente il gioco!
# Infine aggiungere la funzionalità richiesta nei commenti sottostanti


from random import randint

t = ["Sasso", "Carta", "Forbici", ]

computer = t[randint(0,2)]

play = True

while play:
    giocatore = input("Sasso, Carta, Forbici, Ciao? ")
    if giocatore == computer:
        print("Avete pareggiato")
    elif giocatore == "Sasso":
        if computer == "Carta":
            print("Hai perso!", computer, "avvolge", giocatore)
        else:
            print("Hai vinto!", giocatore, "rompe", computer)
    elif giocatore == "Carta":
        if computer == "Forbici":
            print("Hai perso!", computer, "tagliano", giocatore)
        else:
            print("Hai vinto!", giocatore, "avvolge", computer)
    elif giocatore == "Forbici":
        if computer == "Sasso":
            print("Hai perso...", computer, "rompe", giocatore)
        else:
            print("Hai vinto!", giocatore, "tagliano", computer)
    elif giocatore == "Ciao" or not giocatore:
      play = False
    else:
        print("Hai inserito una parola sbagliata, riprova!")

    giocatore = False
    computer = t[randint(0,2)]
