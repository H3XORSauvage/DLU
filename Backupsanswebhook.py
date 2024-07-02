import os
import colorama
from colorama import Fore, Style

colorama.init()

def demarrage():
    print("Bienvenue! Lancement du script en cours...")
    print("By Saucisson :D")

if __name__ == "__main__":
    demarrage()

def recherche_DB(nom_fichier, mot_cle):
    resultats = []
    with open(nom_fichier, 'r', encoding='utf-8') as fichier:
        for index, ligne in enumerate(fichier, start=1):
            if mot_cle in ligne:
                resultats.append((nom_fichier, index, ligne.strip()))
    return resultats

def parcourir_sous_dossiers_recherche_DB(dossier_parent, mot_cle):
    resultats = []
    for dossier_racine, _, fichiers in os.walk(dossier_parent):
        for nom_fichier in fichiers:
            if nom_fichier.endswith('.txt'):
                chemin_fichier = os.path.join(dossier_racine, nom_fichier)
                resultats.extend(recherche_DB(chemin_fichier, mot_cle))
    return resultats

if __name__ == "__main__":
    # Dossier principal des DB
    dossier_parent = r'DATABASE'

    mot_cle = input("Entrez le mot à rechercher: ")

    # Recherche dans les DB
    resultats = parcourir_sous_dossiers_recherche_DB(dossier_parent, mot_cle)

    print("Résultats de la recherche :\n")
    if resultats:
        for nom_fichier, ligne_numero, ligne in resultats:
            print(f"{Fore.GREEN}[NEW]{Style.RESET_ALL} {nom_fichier}, ligne {ligne_numero}: {ligne.strip()}")
            print(f"    {ligne}\n")
    else:
        print(f"{Fore.RED}Aucune DB trouvée pour ' {Fore.BLUE}{mot_cle} {Style.RESET_ALL} {Fore.RED}'.{Style.RESET_ALL}")

    input("Entrée pour quitter..")
