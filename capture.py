import time
import sys
import pokemonCapture
from random import randint, random, choice

def delay_print(s):
    # Affiche petit à petit un élément
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

class Capture:

    def __init__(self, name, types, moves, EVs, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Nombre de barres de PV

    def fight(self, Pokemon2):
        print("-----POKEMON BATTLE-----\n")
        print(f"Un {Pokemon2.name} sauvage est apparu !\n")
        print(f"Go {self.name} !")

        time.sleep(2)

        # Avantages de types (Pokémon et non attaques)
        version = ['Feu', 'Eau', 'Plante']
        for i,k in enumerate(version):
            if self.types == k:
                # Même types
                if Pokemon2.types == k:
                    string_1_attack = '\nCe n\'est pas très efficace...\n'
                    string_2_attack = '\nIts not very effective...\n'

                # Pokemon2 > Pokemon1
                if Pokemon2.types == version[(i+1)%3]:
                    Pokemon2.attack *= 2
                    Pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2
                    string_1_attack = '\nCe n\'est pas très efficace...\n'
                    string_2_attack = '\nC\'est très efficace !\n'

                # Pokemon1 > Pokemon2
                if Pokemon2.types == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    Pokemon2.attack /= 2
                    Pokemon2.defense /= 2
                    string_1_attack = '\nC\'est très efficace !\n'
                    string_2_attack = '\nCe n\'est pas très efficace...\n'


        while (self.bars > 0) and (Pokemon2.bars > 0):
            # Affichage de la santé
            print(f"\n{self.name}\t\tPV\t{self.health}")
            print(f"{Pokemon2.name}\t\tPV\t{Pokemon2.health}\n")

            print("1) Attaquer.")
            print("2) Capturer.")
            choix = int(input('Sélectionnez une action : '))

            while True:
                # Choix de capturer ou d'attaquer
                if (choix==1):
                    # Liste les attaques du pkmn en question
                    for i, x in enumerate(self.moves):
                        print(f"{i + 1}.", x)

                    index = int(input('Sélectionnez un attaque : '))

                    if (index > 4):
                        print("Veuillez selectionner une attaque valide.")
                        while (index > 4):
                            index = int(input('Sélectionnez un attaque : '))
                    elif (index <= 4):
                        delay_print(f"\n{self.name} utilise {self.moves[index - 1]}!")

                    time.sleep(1)
                    delay_print(string_1_attack)

                    # Dêgats infligés
                    Pokemon2.bars -= self.attack
                    Pokemon2.health = ""

                    # Prise en compte de la défense
                    for j in range(int(Pokemon2.bars + .1 * Pokemon2.defense)):
                        Pokemon2.health += "="

                    time.sleep(1)
                    print(f"\n{self.name}\t\tPV\t{self.health}")
                    print(f"{Pokemon2.name}\t\tPV\t{Pokemon2.health}\n")
                    time.sleep(.5)

                    # Test si K.O ou non
                    if Pokemon2.bars <= 0:
                        delay_print("\n..." + Pokemon2.name + ' est K.O.')

                    # Retour au menu
                    exec(open("main.py").read())


                    # Tour du pokémon sauvage
                    index = randint(0, 3)
                    delay_print(f"\n{Pokemon2.name} utilise {Pokemon2.moves[index - 1]}!")
                    time.sleep(1)
                    delay_print(string_2_attack)

                    # Dêgats infligés
                    self.bars -= Pokemon2.attack
                    self.health = ""

                    # Prise en compte de la défense
                    for j in range(int(self.bars + .1 * self.defense)):
                        self.health += "="

                    time.sleep(1)
                    print(f"{self.name}\t\tPV\t{self.health}")
                    print(f"{Pokemon2.name}\t\tPV\t{Pokemon2.health}\n")
                    time.sleep(.5)

                    # Test si K.O ou non
                    if self.bars <= 0:
                        delay_print("\n..." + self.name + ' est K.O.')

                    # Retour au menu
                    exec(open("main.py").read())


                elif (choix==2):
                    True
                    tauxcapture = 10

                    print("\n1) Pokéball.")
                    print("2) Superball.")
                    print("3) Hyperball.")
                    print("4) Masterball.\n")
                    ball = int(input("Sélectionnez une ball : "))

                    # % de capture Selon choix ball
                    if (ball == 1):
                        nomBall = 'Pokéball'
                        tauxcapture = tauxcapture*2.5 #25% pour Pokéball
                    elif (ball == 2):
                        nomBall = 'Superball'
                        tauxcapture = tauxcapture * 4.5 #35% pour Superball
                    elif (ball == 3):
                        nomBall = 'Hyperball'
                        tauxcapture = tauxcapture * 5.5 #55% pour Hyperball
                    elif(ball == 4):
                        nomBall = 'Masterball'
                        tauxcapture = tauxcapture * 10 #100% pour MasterBall
                    else:
                        "Veuillez sélectionner un choix valide."
                        break

                    print(f"Joueur 1 lance une {nomBall} !")

                    time.sleep(1)

                    capture = 1*tauxcapture
                    if (randint(0,100) < capture):
                        delay_print("...")
                        print(f"Vous avez capturé {Pokemon2.name} !")

                        # Met fin au script
                        time.sleep(5)
                        break

                        # Retour au menu
                        exec(open("main.py").read())

                    else :
                        delay_print("...")
                        print("Le pokemon s'est échappé.")
                        break
                else:
                    print("Veuillez sélectionner un choix valide.")
                    break


if __name__ == '__main__':

    pokemonCapture.getRandomPkmn()
    # On charge les infos du premier pokémon
    # pkmn1 = pokemonCapture.getRandomPkmn() #Si Pokémon du joueur aléatoire
    pkmn1= pokemonCapture.Salameche #Si Pokémon du joueur statique

    # On charge les infos du deuxième pokémon
    pkmn2 = pokemonCapture.getRandomPkmn()

    # Lance le combat avec les deux pokémons sélectionnés
    pkmn1.fight(pkmn2)