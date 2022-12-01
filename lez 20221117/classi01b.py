class Lavoro:
    ore_lavoro = 40 # Variabile Di Classe
   
    def __init__(self, nome, cognome, contratto):
        self.nome= nome
        self.cognome = cognome
        self.contratto = contratto
       
    def tipo_lavoro(self):
            return f"Tipologia contratto:\n - Nome: {self.nome}\n - Cognome: {self.cognome}\n - Contratto: {self.contratto}\n - Ore lavoro: {self.ore_lavoro}"

nome_1 = Lavoro('Matteo', 'Rossi', 'full-time')
nome_2 = Lavoro('Marco', 'Bianchi', 'full-time')
nome_3 = Lavoro('Dario', 'Verdi', 'full-time')

nome_1.ore_lavoro=31
Lavoro.ore_lavoro=48

nome_4 = Lavoro('Piero', 'Faletti', 'full-time')
nome_5 = Lavoro('Giorgio', 'Picone', 'full-time')

#alterazione valore proprietà ore per utente 2
nome_2.ore_lavoro=32

#printout
print(nome_1.tipo_lavoro())
print(nome_2.tipo_lavoro())
print(nome_3.tipo_lavoro())
print("\nOre del nome 2", nome_2.ore_lavoro)

print(nome_4.tipo_lavoro())
print(nome_5.tipo_lavoro())
