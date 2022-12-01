class Lavoro:
    ore_lavoro = 40 # Variabile Di Classe
   
    def __init__(self, nome, cognome, contratto):
        self.nome= nome
        self.cognome = cognome
        self.contratto = contratto
       
    def tipo_lavoro(self):
            return f"Tipologia contratto:\n - Nome: {self.nome}\n - Cognome: {self.cognome}\n - Contratto: {self.contratto}\n - ore_lavoro: {self.ore_lavoro}"

nome_uno = Lavoro('Matteo', 'Rossi', 'full-time')
nome_uno.ore_lavoro+=2
nome_due = Lavoro('Marco', 'Bianchi', 'full-time')
nome_due.ore_lavoro+=3
nome_tre = Lavoro('Dario', 'Verdi', 'full-time')
nome_tre.ore_lavoro+=4
print(nome_uno.tipo_lavoro())
print(nome_due.tipo_lavoro())
print(nome_tre.tipo_lavoro())

'''
python -m django --version
python -m pip install Django
python manage.py migrate
python manage.py runserver
'''