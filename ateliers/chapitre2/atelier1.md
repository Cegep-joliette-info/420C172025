# Chapitre 2 - Atelier 1 - If

## Numéro 1

Copiez le code suivant:

```py
age: int = 20

print("Quel âge avez-vous?", age, "ans")

print("Vous êtes ");
if age < 13:
    print("\t- trop jeune pour créer un compte Facebook")

if age < 35:
    print("\t- trop jeune pour être le président des USA ")
print("Quel dommage!")
```

 1. Testez le code afin de comprendre l'instruction IF
 2. Si vous affectez 35 à la variable âge, qu'arrive-t-il et pourquoi?
 3. Réparer le code afin que (Quel dommage!) s'affiche avec la condition (age < 35).
 4. Modifier le if (age < 13) afin que si l'âge est plus grand ou égal à 13, il va afficher "assez vieux pour créer un compte Facebook"
 5. Écrire un IF permettant d'afficher "\t- trop jeune pour avoir un permis de conduire" si l'âge est plus petit que 16 et afficher "\t- assez vieux pour avoir un permis de conduire" sinon.
 6. Écrire un IF permettant d'afficher "\t- trop jeune pour avoir un tatou" si l'âge est plus petit que 18 et afficher "\t- assez vieux pour avoir un tatou" sinon.
 7. Écrire un IF permettant d'afficher: "\t- assez vieux pour la retraite" si l'âge est plus grand ou égal à 65 et afficher "\t- trop jeune pour la retraite" sinon.

## Numéro 2

Écrire un algorithme qui selon le sexe (H,h,F,f,A,a), le prénom et le nom, affiche un message approprié. 

Tests:

```
Prénom, nom et sexe (H,h,F,f,A,a): France Beaudoin f    Bonjour madame France Beaudoin
Prénom, nom et sexe (H,h,F,f,A,a): Jean Bon H           Bonjour monsieur Jean Bon
Prénom, nom et sexe (H,h,F,f,A,a): Amphès Dlapen F      Bonjour madame Amphès Dlapen
Prénom, nom et sexe (H,h,F,f,A,a): Alex Thérieur h      Bonjour monsieur Alex Thérieur
Prénom, nom et sexe (H,h,F,f,A,a): Fred Groleau a       Bonjour Fred Groleau
Prénom, nom et sexe (H,h,F,f,A,a): Fred Groleau A       Bonjour Fred Groleau
```

## Numéro 3

Écrire un algorithme qui vérifie si un entier est positif, négatif ou égal à zéro. 

Tests: 

```
Avec l'entier: -1    -1 est négatif
Avec l'entier: 50    50 est positif
Avec l'entier: 0     0 est égal à zéro
```

## Numéro 4

Écrire un algorithme qui selon un nombre (1-7) donne le jour correspondant. 

Tests: 

```
Avec le nombre: 1     1 : dimanche
Avec le nombre: 3     3 : mardi
Avec le nombre: 7     7 : samedi
Avec le nombre: 50    50 : -
```

## Numéro 5

Écrire un algorithme qui calcul le prix final en fonction du montant initial. Les taxes sont ajoutés après le calcul du rabais.
Les montants de 100$ et plus ont droit à un rabais de 10%, les montants entre 50$ et 100$ ont droit à un rabais de 5$ et les montants de moins de 50$ n'ont droit à aucun rabais.

Tests:

```
Avec 19.99:     22.9835025
Avec 72.41:     77.5046475
Avec 99.99:     109.2147525
Avec 100:       103.4775
```

## Numéro 6 - Défi

Les droits utilisateurs sont saisis sous forme d'un nombre binaire sur 4 bits. Chaque droit est encode en binaire, ils donnent accès à un module spécifique:

 * 1- RH
 * 2- Inventaire
 * 4- Comptabilité
 * 8- Informatique

Tests:

```
Avec 0b1011:
 - Accès au module RH
 - Accès au module Inventaire
 - Accès au module Informatique

Avec 0b0000:
 - Accès à aucun module

Avec 0b0100:
 - Accès au module Comptabilité
```