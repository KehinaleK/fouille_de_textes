from pathlib import Path
import re
import argparse

##### CE PROGRAMME PERMET DE NETTOYER LES DUMPS TEXTS ET DE LES TRAITER AFIN DE CRÉER DES FICHIERS TXT PROPRES #####
# Les fichiers propres sont stockés dans dumps-traites/<nom_du_site> 
# Nous privilégions parfois les expressions régulières à Beautiful Soup car les sites comprennent trop de variations plus faciles à attraper avec les re.
# python3 nettoyage.py marmiton

#### ON COMMENCE PAR RÉCUPÉRER L'ENSEMBLE DES DOSSIERS DUMPS NON TRAITES PAR SITE #####
def parcourir_dossier(site):

    dossier = Path("dumps-text")
    liste_fichiers = dossier.glob(f"{site}/*.txt")
    return liste_fichiers

#### FONCTION POUR ÉVITER RÉPÉTITION AVEC LES EXCEPTIONS #####
def texte_exception(fichier, texte):

    chemin = f"dumps-traites/{fichier.parent.name}/{fichier.name}"
    print(chemin)
    print(texte)
    with open(chemin, "w", encoding="utf8") as file_traite:
        texte_trop_beau = re.sub(r"\s+", " ", texte.group(0).strip())
        file_traite.write(texte_trop_beau)

#### FONCTION DE NETTOYAGE NADINE #####
def nettoyage_nadine(liste_fichiers):

    for fichier in liste_fichiers:
        with open(fichier, "r", encoding="utf8") as file:
            texte_full = file.read()
            try:
                texte = re.search("Let.s go en cuisine(.*?)(?=Si vous testez cette recette)", texte_full, re.DOTALL)
                texte_exception(fichier, texte)
            except:
                if fichier == Path("dumps-text/nadine/18_nadine_dump.txt"):
                    texte = re.search("Let.s go en cuisine(.*?)(?=PartagezEnregistrer22)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                elif fichier == Path("dumps-text/nadine/69_nadine_dump.txt"):
                    texte = re.search("Let.s go en cuisine(.*?)(?=PartagezEnregistrer33)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                elif fichier == Path("dumps-text/nadine/32_nadine_dump.txt"):
                    texte = re.search("Let.s go en cuisine(.*?)(?=D’après une recette de Yolande.)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                elif fichier == Path("dumps-text/nadine/70_nadine_dump.txt"):
                    texte = re.search("Les orages passés(.*?)(?=PartagezEnregistrer0.)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                else:
                    texte = re.search("Épingler la recette(.*?)(?=Si vous testez cette recette)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                

    # On a eu besoin de s'occuper de trois exceptions

#### FONCTION DE NETTOYAGE JACKIE #####
def nettoyage_jackie(liste_fichiers):

    for fichier in liste_fichiers:
        with open(fichier, "r", encoding="utf8") as file:
            texte_full = file.read()
            texte = re.search("Ingrédients(.*?)(?=Les participants|La petite (H|h)istoire|(A|a)vec cette recette|Impression)", texte_full, re.DOTALL)
            texte_exception(fichier, texte)
            # Toujours le même début mais pas la même fin, everybody loves Jackie ! 

#### FONCTION DE NETTOYAGE MERCOTTE #####
def nettoyage_mercotte(liste_fichiers):

    for fichier in liste_fichiers:
        with open(fichier, "r", encoding="utf8") as file:
            texte_full = file.read()
            try:
                if fichier == Path("dumps-text/mercotte/146_mercotte_dump.txt"):
                    texte = re.search("La recette(.*?)(?=Imprimer la (R|r)ecette)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                elif fichier == Path("dumps-text/mercotte/195_mercotte_dump.txt"):
                    texte = re.search("Pour 6 personnes : préparation 10 min, cuisson 40min(.*?)(?=Imprimer la (R|r)ecette)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                else:
                    texte = re.search("La recette(.*?)(?=Explications? utiles? ou futiles?|Imprimer la (R|r)ecette|Langoustines\? Saint Jacques\?)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
            except:
                if fichier == Path("dumps-text/mercotte/159_mercotte_dump.txt"):
                    texte = re.search("La recette :(.*?)(?=On peut présenter dans des tasses avec possibilité de se servir ou non de noisettes)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                else:
                    texte = re.search("Version rapide :(.*?)(?=Imprimer la Recette)", texte_full, re.DOTALL)
                    texte_exception(fichier, texte)
                
            # On aime BEAUCOUP moins Mercotte ! COLÈRE !

#### FONCTION DE NETTOYAGE MARMITON #####
def nettoyage_marmiton(liste_fichiers):

    for fichier in liste_fichiers:
        with open(fichier, "r", encoding="utf8") as file:
            texte_full = file.read()
            texte = re.search("Ingrédients(.*?)(?=Je m'inscris|Voir toutes les recettes)", texte_full, re.DOTALL)
            texte_exception(fichier, texte)

            # Marmiton toujours là pour nous !

#### FONCTION DE NETTOYAGE ELLE #####
def nettoyage_elle(liste_fichiers):

    for fichier in liste_fichiers:
        with open(fichier, "r", encoding="utf8") as file:
            texte_full = file.read()
            texte = re.search("Ingrédients(.*?)(?=L'astuce|[0-9].?[0-9]?[0-9]? sur)", texte_full, re.DOTALL)
            texte_exception(fichier, texte)
    
            # Vive Elle
        
def main():

    parser = argparse.ArgumentParser(description='Extraire le contenu textuel mais propre !')
    parser.add_argument('site', choices=["nadine", "jackie", "mercotte", "marmiton", "elle"], help='Nom du site dont on veut nettoyer les fichiers')
    args = parser.parse_args()

    liste_fichiers = parcourir_dossier(args.site)
    if args.site == "nadine":
        nettoyage_nadine(liste_fichiers)
    elif args.site == "jackie":
        nettoyage_jackie(liste_fichiers)
    elif args.site == "mercotte":
        nettoyage_mercotte(liste_fichiers)
    elif args.site == "marmiton":
        nettoyage_marmiton(liste_fichiers)
    elif args.site == "elle":
        nettoyage_elle(liste_fichiers)

if __name__ == "__main__":
    main()