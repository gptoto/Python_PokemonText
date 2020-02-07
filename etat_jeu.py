from enum import Enum

# Attribue un etat à la partie
class Etat_jeu(Enum):
    # Si ENCOURS, garde la fenêtre ouverte
    ENCOURS = 1,
    # Si COMBATFINI, ferme la fenêtre
    COMBATFINI = 2
    # SI TOURFINI, revient en haut de la boucle de combat
    TOURFINI = 3