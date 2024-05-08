import pandas as pd
import matplotlib.pyplot as plt
import datastructures
import math


def get_table():

    tableau = pd.read_csv("recettes.csv")
    colonnes = tableau[["id", "liens", "textes", "textes_lemma", "vegetarien", "vegan", "crudivore", "sans_gluten", "alixproof", "sans_noix", "sucré/salé"]]
    return colonnes


##### #####
def get_recettes(colonnes):

     
    lignes_necessaires = colonnes[0:501]
    list_recettes = []
    for index, ligne in lignes_necessaires.iterrows():
        id = ligne["id"]
        lien = ligne["liens"]
        texte = ligne["textes"]
        texte_lemma = ligne["textes_lemma"]
        vegetarien = ligne["vegetarien"]
        vegan = ligne["vegan"]
        crudivore = ligne["crudivore"]
        sans_gluten = ligne["sans_gluten"]
        alixproof = ligne["alixproof"]
        sans_noix = ligne["sans_noix"]
        sucre_sale = ligne["sucré/salé"]
        recette = datastructures.Recette(id = id, url = lien, texte = texte, texte_lemma = texte_lemma, vegetarien = vegetarien, vegan= vegan, crudivore = crudivore, sans_gluten = sans_gluten, alixproof= alixproof, sans_noix = sans_noix, ss = sucre_sale) 
        list_recettes.append(recette)
   
    return list_recettes

def get_numbers(list_recettes):

    ## Initialisation variables
    nbr_recette = 0
    nbr_vegetarien = 0
    nbr_vegan = 0
    nbr_crudivore = 0
    nbr_sans_gluten = 0
    nbr_alixproof = 0
    nbr_sans_noix = 0
    nbr_sale = 0
    nbr_sucre = 0

    for recette in list_recettes:     
        nbr_recette += 1
        if recette.vegetarien == 1:
            nbr_vegetarien += 1
        if recette.vegan ==1: 
            nbr_vegan += 1   
        if recette.crudivore == 1:
            nbr_crudivore += 1
        if recette.sans_gluten == 1:
            nbr_sans_gluten += 1
        if recette.alixproof == 1:
            nbr_alixproof += 1
        if recette.sans_noix == 1:
            nbr_sans_noix += 1 
        if recette.ss == "sucré": 
            nbr_sucre += 1
        else: 
            nbr_sale += 1
    
    pourcentage_vegetarien = round(((nbr_vegetarien/nbr_recette)*100), 2)
    pourcentage_vegan = round(((nbr_vegan/nbr_recette)*100), 2)
    pourcentage_crudivore = round(((nbr_crudivore/nbr_recette)*100), 2)
    pourcentage_sans_gluten = round(((nbr_sans_gluten/nbr_recette)*100),2)
    pourcentage_alixproof = round(((nbr_alixproof/nbr_recette)*100),2)
    pourcentage_sans_noix = round(((nbr_sans_noix/nbr_recette)*100),2)
    pourcentage_sucre = round(((nbr_sucre/nbr_recette)*100), 2)
    pourcentage_sale = round(((nbr_sale/nbr_recette)*100), 2)


    return nbr_recette, nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix, nbr_sale, nbr_sucre, pourcentage_vegetarien, pourcentage_vegan, pourcentage_crudivore, pourcentage_sans_gluten, pourcentage_alixproof, pourcentage_sans_noix, pourcentage_sale, pourcentage_sucre


def plot_regimes(nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix, nbr_sale, nbr_sucre):
    bar_width = 0.25
    indices = range(len([nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix]))

    plt.figure(figsize=(12, 6))
    plt.bar(indices, [nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix], color=['green', 'darkseagreen', 'lightcoral', 'gold', 'skyblue', 'pink'], width=bar_width, edgecolor='grey')
    plt.xlabel('Regime alimentaire', fontweight='bold', fontsize=15)

    plt.ylabel('Nombre de recettes', fontweight='bold', fontsize=15)
    plt.ylim(0,500)
    plt.title('Nombre de recettes en fonction du régime alimentaire')
    plt.xticks(indices, ['Végétarien', 'Vegan', 'Crudivore', 'Sans gluten', 'Alixproof', 'Sans noix'], rotation=30)
    plt.show()


colonnes = get_table()
list_recettes = get_recettes(colonnes)
nbr_recette, nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix, nbr_sale, nbr_sucre, pourcentage_vegetarien, pourcentage_vegan, pourcentage_crudivore, pourcentage_sans_gluten, pourcentage_alixproof, pourcentage_sans_noix, pourcentage_sale, pourcentage_sucre = get_numbers(list_recettes)
print(nbr_recette, nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix, nbr_sale, nbr_sucre)
print(pourcentage_vegetarien, pourcentage_vegan, pourcentage_crudivore, pourcentage_sans_gluten, pourcentage_alixproof, pourcentage_sans_noix, pourcentage_sale, pourcentage_sucre)
plot_regimes(nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix, nbr_sale, nbr_sucre)


def plot_ss(nbr_sale, nbr_sucre): 
    nom = ["salé", "sucré"]
    taille = [nbr_sale, nbr_sucre]

    plt.figure(figsize=(14, 12))  
    plt.pie(taille, labels=nom, colors=["pink", "yellowgreen"])
    plt.title(f"Répartition des recettes en salé ou sucré")
    plt.axis('equal')
    plt.show()
    plt.close()

plot_ss(nbr_sale, nbr_sucre)

def plot_pourcentage_regimes(pourcentage_vegetarien, pourcentage_vegan, pourcentage_crudivore, pourcentage_sans_gluten, pourcentage_alixproof, pourcentage_sans_noix):
    bar_width = 0.25
    indices = range(len([nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix]))

    plt.figure(figsize=(12, 6))
    plt.bar(indices, [nbr_vegetarien, nbr_vegan, nbr_crudivore, nbr_sans_gluten, nbr_alixproof, nbr_sans_noix], color=['lemonchiffon', 'g', 'r', 'm', 'b', 'c'], width=bar_width, edgecolor='grey')
    plt.xlabel('Regime alimentaire', fontweight='bold', fontsize=15)
    plt.ylabel('Nombre de recettes', fontweight='bold', fontsize=15)
    plt.title('Nombre de recettes en fonction du régime alimentaire')

    plt.xticks(indices, ['Végétarien', 'Vegan', 'Crudivore', 'Sans gluten', 'Alixproof', 'Sans noix'], rotation=30)
    plt.show()

    plt.show()
