#!/usr/bin/env python3
"""
Fonction Main du script
"""

import os
import sys


ROUGE = "\u001b[31m"


def main():
    """
    S'agit de la finction principal
    :return: retourne un texte dans la console
    """
    compteur = int(os.getenv('START', "1"))
    if len(sys.argv) > 5 or isinstance(sys.argv, int):
        if isinstance(sys.argv, int):
            print("[LP] " + ROUGE + "Le nombre n'est pas valide : " + str(sys.argv[1]))
        else:
            print("[LP] " + ROUGE + "Trop d'argument : " + str(len(sys.argv)))

    else:
        if sys.argv != "":
            compteur = int(sys.argv[1])

        for line in sys.stdin:
            sys.stdout.write("[LP]    " + str(compteur) + ": " + line + "\n")
            compteur += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
