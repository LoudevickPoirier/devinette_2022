#!/usr/bin/env python3
import random
#COLORATION
ROUGE = "\u001b[31m"
BLANC = "\u001b[37m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
BLUE = "\u001b[34m"

def main():
    """
    Fonction principale
    """
    nombreRandom = 0;
    compteur = 0;
    reponse = "";
    while reponse != nombreRandom:
        print(ROUGE + "LP" + BLANC + ":" + CYAN + " Jeu de devinette...")
        print(ROUGE + "LP" + BLANC + ":" + CYAN + " Devinez le nombre entier entre 1 et 100")
        nombreRandom = nbRandom()
        compteur += 1;
        print(nombreRandom)
        reponse = input(BLANC + "Essai "+ GREEN + str(compteur) + BLANC + ": ")
        reponse = int(reponse)
        print(reponse)
        if (reponse < nombreRandom):
            print(ROUGE + "LP" + BLANC + ">" + " Votre nombres est trop " + GREEN + "petit" + BLANC + "...")
        else:
            if(reponse > nombreRandom):
                print(ROUGE + "LP" + BLANC + ">" + " Votre nombres est trop " + GREEN + "grand" + BLANC + "...")
            else:
                print(ROUGE + "LP" + BLANC + ">" + BLUE + " Bravo, vous avez deviné le nombre!")

def nbRandom():
    return random.randrange(1,101)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
