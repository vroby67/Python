"""
Mettiamo alla prova la natura di calcolatrice estesa del 
computer risolvendo un classico problema di economia: 
“Se depositiamo in banca 100 € a un tasso di interesse annuo 
del 3% quanti soldi avremo dopo 10 anni?”

All’inizio abbiamo 100 €, dopo un anno si aggiungono i 3 € 
di interesse portando il nostro capitale a 103 €, 
dopo 2 anni maturano altri 3,09 € di interesse 
(infatti, 103 · 0,03 = 3,09) e il capitale diventa 106,09 € e così via.

I dati di ingresso con cui abbiamo a che fare sono i seguenti:

capitale iniziale (Ci);
capitale finale (Cf), in economia si chiama anche “montante”, 
perché nel corso degli anni, se il tasso di interesse è positivo, il suo valore aumenta;
tasso di interesse annuo (tasso), è la percentuale di interesse che la banca riconosce dopo un anno di 
deposito del capitale; numero di anni (n) di deposito.

Utilizziamo la seguente formula per il calcolo dell’interesse composto 
 (si chiama composto perché l’interesse
  si calcola sia sul capitale iniziale che sull’interesse accumulato fino 
  all’anno precedente):

Cf = Ci(1 + tasso) ^ n
"""
import math

ci = float(input("Capitale iniziale: "))
ti = float(input("Tasso d'interesse: ")) / 100
durata = float(input("Durata in anni: "))

cf = ci * (1 + ti)**durata

print("Capitale finale: ", round(cf, 2))