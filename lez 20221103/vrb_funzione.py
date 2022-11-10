'''
Scrivere una funzione con due parametri in input
Creare una funzione annidata che ne calcola la somma
Quindi, un altra funzione somma 22 e restituisce il risultato.
'''

from curses import nonl

def funzGen(a, b):
  def somma():
    nonlocal a, b
    return a + b
  
  return somma()

def inc22(a):
  return a + 22

print(inc22(funzGen(2, 3)))
    
    
