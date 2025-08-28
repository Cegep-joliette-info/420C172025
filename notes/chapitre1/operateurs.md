# Opérateurs et expressions

Dans `4 + 2` donne 6

```
4 + 2     est une expression
4         est un opérande
2         est un opérande
+         est un opérateur
6         est la valeur de l’expression ou le résultat
```

Les types `int`, `float` et `bool` sont considérés comme des valeurs numériques.

## Opérateurs Arithmétiques

Opérateurs arithmétiques unaires (agit sur une opérande)

| Opérateur | Action                         |
|:---------:|--------------------------------|
|     +     | sans effet                     |
|     -     | change le signe de l'opérateur |

Opérateurs arithmétiques binaires (agit sur deux opérandes)

| Opérateur | Action                        |
|:---------:|-------------------------------|
|     +     | addition                      |
|     -     | soustraction                  |
|     *     | multiplication                |
|     /     | division                      |
|     %     | modulo                        |
|    **     | exposant                      |
|    //     | division entière              |

*Attention `5 / 0`, `5 // 0` ou `5 % 0` fait planter le programme.

## Opérateurs de comparaisons

Opérateurs binaires, les deux opérandes doivent être de même type, le résultat va être booléen.

| Opérateur | Action                 |
|:---------:|------------------------|
|    ==     | égale                  |
|    !=     | est différent          |
|     >     | est plus grand         |
|     <     | est plus petit         |
|    >=     | est plus grand ou égal |
|    <=     | est plus petit ou égal |

##  Opérateurs logiques

Les opérateurs logiques agissent sur des opérandes de type booléen et donnent un résultat de type booléen.

Ils sont présentés dans leur ordre de priorité.

| Opérateur | Action                                                        |
|:---------:|---------------------------------------------------------------|
|    non    | NON logique (opérateur unaire), inverse le booléen            |
|    and    | ET logique, donne vrai si les deux opérandes sont vrai        |
|    or     | OU logique, donne vrai si au moins une des opérandes est vrai |

Table de vérité

|   a   |   b   | a and b | a or b | not a |
|:-----:|:-----:|:-------:|:------:|:-----:|
| False | False |  False  | False  | True  |
| False | True  |  False  |  True  | True  |
| True  | False |  False  |  True  | False |
| True  | True  |  True   |  True  | False |

Attention, dans le cas du `or`, l'opérande de droite est ignorée si l'opérande de gauche est vrai. Ce sera utile lorsque nous allons travailler avec les fonctions.

## Opérateurs de chaînes

Avec l'opérateur `+` permet de concaténer, les 2 opérandes doivent être des chaînes.

Vous pouvez utiliser l'opérateur `*` pour répéter une chaîne.

## Opérateurs binaires

Les opérateurs binaires effectuent des opérations binaires sur deux opérandes numériques.
Nous n'utiliserons pas ces opérateurs dans le cours, ne passez pas trop de temps dessus.

| Opérateur | Nom         | Description                                                             |
|-----------|-------------|-------------------------------------------------------------------------|
| &         | et          | Donne 1 si le bit des 2 nombres est à 1                                 |
| \|        | ou          | Donne 1 si le bit d'au moins un nombre est à 1                          |
| ^         | xor         | Donne 1 si le bit d'un nombre est à 1                                   |
| ~         | non         | Inverse les bits (opérateur unaire)                                     |
| <<        | Left shift  | Multiplie le nombre de gauche par 2, le nombre de fois indiqué à droite |
| >>        | Right shift | Divise le nombre de gauche par 2, le nombre de fois indiqué à droite    |

## Opérateurs d'assignations

L'opérateur d'assignation de base est le `=`. Tous les autres ne sont que des raccourcis.

Opérateurs d'assignations arithmétiques:

 * +=
 * -=
 * *=
 * /=
 * %=
 * //=
 * **=

Opérateurs d'assignations binaires:

 * &=
 * |=
 * ^=
 * \>\>=
 * <<=

Spécial, le `:=` permet d'assigner une variable durant une autre opération. Nous allons éviter cet opérateur.

```py
print(x = 2)  # Erreur
print(x := 2) # Affiche 2 et affecte 2 à x en même temps
```

## Priorité des opérations

Les opérateurs sont évalués de gauche à droite, selon les priorités suivantes:

 * `()`
 * `**`
 * `+`, `-`, `~` (opérateurs unaires)
 * `*`, `/`, `//`, `%`
 * `+`, `-`
 * `<<`, `>>`
 * `&`
 * `^`
 * `|`
 * `==`, `!=`, `>`, `>=`, `<`, `<=`
 * `not`
 * `and`
 * `or`