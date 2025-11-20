# Chapitre 4 - Atelier 3 - Expressions régulères

Faites tous les numéros suivants avec des expressions régulières.

## Numéro 1

Demandez du texte à l'utilisateur, affichez tous les nombres saisies, incluant les nombres négatifs et décimaux.

Exemple:

```
Entrez du texte et des chiffres: a4e -97 4.56 ,34 0,12 -98.123 3 123.
['4', '-97', '4.56', '34', '0', '12', '-98.123', '3', '123']
```

## Numéro 2

Remplacez toutes les variantes du mot banane (banana, banano, binona, etc.) par BANANA. Les consonnes doivent rester les mêmes, mais les voyelles peuvent être n'importe lesquelles.

Exemple:

```
Entrez des bananes: Banane babone bonani bibino BENANA
BANANA babone BANANA bibino BANANA
```

## Numéro 3

Demandez du texte à l'utilisateur, validez si c'est un numéro de local valide du cégep.
Un numéro de local contient:

 1. Code de l'aile: A, B, C ou D
 2. Un tiret, optionnel
 3. Un chiffre entre 0 et 6
 4. Deux chiffres entre 0 et 9

Exemples de numéros de locaux valides: A-314, C222, B654, D043

Exemples de numéros de locaux invalides: C-789, H123, E 123, ABC

Exemples de résultat:

```
Entrez un numéro de local: C-224
Ce local existe à Joliette

Entrez un numéro de local: G602
Ce n'est pas un local valide

Entrez un numéro de local: A802
Ce n'est pas un local valide

Entrez un numéro de local: B599
Ce local existe à Joliette
```