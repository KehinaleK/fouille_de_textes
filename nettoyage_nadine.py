import sys
import re
from pathlib import Path



def nettoyage(fichier):

   with open(fichier, 'r', encoding='utf8') as file:
      texte_full = file.read()
      texte = re.search("Let.s go en cuisine(.*)Si vous testez cette recette", texte_full, re.DOTALL)
      print(texte.group(0))


nettoyage(fichier=sys.argv[1])