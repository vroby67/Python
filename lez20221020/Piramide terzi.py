"""
Scrivere un programma che calcola l'altezza di una piramide in base ai mattoni disponibili. Vedere immagini allegate.
"""
# verifica l'input dell'utente
def check_input(input):
    try:
        # converte in intero
        val = int(input)
        return True
    except ValueError:
        
        return False

# Metodo che trova i livelli della piramide
# da come risultato una tupla con numero di piani e la rimanenza
def pyramid_levels(bricks):
    levels = 0
    remaining_bricks = bricks
    more_levels = True
    while more_levels:
        if remaining_bricks >= (levels + 1):
            levels += 1
            remaining_bricks -= levels
        else:
            more_levels = False
    return levels, remaining_bricks

# disegna una riga di mattonele
def drawBricksRow( bricsNumber = 1, offset = 2, height = 2, width = 3, charRow = "-", charCol = "|"):
    space = " "
    # disegna la parte superiore
    print(offset* space + bricsNumber * ( 2 * space + width * charRow))
    # disegna la parte verticale
    for i in range(0, height):
        print(offset * space + bricsNumber * ( 2 * space + charCol + (width -2) * space +  charCol))
    # disegna la parte inferiore
    print(offset* space + bricsNumber * ( 2 * space + width * charRow))

# disegna la piramide dell'altezza desiderata
def drawPyramid(levels):
    for level in range(0, levels):
        offset = 4 + 6 * (levels - level)
        drawBricksRow(level + 1, offset = offset, height= 2, width = 10, charRow = ".", charCol= "|")


#
def runProgram():
    abort = False
    while not abort:
        number_of_bricks = input("Inserisci il numero di mattoni: ")
        if check_input(number_of_bricks):
            levels, remanins = pyramid_levels(int(number_of_bricks))
            print("Numero piani è ", levels)
            if remanins > 0:
                print("Avanzano {0} mattoni, sprecaccione".format(remanins))
            else:
                print("!!! Congratulazioni, non hai fatto sprecco di materiale !!!")
            drawPyramid(levels)
        print("")
        ask = input("Vuoi continuare?(s/n)")
        if ask.lower() == "n":
            abort = True

runProgram()


