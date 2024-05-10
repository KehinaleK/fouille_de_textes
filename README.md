# fouille_de_textes
Dépôt pour le projet de l'UE fouille de textes

# Scripts de récupération des données et des statistiques
## retrieval.py
Commandes à utiliser : 
python3 retrieval.py {site de cuisine}
ex: python3 retrieval.py nadine

Pour lancer ce script, il faut avoir dans le même dossier un fichier liens.csv. 
Les fichiers crées sont stockés dans dumps-text/<nom_du_site>. 

## nettoyage.py
Commandes à utiliser: 
python3 nettoyage.py {site de cuisine}
ex: python3 nettoyage.py marmiton

Pour lancer ce script il faut les dossiers dumps créés à l'aide de retrieval.py. 
Les fichiers propres sont stockés dans dumps-traites/<nom_du_site>. 

## creation_tableau.py
Commandes à utiliser: 
python3 creation_tableau.py dumps-traites/. 

Pour cela il faut avoir lancé le script nettoyage.py.

## datastructures.py
Fichier qui contient la datastructures de nos recette.

## statistiques.py
Commandes à utiliser: 
python3 datastructures.py 

Lis le fichier recettes.csv créé avec le script creation_tableau.py et fait des statistiques. 

# Scripts d'apprentissage
Il y a 4 scripts d'apprentissage un pour chaque modèle. 

## nbm.py
Script d'apprentissage avec Naïve bayes.
Commandes à utiliser:  
python3 nbm.py {régime}
ex: python3 nbm.py vegan

## svm.py
Script d'apprentissage avec les SVM.
Commandes à utiliser:  
python3 svm.py {régime}
ex: python3 svm.py vegan

## knn.py
Script d'apprentissage avec k nearest neighbours.
Commandes à utiliser:  
python3 knn.py {régime}
ex: python3 knn.py vegan

## dtc.py 
Script d'apprentissage avec Decision Trree Classifier.
Commandes à utiliser:  
python3 dtc.py {régime}
ex: python3 dtc.py vegan

![Mercotte](Mercote-removebg-preview.png)