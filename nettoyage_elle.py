import sys
import re
from pathlib import Path



def nettoyage(fichier):

   with open(fichier, 'r', encoding='utf8') as file:
      texte_full = file.read()
      texte = re.search("Nombre de personnes(.*)noter cette recette ?", texte_full, re.DOTALL) # essayer d'avoir le nom de la recette ? 
      print(texte.group(0))


nettoyage(fichier=sys.argv[1])