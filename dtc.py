import csv
import argparse
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns; set()
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
import nltk # Obligée d'importer nltk pour obtenir des stopwords en français, il n'y en a pas chez scikit learn
from nltk.corpus import stopwords
nltk.download('stopwords')

# ex: python3 dtc.py vegan

def entrainement(regime, index):


    french_stop_words = stopwords.words('french')
    french_stop_words.remove("pas")
    

    corpus_dataframe = pd.read_csv('recettes.csv', header=0, usecols=[2, 3, index], names=['textes', 'textes_lemma', regime])
    corpus_dataframe = corpus_dataframe.dropna(subset=['textes'])

    train_corpus, test_corpus=train_test_split(corpus_dataframe, test_size=0.25, random_state=42,stratify=corpus_dataframe[regime])

    train_text = train_corpus['textes'] + ' ' + train_corpus['textes_lemma']
    test_text = test_corpus['textes'] + ' ' + test_corpus['textes_lemma']
    # Créer une pipeline
    model = make_pipeline(TfidfVectorizer(stop_words=french_stop_words), DecisionTreeClassifier())
    model.fit(train_text, train_corpus[regime])
    test_evaluation = model.predict(test_text)
    # On convertie les données textuelles en matrices globalement, chaque mot a un "score".
 
    # Permet d'entraîner le modèle
    # On "fit" les données d'entrainement et les données cibles.
    # On dit que ces données vectorisées sont associées à telle ou telle réponse.

    print("Taux d'accuracy :", accuracy_score(test_corpus[regime], test_evaluation))
    print("Classification Report:")
    print(classification_report(test_corpus[regime], test_evaluation))

    return test_evaluation, test_corpus

 # PERMET D'OBTENIR NOS TABLEAUX CSV 
def obtention_phrases(test_evaluation, test_corpus, regime):

    VP = []
    FP = []
    VN = []
    FN = []

    for phrase, vraie_valeur, prediction in zip(test_corpus["textes"], test_corpus[regime], test_evaluation):

        if vraie_valeur == 1 and prediction == 1:
            VP.append((phrase, vraie_valeur, prediction))
        elif vraie_valeur == 0 and prediction == 1:
            FP.append((phrase, vraie_valeur, prediction))
        elif vraie_valeur == 0 and prediction == 0:
            VN.append((phrase, vraie_valeur, prediction))
        elif vraie_valeur == 1 and prediction == 0:
           FN.append((phrase, vraie_valeur, prediction))

    with open(f"data/{regime}_dtc.csv", "w") as fichier:
        structure = csv.writer(fichier, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        structure.writerow(["regime", "valeur réelle", "valeur prédite"])
        if len(VP) > 0:
            structure.writerow(["VRAIS POSITIFS", " ", " "])
        for phrase in VP:
            structure.writerow([phrase[0], phrase[1], phrase[2]])
        if len(FP) > 0:
            structure.writerow(["FAUX POSITIFS", " ", " "])
        for phrase in FP:
            structure.writerow([phrase[0], phrase[1], phrase[2]])
        if len(VN) > 0:
            structure.writerow(["VRAIS NÉGATIFS", " ", " "])
        for phrase in VN:
            structure.writerow([phrase[0], phrase[1], phrase[2]])
        if len(FN):
            structure.writerow(["FAUX NÉGATIFS", " ", " "])
        for phrase in FN:
            structure.writerow([phrase[0], phrase[1], phrase[2]])
        

# Création d'une matrice de confusion : 
def matrice_de_confusion(test_evaluation, test_corpus, regime):


    matrice = confusion_matrix(test_corpus[regime], test_evaluation)
    sns.heatmap(matrice, square=True, annot=True, fmt='d',cmap='Reds', cbar=True, xticklabels=[f'non-{regime}', regime], yticklabels=[f'non-{regime}', regime])
    plt.xlabel('Vraies valeurs')
    plt.ylabel('Valeurs prédites')
    plt.title('Matrice de confusion')
    plt.show()

def main():
    
    parser = argparse.ArgumentParser(description="Choix du régime alimentaire pour l'entraînement")
    parser.add_argument('regime', choices=['vegetarien', 'vegan', 'crudivore', 'sans_gluten', 'alixproof', 'sans_noix', "sucré/salé"], help= "Choix du régime alimentaire")
    args = parser.parse_args()
        
    if args.regime == "vegetarien":
        regime = "vegetarien"
        index = 4
    elif args.regime =="vegan":
        regime = "vegan"
        index = 5
    elif args.regime == "crudivore":
        regime = "crudivore"
        index = 6
    elif args.regime == "sans_gluten":
        regime = "sans_gluten"
        index = 7
    elif args.regime == "alixproof": 
        regime = "alixproof"
        index = 8
    elif args.regime == "sans_noix":
        regime = "sans_noix"
        index = 9
    elif args.regime == "sucré/salé": 
        index = 10
    test_evaluation, test_corpus = entrainement(regime, index)
    obtention_phrases(test_evaluation, test_corpus, regime)
    matrice_de_confusion(test_evaluation, test_corpus, args.regime)


if __name__ == "__main__":
    main()