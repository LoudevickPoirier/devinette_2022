#!/usr/bin/env python3
"""
Fonction Main du script
"""

import random
import re

# COLORATION
ROUGE = "\u001b[31m"
ORANGE = "\u001B[33m"
BLANC = "\u001b[37m"
CYAN = "\u001b[36m"
GREEN = "\u001b[32m"
BLUE = "\u001b[34m"


def main():
    """
    Fonction principale
    """
    reponse = ""

    while reponse is not "nombreRandom":
        compteur = 1
        print(ROUGE + 'LP' + BLANC + ':' + CYAN + ' Jeu de devinette...')
        print(ROUGE + 'LP' + BLANC + ':' + CYAN + ' Devinez le nombre entier entre 1 et 100 \n')
        nombrerandom = nbrandom()
        listereponse = []
        reponse = ""
        succes = False
        rejouer = False

        while compteur < 11 or succes is not True or rejouer is True:
            reponse = input(BLANC + 'Essai ' + GREEN + str(compteur) + BLANC + ': ')
            if reponse is "GGG":
                succes = True
                listereponse.append(reponse)
                break
            if reponse is "PPP":
                listereponse.append(reponse)
                break

            # noinspection PyPep8
            if re.match("^\s*\S*[0-9 -]+$", reponse):
                reponse = int(reponse)
                if reponse is not nombrerandom:
                    if reponse in listereponse:
                        print(
                            ROUGE + 'LP' + BLANC + '>>>' + CYAN + ' Ce nombre a déjà été essayé:' + GREEN + str(
                                listereponse) + '\n')
                    else:
                        compteur += 1
                        listereponse.append(reponse)
                        if reponse > nombrerandom:
                            print(
                                ROUGE + 'LP' + BLANC + '>'
                                + ' Votre nombres est trop ' + GREEN + 'grand' + BLANC + '...\n')
                        if reponse < nombrerandom:
                            print(
                                ROUGE + 'LP' + BLANC + '>'
                                + ' Votre nombres est trop ' + GREEN + 'petit' + BLANC + '...\n')
                else:
                    listereponse.append(reponse)
                    succes = True
                    break
            else:
                print(
                    ROUGE + 'LP' + BLANC + ' >>>' + ROUGE + ' ERREUR: Entrez un nombre entier svp!\n')

        if succes:
            print(ROUGE + 'LP' + BLANC + ' >' + GREEN + ' Bravo, vous avez deviné le nombre! ')
            print(ROUGE + 'LP' + BLANC + ' >' + BLANC + ' Vos essai:  ' + BLUE + str(listereponse) + '\n')
        else:
            print(
                ROUGE + 'LP' + BLANC + ' >'
                + ROUGE + ' Désolé, vous avez échoué après ' + BLUE + '10' + BLANC + ' tentatives.')
            print(ROUGE + 'LP' + BLANC + ' >' + BLANC + ' Vos essai:  ' + BLUE + str(listereponse))
            print(
                ROUGE + 'LP' + BLANC + '> Le nombre était: ' + BLUE + str(nombrerandom) + '\n')
        while reponse != "oui" or reponse != "o" or reponse != "non" or reponse != "n":
            reponse = input(ROUGE + 'LP' + ORANGE + ' Voulez-vous rejouer? [O/N] ')
            reponse = reponse.lower()
            if reponse == "oui" or reponse == "o" or reponse == "non" or reponse == "n":
                if reponse == "oui" or reponse == "o":
                    break
                if reponse == "non" or reponse == "n":
                    print(ROUGE + 'LP' + ORANGE + ' Au Revoir !')
                    break
            else:
                print(ROUGE + 'LP' + BLANC + ' >' + ROUGE + ' Choix invalide ! ')
        if reponse == "non" or reponse == "n":
            break


def nbrandom():
    """
    Fonction qui retourne un nombre random entre 1 et 100
    :return: un nombre random
    """
    return random.randrange(1, 101)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
