from dataclasses import dataclass


@dataclass
class Recette: 
    id: int
    url: str
    texte: str
    texte_lemma: str
    vegetarien: bool
    vegan: bool
    crudivore: bool
    sans_gluten: bool
    alixproof: bool
    sans_noix: bool
    ss: str
