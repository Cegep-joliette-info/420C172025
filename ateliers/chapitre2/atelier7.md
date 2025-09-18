# Chapitre 2 - Atelier 7 - Fonctions intégrées

## Numéro 1

Calculez l'aire d'un cercle en utilisant la valeur de pi du module math.

Exemple:
```
Entrez le rayon du cercle: 5
L'aire est de: 78.54
```

## Numéro 2

En utilisant les fonctions du module math, calculez le nombre de chance de gagner le gros lot au tirage classique du loto 6/49.

Comment fonction le 6/49: 6 numéros sur les 49 disponibles sont disponibles. Si les 6 numéros sont sur votre billet vous gagnez le gros lot.

Petit défi: Afficher le nombre de chances de gagner en utilisant le séparateur de milier français: l'espace

Exemple de résultat:
```
# Sans le défi:
Vous avez 1 chance sur 13,983,816 de gagner le 6/49

# Avec le défi:
Vous avez 1 chance sur 13 983 816 de gagner le 6/49
```

## Numéro 3

Demandez un texte à l'utilisateur, sur ce texte:

 * Transformez tout en minuscule
 * Remplacez les lettres 'e' par des 'o'
 * Retirez les lettre 'a'
 * Doublez la consonne de votre choix
 * Mettre la première lettre seulement en majuscule

Exemple de résultat:

```
Veuillez écrire quelque chose: Aujourd'hui il fait beau
Ujourrd'hui il fit bou
```

## Numéro 4

Demandez un nombre à l'utilisateur. S'il donne un nombre multipliez le par deux. S'il donne autre chose, insultez le.
Attention, s'il répond `  42` (notez les espaces devant le chiffre) vous devez accepter le nombre.

Exemple:
```
Veuillez saisir un nombre:          5
Le nombre doublé est: 10

Veuillez saisir un nombre: 2,3
Le nombre donné n'est pas valide
```

## Numéro 5

Reprendre le [numéro 3 de l'atelier 2 du chapitre 2](atelier2.md). Corrigez l'erreur d'arrondis lors du calcul des taxes.

*Copie de l'énoncé du numéro 3 de l'atelier 2 du chapitre 2:*

Demandez à l'utilisateur un nombre de produits et un prix unitaire. Affichez sur 2 décimales: Le sous-total, la TPS, la TVQ et le total.

Exemple (remarquez l'erreur d'arrondis):
```
Veuillez entrer un nombre de produits: 4
Veuillez entrer un prix unitaire: 9.99

Sous-total: 39.96
TPS: 2.00
TVQ: 3.99
Total: 45.94
```