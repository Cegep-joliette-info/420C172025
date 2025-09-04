# Chapitre 2 - Atelier 2 - Lecture au clavier

Vous pouvez reprendre tous les problèmes de [Chapitre 1, Atelier 2, Numéro 4](../chapitre1/atelier2.md) ou [Chapitre 2, Atelier 1, Numéros 2 à 6](atelier1.md) et demandez les informations variables à l'utilisateur au lieu de les figer dans le code (*hardcoded*).

## Numéro 1

Demandez à l'utilisateur une température en Celsius. Convertissez cette température en Fahrenheit.

Exemple en console:
```
Entrez une température en Celsius: 22
Température en Farenheit: 71.6
```

## Numéro 2

Demandez à l'utilisateur une longueur et une largeur. Affichez si c'est un carré ou un rectangle puis calculez son aire.

Exemple 1:
```
Veuillez entrer une longueur: 10
Veuillez entrer une largeur: 10
C'est un carré
Aire de 100
```

Exemple 2:
```
Veuillez entrer une longueur: 42
Veuillez entrer une largeur: 5
C'est un rectangle
Aire de 210
```

## Numéro 3

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

## Numéro 4

Demandez à l'utilisateur 5 notes, faites la moyenne puis affichez le résultat en pourcentage sur 2 décimales.

Exemple:
```
Veuillez entrer la note #1: 75
Veuillez entrer la note #2: 92
Veuillez entrer la note #3: 41
Veuillez entrer la note #4: 60
Veuillez entrer la note #5: 88

La moyenne est de: 71.20%
```

## Numéro 5

Écrire le code pour obtenir le résultat (exemple ci-dessous) à la console.

Demandez à l'utilisateur de saisir les nombres 1, 2 et 4 puis faites les calculs.

Exemple 1:

```
Veuillez saisir nb1, un entier: 7
Veuillez saisir nb2, un entier: 4
Veuillez saisir nb4, un réel: 4

La valeur de nb1 est 7
La valeur de nb2 est 4
La valeur de nb4 est 4.0
---------------------------------
7 + 4 = 11
7 - 4 = 3
7 * 4 = 28
7 / 4 = 1.75
7 / 4.0 = 1.75
7 // 4 = 1
7 // 4.0 = 1.0
7 % 4 = 3
7 % 4.0 = 3.0
---------------------------------
nb2 == nb4 : 4 == 4.0 : True
nb2 != nb4 : 4 != 4.0 : False
nb1 > nb2 : 7 > 4 : True
nb1 >= nb4 : 7 >= 4.0 : True
---------------------------------
```

Exemple 2:

```
Veuillez saisir nb1, un entier: 22
Veuillez saisir nb2, un entier: 3
Veuillez saisir nb4, un réel: 5.0

La valeur de nb1 est 22
La valeur de nb2 est 3
La valeur de nb4 est 5.0
---------------------------------
22 + 3 = 25
22 - 3 = 19
22 * 3 = 66
22 / 3 = 7.333333333333333
22 / 5.0 = 4.4
22 // 3 = 7
22 // 5.0 = 4.0
22 % 3 = 1
22 % 5.0 = 2.0
---------------------------------
nb2 == nb4 : 3 == 5.0 : False
nb2 != nb4 : 3 != 5.0 : True
nb1 > nb2 : 22 > 3 : True
nb1 >= nb4 : 22 >= 5.0 : True
---------------------------------
```

## Numéro 6

Demandez à l'utilisateur d'entrer un nombre, dites si ce nombre est:

 * Positif, négatif ou null
 * Pair ou impair

Exemples:
```
Veuillez entrer un nombre: -5
Le nombre -5 est négatif et impair

Veuillez entrer un nombre: 42
Le nombre 42 est positif et pair
```

## Numéro 7

Demandez 2 nombres à l'utilisateur, affichez les du plus petit au plus grand.

```
Veuillez saisir le nombre 1: 42
Veuillez saisir le nombre 2: -9
-9 42

Veuillez saisir le nombre 1: 0
Veuillez saisir le nombre 2: 9001
0 9001
```

## Numéro 8

Demandez à l'utilisateur s'il veut convertir du Fahrenheit vers le Celsius ou l'inverse, demandez ensuite une température puis faites la conversion.

```
Voulez-vous convertir:
1: du Farenheit au Celsius
2: du Celsius au Farenheit
Veuillez saisir 1 ou 2: 1
Entrez une température en Farenheit: 72
Température en Celsius: 22.22

Voulez-vous convertir:
1: du Farenheit au Celsius
2: du Celsius au Farenheit
Veuillez saisir 1 ou 2: 2
Entrez une température en Celsius: 24
Température en Farenheit: 75.20
```

## Numéro 9

Demandez à l'utilisateur de choisir une opération mathématique (addition, multiplication, division et soustraction) puis de choisir 2 nombres.
Affichez le résultat de l'opération choisie sur les 2 nombres, attention à la division par zéro, le programme ne doit pas planter!

Ajoutez aussi une valiation en cas d'opérateur invalide

```
Veuillez choisir une opération (+, -, *, /): +
Veuillez saisir le nombre 1: 5
Veuillez saisir le nombre 2: 8
5 + 8 = 13

Veuillez choisir une opération (+, -, *, /): /
Veuillez saisir le nombre 1: 42
Veuillez saisir le nombre 2: 0
Impossible de diviser par zéro

Veuillez choisir une opération (+, -, *, /): Non
Veuillez saisir le nombre 1: 0
Veuillez saisir le nombre 2: 0
Opération non-valide
```

## Numéro 10

Reprenez le numéro 8, mais l'utilisateur peut aussi choisir les degrés Kelvin. Il devra aussi choisir vers quelle unité il veut convertir. Arrondissez toutes les réponses à 1 décimale.

```
Les unites disponibles sont:
1 - Kelvin
2 - Celsius
3 - Farenheit
Veuillez choisir l'unité source (1, 2 ou 3): 2
Veuillez saisir la température source: 24
Veuillez choisir l'unité de destination (1, 2 ou 3): 1
297.15

Les unites disponibles sont:
1 - Kelvin
2 - Celsius
3 - Farenheit
Veuillez choisir l'unité source (1, 2 ou 3): 3
Veuillez saisir la température source: 72
Veuillez choisir l'unité de destination (1, 2 ou 3): 2
22.22
```