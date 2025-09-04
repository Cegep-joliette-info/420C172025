# Chapitre 2 - Atelier 3 - Match

## Section 1

Pour tous les numéros de cette section, résoudre les problèmes sans if (utilisez un match). Ce sont des numéros qui proviennent des exercices précédents.

### Numéro 1

Écrire un algorithme qui selon le sexe (H,h,F,f,A,a), le prénom et le nom, affiche un message approprié. 

Exemple:
```
Entrez votre prénom: Bob
Entrez votre nom: Gratton
Choisir votre sexe (H, h, F, f, A, a): H
Bonjour monsieur Bob Gratton
```

### Numéro 2

Résoudre ce problème sans if (utilisez un match):

Écrire un algorithme qui selon un nombre (1-7) donne le jour correspondant. Tout nombre invalide affiche "-".

Exemples: 
```
Entrez un chiffre entre 1 et 7: 1
dimanche

Entrez un chiffre entre 1 et 7: 5
jeudi

Entrez un chiffre entre 1 et 7: 42
-
```

## Section 2

Résoudre ces problèmes avec un if, sans match, puis faites l'inverse.
Demandez-vous ensuite, quelle est la solution la plus simple?

### Numéro 3

Demandez un mois à l'utilisateur (1 pour janvier, 2 pour février, 3 pour mars, etc.). Affichez la saison correspondante au mois sélectionné, ou affichez "Invalide" si le chiffre choisi n'est pas valide.

Exemples:
```
Entrez un nombre entre 1 et 12 représentant un mois (1 = janvier): 5
Printemps

Entrez un nombre entre 1 et 12 représentant un mois (1 = janvier): 12
Hiver

Entrez un nombre entre 1 et 12 représentant un mois (1 = janvier): 42
Invalide
```

### Numéro 4

Demandez un jour et un mois à l'utilisateur (1 pour janvier, 2 pour février, 3 pour mars, etc.). Indiquez si la date entrée est valide, considérez que l'année n'est pas bissextile.

### Numéro 5 - Défi

Dans une chaîne de restaurant les choix suivants sont offerts:

 * Entrées: Salade (8$), Soupe (6$)
 * Plats principaux: Poulet (20$), Steak (34$), Tofu (49$)
 * Desserts: Pointe de tarte (9$), Crème glacé (4$)

Demandez à l'utilisateur s'il veut une entrée, si oui offrez lui les choix disponible. Répéter pour chaque catégorie. Affichez le total de la facture ainsi que le pourboire suggéré de 42%.

Vous pouvez changer les catégories, les repas et les prix selon votre gout.

Exemple:
```
Voulez-vous une entrée (O/N)? O
Voulez-vous:
1 - Une salade (8$)
2 - Une soupe (6$)
Votre choix: 2
Voulez-vous un plat principal (O/N)? O
Voulez-vous:
1 - Le poulet (20$)
2 - Le steak (34$)
3 - Le tofu (49$)
Votre choix: 2
Voulez-vous un dessert (O/N)? O
Voulez-vous:
1 - Une pointe de tarte (9$)
2 - Une crème glacé (4$)
Votre choix: 1
Total de 49.00$, pourboire suggéré: 20.58$

Voulez-vous une entrée (O/N)? N
Voulez-vous un plat principal (O/N)? O
Voulez-vous:
1 - Le poulet (20$)
2 - Le steak (34$)
3 - Le tofu (49$)
Votre choix: 4
Choix invalide
Voulez-vous un dessert (O/N)? bla
Total de 0.00$, pourboire suggéré: 0.00$
```