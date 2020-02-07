

class Joueur:

    def __init__(self,nom, argent):
        self.nom = nom
        # Montant du porte-monnaie du joueur en pokédollars
        self.argent = argent

    def getMonnaie(self, argent):
        argent = 1000
        return self.argent

    def getNom(self, nom):
        return self.nom