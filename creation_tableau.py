import pandas as pd
from pathlib import Path
import re

##### PREMIÈRE FONCTION POUR OBTENIR LE TABLEAU ORIGINEL ####
def get_table():

    tableau = pd.read_csv("liens.csv")
    colonnes = tableau[["id", "liens", "vegetarien", "vegan", "crudivore", "sans_gluten", "crudivore", "sans_gluten", "alixproof", "sans_noix", "sucré/salé"]]
    colonnes = tableau[tableau["id"] > 0] # On enlève les lignes avec les totaux 
    colonnes["id"] = colonnes["id"].astype(int) # On convertit tout en entier
    colonnes["vegetarien"] = colonnes["vegetarien"].astype(int)
    colonnes["vegan"] = colonnes["vegan"].astype(int)
    colonnes["crudivore"] = colonnes["crudivore"].astype(int)
    colonnes["sans_gluten"] = colonnes["sans_gluten"].astype(int)
    colonnes["alixproof"] = colonnes["alixproof"].astype(int)
    colonnes["sans_noix"] = colonnes["sans_noix"].astype(int)

    return colonnes
    # Return les colonnes entièrement 

get_table()

#### ON CRÉE UNE LISTE AVEC TOUS NOS TEXTES ####
def get_textes(dossier):
    
    liste_textes = []
    listes_fichiers = sorted(dossier.glob("*/*.txt"), key=lambda fichier: int(re.match(r'(\d+)', fichier.name).group(0)))
    # Il a fallu récupérer tous nos dossiers par ordre numérique
    # On aurait aussi pu passer pas la direction nadine, puis jackie, puis mercotte... Mais pas integrée dans glob
    for fichier in listes_fichiers:
        with open(fichier, "r", encoding="utf8") as f:
            texte = f.read()
            liste_textes.append(texte)
   
    return liste_textes



def lemmatisation(liste_textes):

    import spacy 
    nlp = spacy.load("fr_core_news_md")

    liste_textes_lemma = []
    for texte in liste_textes:
        doc = nlp(texte)
        liste_texte_lemma = []
        for mot in doc:
            lemme = mot.lemma_
            liste_texte_lemma.append(lemme)
        texte_lemma = " ".join(liste_texte_lemma)
        liste_textes_lemma.append(texte_lemma)

    return liste_textes_lemma


##### ON INSERT LES TEXTES DANS LE TABLEAU "LIENS" ET ON EN CRÉER UN NOUVEAU #####
def insertion_textes(liste_textes, colonnes, liste_textes_lemma):

    liens = colonnes.columns.get_loc("liens")

    avant = colonnes.iloc[:, : liens+1]
    après = colonnes.iloc[:, liens+1 :]
    avant["textes"] = liste_textes
    avant["textes_lemma"] = liste_textes_lemma


    tableau = pd.concat([avant, après], axis=1)
    print(tableau)
    tableau.to_csv("recettes.csv", index=False, encoding='utf-8-sig')


def main():

    colonnes = get_table()
    liste_textes = get_textes(dossier = Path("dumps-traites"))
    liste_textes_lemma = lemmatisation(liste_textes)
    insertion_textes(liste_textes, colonnes, liste_textes_lemma)
   

if __name__ == "__main__":
    main()