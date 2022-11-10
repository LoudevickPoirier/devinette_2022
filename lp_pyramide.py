#!/usr/bin/env python3
import argparse
import sys


def rectangle(hauteur: int, motif: str) -> str:
    rect=""
    compteur=0
    args = arguments()

    for _ in range(0, hauteur):
        compteur+=1
        if args.LP:
            rect += "[LP]   "
        rect += compteur * motif + "\n"
    return rect

def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Ce programme permet de tracer une pyramide.")
    parser.add_argument("hauteur", type=int, help="Hauteur de la pyramide en nombre de ligne")

    parser.add_argument("-m", "--motif", default="#",
                        help="Motif de caractères utilisé pour dessiner la pyramide (défaut=#)")
    parser.add_argument("-I", "--LP", action='store_true',
                        help="Permet d'afficher les initiales.")
    return parser.parse_args()

def main() -> None:
    args = arguments()
    rect = rectangle(args.hauteur, args.motif)
    print(rect, end='')

if __name__ == '__main__':
    main()  # LP: Démarrer le script
