'''
Calcolatrice
'''

def calcola(operazione, a, b):
  match operazione:
    case "somma":
      return a + b

    case "sottrai":
      return a - b

    case "moltiplica":
      return a * b

    case "dividi":
      return a / b

    case "eleva":
      return a ** b
    case other:
      return "Operazione non conosciuta"
    
print (calcola("somma", 4, 2))
print (calcola("sottrai", 4, 2))
print (calcola("moltiplica", 4, 2))
print (calcola("dividi", 4, 2))
print (calcola("eleva", 4, 2))
print (calcola("ciccia", 4, 2))

