
# Projet de fouille de textes
# > Tri des recettes en régimes allimentaires 
## Kehina et Alix les best 



# Régimes annalysables ? 

### Notion de sains et de régimes  
Sains = équilibre 
dc on a choisit les régimes restrictifs 
genre question de vie ou de mort 
Régimes = très perso = pas binaire bon pour un pas pour un autre 
Ne pouvant pas avoir une catégorie binaire, oui/non ou sains/mauvais, nous avons décidé d'entrainer la machine sur plusieurs régimes allimentaire. Nous testerons ainsi sa capacité à repérer différents régimes.
  
 
### Généralistes 
- Vegan 
- Végétarien 
- Pescétarien 

### Allergies
- Lait / lactose 
- Oeufs 
- Gluten 
- Noix 
- Crustacés
- Sans patates (alixproof)

### Trucs rigolos 
- Crudivore 
- Pour les nuls / débutants en cuisine
- sans alcool / coq au vin  

### Medicaux 
- liquides 
- diabete
- choléstérole 
- régimes anti-inflamatoire 
Un peu chaud et technique 
ex: lissage de la glycémie sur plusieurs heures 

# Régimes choisis 
- Vegan  
- Végétarien 
- Crudivore 
- Sans gluten 
- Sans noix ? 
- Alix proof ? (sans lait(frommage, beurre...), sans oeuf, sans patate (fécules de pomme de terre), sans fruits de mer, sans poissons...)


# Création du corpus 
- script aspirations des urls  

Sites utilisés: 
- J le sang 
- Mercotte ce génie 
...

# Annotation du corpus 
Dans un fichier tabulaire (TSV), 
Les recettes sont annotées par un 1 ou un 0 selon si elles sont compatibles avec les différents régimes choisis plus haut. 



# Critères des diffèrents Régimes choisis 
## Végétarien 
Le régime végétarien, consiste à ne pas consommer de viande animal.   
## Vegan
Plus restricit que le régime végétarien, le règime végan exclut tous les produits d'origine animal ce qui inclut en plus de la viande, les oeufs, le lait. La consomation de produits commme le miel, la cire d'abeille ou le cuir sont souvent aussi exclut. 
## Crudivore 
Le régime crudivore consiste à ne manger uniquement des produits crus. 
## Sans gluten 
Le régime sans gluten consiste à retirer tous les aliments contennant du gluten : blé, seigle, orge, épautre (farine, bulgur, semoule, seitan, sauce soja, extrait de levure, vinaigre de malt, bière, friture (Panco), ... ) 
## Alix Proof 
Le régime "ne pas faire gonfler Alix" consiste à ne pas manger de produits provocant des réactions inopinées sur le système inflamatoire/qui ne font pas réagir les mastocytes d'Alix. 
Ce régime exclut: les produits laitiers, les oeufs, les pommes de terres, les fruits de mer, le poisson, 




# Options supplémentaires 
- Création de menus journaliers pour répondre à la question du sain et de l'équilibre allimentaire avec les besoins journaliers d'une personne 
- Voir un régime sur une journée ou une semaine permettrait aussi de prendre en compte des pathologies ayant des besoins spécifique: lisser la glycémie pour les personnes atteintes de diabète. Sur une semaine, le potentiel inflamatoire des alliments pourait aussi être annalyse pour des pathologies nécessitants un régime anti-inflamatoire. 

