# Chapitre 2 - Atelier 5 - For

Sauf pour le numéro 1:
Tous les numéros doivent être résolus avec l'instruction `for`. Cet atelier reprends les numéros de l'atelier précédent.

## Numéro 1

Ouvrez l'atelier précédent (atelier des `while`), sauf pour le numéro 1, regardez tous les numéros (même si vous ne l'avez pas fait). Demandez-vous si c'est possible de faire ce numéro avec un `for`, sinon pourquoi?

## Numéro 2

Comptez de 1 à 10, un numéro par ligne.

```
1
2
3
4
5
6
7
8
9
10
```

Vous pouvez essayer de l'afficher comme ceci:

```
1 - 2 - 3 - 4 - 5 - 6 - 7 - 8 - 9 - 10
```

## Numéro 3

Afficher la série suivante de nombres entiers (1 nombre par ligne): 5, 10, 15, 20, 25, 30, …, 90, 95, 100

## Numéro 4

Faites la somme de tous les nombres de 1 à 100.

```
La somme de tous les nombres entre 1 et 100: 5050
```

## Numéro 5

Calculez manuellement la factorielle d'un nombre saisi par l'utilisateur. Par exemple, la factorielle de 5 est `5 x 4 x 3 x 2 x 1`.

```
Veuillez entrer un nombre: 7
7! = 5040
```

## Numéro 6

Afficher un triangle formé d'étoiles. La hauteur du triangle (c’est-à-dire son nombre de lignes) est lue.

Exemple:

```
Combien de lignes? 8
*
**
***
****
*****
******
*******
********
```

## Numéro 7

Demandez 2 nombres à l'utilisateur, faites la multiplication entre ces 2 nombres en utilisant seulement le `+`. Ne pas considérer les nombres négatifs.

```
Veuillez entrer un nombre: 3
Veuillez entrer un nombre: 4
3 * 4 = 12
```

## Numéro 8

Demandez un nombre à l'utilisateur, inversez ce nombre (1234 deviendra 4321).

Pour savoir combien il y a de chiffre dans le nombre, utilisez:
```py
# La variable `nb` contient le nombre saisis par l'utilisateur
nbChiffres: int = len(str(nb))
```

Exemple de résultat:

```
Veuillez entrer un nombre: 1234
L'inverse de 1234 est 4321
```

## Numéro 9 - Défi

Demandez 2 nombres à l'utilisateur. Faites l'exposant en utilisant seulement des additions.

```
Veuillez entrer un nombre: 2
Veuillez entrer un nombre: 8
2 ** 8 = 256
```