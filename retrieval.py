import pandas as pd
import requests
from bs4 import BeautifulSoup
import argparse

##### CE PROGRAMME PERMET D'EXTRAIRE LE CONTENU TEXTUEL BRUT DE CHAQUE LIEN DU CORPUS #####
# Les fichiers crées sont stockés dans dumps-text/<nom_du_site>
# Exemple commande = python3 retrieval.py nadine

##### PREMIÈRE FONCTION POUR OBTENIR LES COLONNES DES LIENS ET DES ID ####
def get_table():

    tableau = pd.read_csv("liens.csv")
    colonne_liens_id = tableau[["id", "liens"]]
    return colonne_liens_id
    # Return les colonnes entièrement 

##### FONCTION POUR RÉCUPÉRER LES LIENS DES RECETTES #####
def get_liens(colonne_liens_id, debut, fin):

    # On commence par obtenir les lignes concernant chaque site
    lignes_necessaires = colonne_liens_id[debut:fin]
    lignes_necessaires["id"] = lignes_necessaires["id"].astype(int) # On convertit les id en int ! 
    liste_liens = list(lignes_necessaires.itertuples(index=False, name=None)) # On crée une liste de tuples (id, lien)

    return liste_liens

##### FONCTION POUR RÉCUPÉRER LE CONTENU TEXTUEL DE CHAQUE LIEN À L'AIDE DE BEAUTIFUL SOUP #####
def get_texte(liste_liens, site):

    for id, lien in liste_liens:
        url = lien
        reponse = requests.get(url)
        soupe = BeautifulSoup(reponse.text, "html.parser")
        texte = soupe.get_text()
        chemin = f"dumps-text/{site}/{id}_{site}_dump.txt"
        with open(chemin, "w", encoding="utf8") as fichier:
            fichier.write(texte)

def main():

    parser = argparse.ArgumentParser(description='Extraire le contenu textuel')
    parser.add_argument('site', choices=["nadine", "jackie", "mercotte", "marmiton", "elle"], help='Nom du site dont on veut extraire les liens')
    args = parser.parse_args()

    colonne_liens_id = get_table()

    # On extrait les liens correspondants à chaque site
    if args.site == "nadine":
        liste_liens = get_liens(colonne_liens_id, debut = 0, fin = 50)
    elif args.site == "jackie":
        liste_liens = get_liens(colonne_liens_id, debut = 51, fin = 101)
    elif args.site == "mercotte":
        liste_liens = get_liens(colonne_liens_id, debut = 102, fin = 152)
    elif args.site == "marmiton":
        liste_liens = get_liens(colonne_liens_id, debut = 153, fin = 303)
    elif args.site == "elle":
        liste_liens = get_liens(colonne_liens_id, debut = 304, fin = 454)

    get_texte(liste_liens, args.site)

if __name__ == "__main__":
    main()


