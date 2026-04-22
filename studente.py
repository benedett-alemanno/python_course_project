class Studente:
    """La classe studente ha questi attributi."""

    def __init__(self, nome, abito, eta, matricola, voti):
        self.nome = nome
        self.abito = abito
        self.eta = eta
        self.matricola = matricola
        self.voti = voti

    def presentati(self):
        return f"Mi chiamo {self.nome}, abito a {self.abito}, ho {self.eta} anni, matricola {self.matricola}, voti: {self.voti}"

    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    def calcola_media(self):
        return sum(self.voti) / len(self.voti)

    def studia_ore(self, ore):
        return f"{self.nome} ha studiato per {ore} ore"

# Esempio con due studenti
studente1 = Studente('Lucia', 'Lecce', 25, 2007563, [27, 26, 22])
studente2 = Studente('Marco', 'Squinzano', 24, 2008123, [20, 28, 23])

print("STUDENTE 1")
print(studente1.presentati())
print(studente1.studia_ore(3))
studente1.aggiungi_voto(28)
print("Voti aggiornati:", studente1.voti)
print("Media:", studente1.calcola_media())

print("STUDENTE 2")
print(studente2.presentati())
print(studente2.studia_ore(4))
print("Voti:", studente2.voti)
print("Media:", studente2.calcola_media())
