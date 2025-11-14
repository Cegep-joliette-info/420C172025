# Chapitre 3 - Atelier 9 - Dictionnaires

## Numéro 1

Créez un dictionnaire pour enregistrer les données d'un utilisateur. Faites les étapes suivantes, une après l'autre dans le code (ce n'est pas logique, mais je veux vous faire pratiquer la manipulation de dictionnaire):

 1. Demandez le nom d'utilisateur et le mot de passe à l'usager, enregistrez les données dans un dictionnaire
 2. Validez le mot de passe (doit avoir au moins 8 caractères et ne pas contenir le nom d'utilisateur), affichez un message d'erreur et redemandez le mot de passe jusqu'à ce qu'il soit valide
 3. Demandez une confirmation de mot de passe s'il n'y en a pas dans le dictionnaire et sauvegardez la dans le dictionnaire. Supprimez la confirmation de mot de passe si elle n'est pas identique au mot de passe.

Exemple à la console:

```
Entrez votre nom d'utilisateur: asdf
Entrez votre mot de passe: 12asdf34
Le nom d'utilisateur ne peut pas être dans le mot de passe
Entrez votre mot de passe: 1234
Le mot de passe doit avoir au moins 8 caractères
Entrez votre mot de passe: qwerqwer
Répétez le mot de passe: qwer
Ce n'est pas le bon mot de passe
Répétez le mot de passe: qwerqwer
{'nomUtilisateur': 'asdf', 'motDePasse': 'qwerqwer', 'confirmation': 'qwerqwer'}
```

## Numéro 2

Reprise du chapitre 3 - atelier 3 - numéro 5.

Demandez une chaîne de caractère à l'utilisateur. Avec un dictionnaire, faites le décompte de chaque caractères saisis (il y a 5 'a', 8 'b', etc.).

Défi: Comptez le nombre de chaque lettre (a-z), caractères spéciaux (tous ensemble) et caractères d'espacements (tous ensembles).
Pour les lettres, les minuscules, majuscules et accents compte pour la même lettre (A, a et à compte pour la lettre a).

Exemples:

```
Entrez du texte: Il était trop Tôt pour aller sur l'île
{'i': 3, 'l': 5, 'espace': 7, 'e': 3, 't': 5, 'a': 2, 'r': 4, 'o': 3, 'p': 2, 'u': 2, 's': 1, 'spécial': 1}

Entrez du texte: Numéro 2 Reprise du chapitre 3 - atelier 3 - numéro 5. Demandez une chaîne de caractère à l'utilisateur. Avec un dictionnaire, faites le décompte de chaque caractères saisis (il y a 5 'a', 8 'b', etc.). Défi: Comptez le nombre de chaque lettre (a-z), caractères spéciaux (tous ensemble) et caractères d'espacements (tous ensembles). Pour les lettres, les minuscules, majuscules et accents compte pour la même lettre (A, a et à compte pour la lettre a).
{'n': 14, 'u': 19, 'm': 15, 'e': 66, 'r': 24, 'o': 13, 'espace': 75, 'spécial': 39, 'p': 11, 'i': 16, 's': 25, 'd': 10, 'c': 25, 'h': 4, 'a': 33, 't': 30, 'l': 18, 'z': 3, 'v': 1, 'f': 2, 'q': 2, 'y': 1, 'b': 4, 'x': 1, 'j': 1}
```

## Numéro 3

Selon le dictionnaire suivant (noms créés par ChatGPT 4o mini):

```py
personnes: {str: int} = {
    "Alice Tolérance": 92,
    "Bob L'éponge": 58,
    "Clara Té": 76,
    "David Tennant": 99,
    "Emma Gination": 45,
    "Franck Poin": 61,
    "Gérard Mène": 84,
    "Hélène Droit": 72,
    "Iris Cible": 33,
    "Jack Pot": 66,
    "Kévin Prénom": 90,
    "Léo Tard": 19,
    "Monique Rire": 53,
    "Nina Faim": 88,
    "Oscar Doute": 27,
    "Paul Choisir": 41,
    "Quentin Démarre": 69,
    "Rita Joye": 55,
    "Sophie Tentation": 30,
    "Tom Alerte": 81
}
```

Affichez le nom de la personne ayant le plus haut score et celui de la personne ayant le plus petit score.

Défi: Faites une fonction qui prend un dictionnaire en paramètre et retourne un tuple contenant la réponse.

```
Plus petit: Léo Tard avec le score 19
Plus grand: David Tennant avec le score 99
```

## Numéro 4

Affichez le menu suivant à l'utilisateur:

```
Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
```

Vous aurez une liste de joueurs, chaque joueur sera un dictionnaire qui contient son nom et son score.

### Option 1 - Ajouter un joueur

Faites une fonction `estDansListe` qui vérifie si le nom d'utilisateur est dans la liste. Même si ce n'est pas idéal, utilisez un "foreach" dans cette fonction.

Demandez le nom d'utilisateur, validez qu'il contient au moins 3 caractère et qu'il est unique. Si tout est beau, l'ajouter à la liste avec un score de zéro.

### Option 2 - Jouer une partie

Choisir un joueur au hasard, augmentez son score de 1. Affichez qu'il a gagné un point.

### Option 3 - Afficher le score

Affichez le nom de chaque joueur avec son score.

Défi: Affichez celui qui a le plus haut score pour commencer.

```
Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 1
Entrez le nom du joueur: aaa

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 1
Entrez le nom du joueur: bbb

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 1
Entrez le nom du joueur: ccc

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo ccc

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo aaa

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo ccc

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo aaa

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo bbb

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 2
Bravo ccc

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 3
ccc - 3
aaa - 2
bbb - 1

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 6
Choix invalide

Veuillez choisir une des option suivante:
  1 - Ajouter un joueur
  2 - Jouer une partie
  3 - Afficher le score
  4 - Quitter
Votre choix: 4
```