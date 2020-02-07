import os
import time
import sys

import pokemonCombat
# Delay printing
from random import randint, random, choice


def delay_print(s):
    # Affiche petit à petit un élément
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


class Combat:

    def __init__(self, name, types, moves, EVs, health='==================='):
        self.name = name
        self.types = types
        self.moves = moves
        self.attack = EVs['ATTACK']
        self.defense = EVs['DEFENSE']
        self.health = health
        self.bars = 20 # Nombre de barres de PV

    def fight(self, Pokemon2):

        # Print fight information
        print("-----POKEMON BATTLE-----")
        print(f"\n{self.name}")
        print("TYPE/", self.types)
        print("ATTACK/", self.attack)
        print("DEFENSE/", self.defense)

        print("\nVS")
        print(f"\n{Pokemon2.name}")
        print("TYPE/", Pokemon2.types)
        print("ATTACK/", Pokemon2.attack)
        print("DEFENSE/", Pokemon2.defense)


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

            print(f"Go {self.name}!")
            # Liste les attaques du pkmn en question
            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)

            index = int(input('Sélectionnez un attaque : '))
            if (index > 4):
                print("Veuillez selectionner une attaque valide.")
                while (index > 4):
                    index = int(input('Sélectionnez un attaque : '))
            elif (index <= 4):
                delay_print(f"\n{self.name} utilise {self.moves[index-1]}!")

            time.sleep(1)
            delay_print(string_1_attack)

            # Dêgats infligés
            Pokemon2.bars -= self.attack
            Pokemon2.health = ""

            # Prise en compte de la défense
            for j in range(int(Pokemon2.bars+.1*Pokemon2.defense)):
                Pokemon2.health += "="

            time.sleep(1)
            print(f"\n{self.name}\t\tPV\t{self.health}")
            print(f"{Pokemon2.name}\t\tPV\t{Pokemon2.health}\n")
            time.sleep(.5)

            # Test si K.O ou non
            if Pokemon2.bars <= 0:
                delay_print("\n..." + Pokemon2.name + ' est K.O.')
                break

            # Retour au menu
            exec(open("main.py").read())

            # Tour du 2e Pkmn
            print(f"Go {Pokemon2.name}!")
            for i, x in enumerate(Pokemon2.moves):
                print(f"{i+1}.", x)

            index = int(input('Sélectionnez un attaque: ')) # A modifier avec randint(0,3) si l'on veut une attaque aléatoire du 2e pkmn.
            if (index > 4):
                print("Veuillez selectionner une attaque valide.")
                while (index > 4):
                    index = int(input('Sélectionnez un attaque : '))
            elif (index <= 4):
                delay_print(f"\n{Pokemon2.name} utilise {Pokemon2.moves[index - 1]}!")
            time.sleep(1)
            delay_print(string_2_attack)

            # Dégâts infligés
            self.bars -= Pokemon2.attack
            self.health = ""

            # Prise en compte de la défense
            for j in range(int(self.bars+.1*self.defense)):
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

        # Argent gagné
        gain = randint(0,500)
        delay_print(f"\nAdversaire vous paie ${gain}.\n")
        # Ajout de l'argent au porte feuille du joueur
        # Red.argent = Red.argent + gain
        # print(objectMagasin.Red.argent)
        time.sleep(5)

        #Retour au menu
        exec(open("main.py").read())

if __name__ == '__main__':

    pokemonCombat.getRandomPkmn()
    # On charge les infos du premier pokémon
    pkmn1 = pokemonCombat.getRandomPkmn()
    # On charge les infos du deuxième pokémon
    pkmn2 = pokemonCombat.getRandomPkmn()
    # Lance le combat avec les deux pokémons sélectionnés
    pkmn1.fight(pkmn2)