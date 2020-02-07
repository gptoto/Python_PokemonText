import sys
import time
import keyboard

from joueur import Joueur


def delay_print(s):
    # Affiche petit à petit un élément
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class ObjectMagasin:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def vente(self):
        print("")


if __name__ == '__main__':
    # Joueur actuel
    Red = Joueur('Red',1000)

    # Objets
    Pokeball = ObjectMagasin("Pokeball", 250)
    Superball = ObjectMagasin("Superball", 600)
    Hyperball = ObjectMagasin("Hyperball", 1000)

    ObjectList = [Pokeball, Superball, Hyperball]  # Insert à Rendre automatique
    print("\n[================================= MAGASIN =================================]")

    i = 1  # Indice dans la liste
    for element in range(len(ObjectList)):
        ObjectList.append(element)
        # Ajout de ligne dynamique
        print(
            f"                             {i}) {ObjectList[element].name} : {ObjectList[element].price} $                           ")
        i = i + 1

    print("                                                                                       ")
    print("                               ESC pour quitter ")
    print("[===========================================================================]")

    choix = int(input("                           Que voulez-vous acheter ?"))

    # Gérer inventaire
    # Si ESC, quitter


    while True:
        if keyboard.is_pressed('Esc'):
            exec(open("main.py").read())
        # Si un objet est présent dans la liste
        elif choix < len(ObjectList):
            nomBall = ObjectList[choix].name
            prixBall = ObjectList[choix].price

            if Red.argent < prixBall:
                print("Solde insuffisant.")
            else:
                print( nomBall+" achetÃ©(e)")
                # Soustraire montant de la balle à argent du joueur
                Red.argent = Red.argent - prixBall
                time.sleep(5)
                break
        else:
            # Ne passe pas dedans
            print("Veuillez entrer une réponse valide.")
