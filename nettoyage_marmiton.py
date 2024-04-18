import sys
import re
from pathlib import Path


# Beautiful soup idéalement 
# A cause des images 

def nettoyage(fichier):

   with open(fichier, 'r', encoding='utf8') as file:
      texte_full = file.read()
      texte = re.search("Ingrédients(.*)Je m'inscris", texte_full, re.DOTALL)
      print(texte.group(0))


nettoyage(fichier=sys.argv[1])