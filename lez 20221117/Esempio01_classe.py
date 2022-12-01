class Lavoro:
    ore_lavoro = 40 # Variabile Di Classe
   
    def __init__(self, nome, cognome, contratto):
        self.nome= nome
        self.cognome = cognome
        self.contratto = contratto
       
    def tipo_lavoro(self):      # Accedo alla variabile di istanza
            return f"Tipologia contratto:\n - OreIstanza: {self.ore_lavoro}\n - Nome: {self.nome}\n - Cognome: {self.cognome}\n - Contratto: {self.contratto}"

    def tipo_lavoro2(self):     # Accedo alla variabile di classe
            return f"Tipologia contratto:\n - OreClasse: {Lavoro.ore_lavoro}\n - Nome: {self.nome}\n - Cognome: {self.cognome}\n - Contratto: {self.contratto}"


nome_uno = Lavoro('Matteo', 'Rossi', 'full-time')
nome_due = Lavoro('Marco', 'Bianchi', 'full-time')
nome_tre = Lavoro('Dario', 'Verdi', 'full-time')
print(nome_uno.tipo_lavoro())
print(nome_uno.tipo_lavoro2())
print(nome_due.tipo_lavoro())
print(nome_due.tipo_lavoro2())
print(nome_tre.tipo_lavoro())
print(nome_tre.tipo_lavoro2())