import os

from joueur import Joueur

# Boucle à répétition sur ce main
while True:
    print("                                                                                       ")
    print("                                                                                       ")
    print("[=================================JEU TEXTUEL POKEMON=================================]")
    print("|                                                                                     |")
    print("|                                                                                     |")
    print("|                                  1) Combat Pokemon.                                 |")
    print("|                                  2) Capture de Pokemon.                             |")
    print("|                                  3) Magasin.                                        |")
    print("|                                                                                     |")
    print("[=====================================================================================]")
    print("                                                                                       ")

    choix = int(input("                                       Que faire ?"))

    if (choix == 1):
        exec(open("combat.py").read())
    elif (choix == 2):
        exec(open("capture.py").read())
    elif (choix == 3):
        exec(open("objectMagasin.py").read())
    # else:
    #     while (choix > 2):
    #         print("Veuillez selectionner un choix valide.")
    #         choix = int(input("                                       Que faire ?\n"))
    #         # Revenir au choix de fonctionnalité # A faire