# Chapitre 1 - Atelier 2 - Opérateurs et expressions

## Numéro 1

Dans un fichier Python, déclarez les variables suivantes:

```py
nb1: int = 5
nb2: float = 2.5
nb3: int
test: bool = False
texte: str = "AB"
code: int = 3
```

Pour chaque ligne suivante, quel sera la valeur et le type du résultat? Certaines lignes vont causer une erreur!

```py
nb1 + 4 % nb1 * 3 - 6
nb1 % 2 % 2 / 2
nb1 % 2 % 2 / 2.0
(nb2 / 2.5) == 1.0
test or (nb2 == (nb1 / 2))
nb1 / 2
nb1 / 2.5
nb1 + texte
(nb1 * 3 % 3) == 3
1 / (nb1 + nb2)
1 / (nb1 + 2)
(nb1 / nb2) != (nb1 / 2)
(nb1 > 2) and (nb1 < 5)
test or (nb1 == 5) and (nb2 > 2)
nb1 / code
nb2 - test
nb3 - 1
nbl / 5
5 % 2 * 7 + 6 / 2
(5 % 2 * 7 + 6) / 2
-nb1 % 2
and test
nb1 / 5
```

## Numéro 2

Trouvez le résultat de chaque opération.

```py
d1: float = 1 / 3.0
d2: float = 1 / 3
i1: int = 10
i2: int = 100
i3: int = 1000
i4: int = 100

i1 * i1
i1 * d2
i1 + d1
i1 * d1
i1 / 0
i2 % 3
i3 % 100
i4 - 100.0
```

## Numéro 3

Trouvez le résultat de chaque opération.

```py
x: int = 5
y: int = 10

(x > 0) and (y > 0)
(x > y) and (y == 10)
(x == 0) or (y == 0)
(x == 0) or (y == 10)
(x > 0) or (y > 0)
not(x > 0)
not not(y != 0)
not(x >= 0 and x <= 10)
((x % 10 == 5) or (y % 10 == 0)) and (x + y > 100)
(x % 10 == 5) or (y % 10 == 0) and (x + y > 100)
```

## Numéro 4

Pour tous les problèmes suivants, identifiez les variables et les constantes puis faites les calculs. Notez que plusieurs exemples ont été arrondis par simplicité, vous n'avez pas à arrondir.

### Problème 1

Calculez l'aire d'un rectangle

Exemple: Un rectangle de 3 par 7 a une aire de 21.

### Problème 2

Convertissez une température en Fahrenheit vers le Celsius

Exemple: 72F donne 22.2C

### Problème 3
Calculez l'âge d'une personne en considérant seulement l'année actuelle et son année de naissance

Exemple: Pour l'année 2024, quelqu'un né en 1990 a 34 ans

### Problème 4

Calculez la circonférence d'un cercle. Vous pouvez utiliser seulement 4 décimales pour PI

Exemple: Un cercle de rayon de 5 a une circonférence de 31.42

### Problème 5

Calculez la moyenne de 3 notes

Exemple: La moyenne des notes 85, 62 et 78 est de 75

### Problème 6

Vous achetez une certaine quantité d'un produit. Calculez le sous-total, puis le total avec les 2 taxes

Exemple: Si j'achète 3 produits à 18.99$, le total sera de 65.50$

### Problème 7

Même chose que le numéro 6, mais sans faire de sous-total, le calcul complet doit être fait d'un coup

Exemple: Si j'achète 3 produits à 18.99$, le total sera de 65.50$

### Problème 8

Un marathonien finis sa course, on lui donne son temps en heures, minutes et secondes. Combien de secondes au total a-t-il pris pour faire sa course?

Exemple: Un temps de 4:32:49 donne un total de 16369 secondes

### Problème 9

Inverse du numéro précédent. Un juge coquin décide de donner le temps du marathonien en secondes seulement. Combien d'heures, minutes et secondes a-t-il pris pour faire sa course?

Exemple: Un total de 17823 secondes donne un temps de 4:57:03

Pour ce dernier numéro, vous pouvez `print` plusieurs valeurs d'un coup comme ceci: `print(a, b, c)`