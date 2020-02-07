from random import randint
from combat import Combat


# Liste contenant les pokémons
listPokemons = []

Salameche = Combat('Salameche', 'Feu', ['Flammèche', 'Griffe', 'Charge', 'Poing de feu'], {'ATTACK': 4, 'DEFENSE': 2})
Reptincel = Combat('Reptincel', 'Feu', ['Flammèche', 'Griffe', 'Lance-flammes', 'Poing de feu'],
                    {'ATTACK': 6, 'DEFENSE': 5})
Dracaufeu = Combat('Dracaufeu', 'Feu', ['Lance-flammes', 'Vol', 'Rafale Feu', 'Poing de feu'],
                   {'ATTACK': 12, 'DEFENSE': 8})

Carapuce = Combat('Carapuce', 'Eau', ['Bulles d\'O', 'Charge', 'Coup d\'Boule', 'Surf'], {'ATTACK': 3, 'DEFENSE': 3})
Carabaffe = Combat('Carabaffe', 'Eau', ['Bulles d\'O', 'Pistolet à O', 'Coup d\'Boule', 'Surf'], {'ATTACK': 5, 'DEFENSE': 5})
Tortank = Combat('Tortank', 'Eau', ['Pistolet à O', 'Bulles d\'O', 'Hydro Cannon', 'Surf'],
                   {'ATTACK': 10, 'DEFENSE': 10})

Bulbizarre = Combat('Bulbizarre', 'Plante', ['Fouet Lianes', 'Tranch\'Herbe', 'Charge', 'Vampigraine'],
                   {'ATTACK': 2, 'DEFENSE': 4})
Herbizarre = Combat('Herbizarre', 'Plante', ['Fouet Lianes', 'Tranch\'Herbe', 'Balle Graine', 'Vampigraine'],
                 {'ATTACK': 4, 'DEFENSE': 6})
Florizarre = Combat('Florizarre', 'Plante', ['Fouet Lianes', 'Tranch\'Herbe', 'Séisme', 'Végé-Attak'],
                  {'ATTACK': 8, 'DEFENSE': 12})

#     listPokemons.insert(pkmns.name) #TypeError: 'type' object is not iterable. Ne fonctionne pas.

listPokemons = [Salameche,Reptincel,Dracaufeu,Carapuce,Carabaffe,Tortank,Bulbizarre,Herbizarre,Florizarre]

def getRandomPkmn():
    return listPokemons[randint(0, 8)]

def getAllPokedex():
    # Retourne tout le pokedex
    print("Liste pokémons")

def getPokedexById():
    # Retourne un pokémon
    print("Pokémon id : X")