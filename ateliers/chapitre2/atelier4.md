# Chapitre 2 - Atelier 7 - While

Tous les numéros (sauf le #1) doivent être résolus avec l'instruction `while`.

## Numéro 1

Sans l'exécuter, que va afficher le code suivant?

```py
n: int
p: int

n = 0
p = 0
while n < 5:
    n += 2

p += 1

print("A : n = " + str(n) + ", p = " + str(p))

n = 0
p = 0
while n < 5:
    n += 2
    p += 1

print("B : n = " + str(n) + ", p = " + str(p))
```

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

Faites la somme de tous les nombres à partir de 1. Arrêtez immédiatement lorsque la somme dépasse 1000.

```
Réponse: 1035
```

## Numéro 6

Faites la somme de tous les nombres à partir de 1. Arrêtez juste avant que la somme dépasse 1000.

```
Réponse: 990
```

## Numéro 7

Calculez manuellement la factorielle d'un nombre saisi par l'utilisateur. Par exemple, la factorielle de 5 est `5 x 4 x 3 x 2 x 1`.

```
Veuillez entrer un nombre: 7
7! = 5040
```

## Numéro 8

Calculer et afficher les racines carrées de nombre entier lu. Les entiers négatifs sont refusés. Arrêter le programme lorsque l'entier lu est 0.

Exemple:

```
Entrez un entier positif: 2
Sa racine carrée est: 1.4142135623730951

Entrez un entier positif: -3
Un entier positif svp!

Entrez un entier positif: 5
Sa racine carrée est: 2.23606797749979

Entrez un entier positif: 0
Fin
```

## Numéro 9

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

## Numéro 10

Demandez 2 nombres à l'utilisateur, faites la multiplication entre ces 2 nombres en utilisant seulement le `+`. Ne pas considérer les nombres négatifs.

```
Veuillez entrer un nombre: 3
Veuillez entrer un nombre: 4
3 * 4 = 12
```

## Numéro 11

Demandez 2 nombres à l'utilisateur. Faites l'exposant en utilisant seulement des additions.

```
Veuillez entrer un nombre: 2
Veuillez entrer un nombre: 8
2 ** 8 = 256
```

## Numéro 12

Demandez 2 nombres à l'utilisateur, calculez le PGCD entre ces 2 nombres.

```
Veuillez entrer un nombre: 25
Veuillez entrer un nombre: 15
Le PGCD de 25 et 15 est 5
```

## Numéro 13

Demandez 2 nombres à l'utilisateur, calculez le PPCM entre ces 2 nombres.

```
Veuillez entrer un nombre: 8
Veuillez entrer un nombre: 12
Le PPCM de 8 et 12 est 24
```

## Numéro 14

Demandez un nombre à l'utilisateur, inversez ce nombre (1234 deviendra 4321). Vous ne devez pas convertir le nombre en string.

```
Veuillez entrer un nombre: 1234
L'inverse de 1234 est 4321
```

## Numéro 15 - Défi

Demandez un nombre plus grand que 1 à l'utilisateur, reposer la question s'il ne respecte pas la règle jusqu'à ce que le nombre soit valide.

Avec ce nombre, calculez et affichez le nombre d'étapes dans la conjecture de Syracuse:

 * Si le nombre est pair, diviser par deux;
 * Si le nombre est impair, multiplier par trois plus un;
 * Arrêter rendu lorsque le nombre vaut 1;

Optionnel: affichez chaque nombre de la suite.

Exemples:
```
Entrez un nombre plus grand que 1: -5
Entrez un nombre plus grand que 1: 1
Entrez un nombre plus grand que 1: 2
La suite débutant par 2 a 2 éléments.
```
```
Entrez un nombre plus grand que 1: 7
La suite débutant par 7 a 16 éléments.
```

Exemple avec le optionnel:
```
Entrez un nombre plus grand que 1: 7
7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
La suite débutant par 7 a 17 éléments.
```