# Chapitre 3 - Atelier 2 - Tableaux et méthodes

Consignes

 * Interdiction : instructions break, continue, return ou de même nature dans une boucle.
 * Une fonction doit avoir une seule instruction return
 * Pour l'atelier vous n'avez pas de commentaires à écrire
 * Attention aux divisions par zéro

## Problème 1

Écrire une fonction nbReussite qui retourne le nombre de réussites à partir d'un tableau de notes.

Tester avec:

```py
notes: npt.NDArray[np.int_] = np.array([10, 50, 8, 30, 9, 17, 36])
nbReussites: int = nbReussites(notes)
print(nbReussites) # Affiche 0
```
```py
notes: npt.NDArray[np.int_] = np.array([10, 50, 80, 30, 99, 75, 60])
nbReussites: int = nbReussites(notes)
print(nbReussites) # Affiche 4
```

## Problème 2

Écrire une fonction afficherNbTab qui affiche les nb premiers éléments d'un tableau d'entiers. Vous pouvez faire des print dans la fonction, notez que c'est exceptionnel.

```py
tab: npt.NDArray[np.int_] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
afficherNbTab(tab, 0) # Affiche rien
```
```py
tab: npt.NDArray[np.int_] = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
afficherNbTab(tab, 52) # Affiche: 1 2 3 4 5 6 7 8 9 10
```

## Problème 3

Écrire une fonction salaireMoyen qui retourne le salaire moyen à partir d'un tableau de salaires.

```py
salaires: npt.NDArray[np.float_] = np.array([35000, 42500, 55000, 125_000, 33000])
moyenne: float = salaireMoyen(salaires)
print(moyenne) # Affiche 58100.0
```
```py
salaires: npt.NDArray[np.float_] = np.array([])
moyenne: float = salaireMoyen(salaires)
print(moyenne) # Affiche 0.0
```

## Problème 4

Écrire une fonction salaireMoyen0 qui retourne le salaire moyen à partir d'un tableau de salaires. La fin des données est indiquée par un salaire à 0, le tableau contient au moins une valeur 0.

```py
salaires: npt.NDArray[np.float_] = np.array([0, 35000, 42500, 55000, 125_000, 33000])
moyenne: float = salaireMoyen0(salaires)
print(moyenne) # Affiche 0.0
```
```py
salaires: npt.NDArray[np.float_] = np.array([35000, 42500, 55000, 125_000, 33000, 0])
moyenne: float = salaireMoyen0(salaires)
print(moyenne) # Affiche 58100.0
```
```py
salaires: npt.NDArray[np.float_] = np.array([35000, 42500, 55000, 0, 125_000, 33000])
moyenne: float = salaireMoyen0(salaires)
print(moyenne) # Affiche 44166.666666666664
```

## Problème 5

Écrire une fonction max2 qui retourne la plus grande valeur à partir d'un tableau d'entiers. Dans ce contexte le tableau ne peut pas être vide. Ne pas utiliser la fonction `max` de Python.

```py
tab: npt.NDArray[np.int_] = np.array([22, 105, 1, -4, 33, 39])
maximum: int = max2(tab)
print(maximum) # Affiche 105
```

## Problème 6

Écrire une fonction min2 qui retourne la plus petite valeur à partir d'un tableau d'entiers. Dans ce contexte le tableau ne peut pas être vide.

```py
tab: npt.NDArray[np.int_] = np.array([22, 105, 1, -4, 33, 39])
minimum: int = min2(tab)
print(minimum) # Affiche -4
```

## Problème 7

Écrire une méthode premierNegatif qui retourne la première valeur négative à partir d'un tableau d'entiers. Si le tableau ne contient pas de valeur négative retourner 0. Attention pas de return dans une boucle.

```py
tab: npt.NDArray[np.int_] = np.array([-1, 22, 0, -55, 4, -3, 9, -2])
negatif: int = premierNegatif(tab)
print(negatif) # Affiche -1
```
```py
tab: npt.NDArray[np.int_] = np.array([1, 22, 0, 55, 4, 3, 9, -2])
negatif: int = premierNegatif(tab)
print(negatif) # Affiche -2
```
```py
tab: npt.NDArray[np.int_] = np.array([1, 22, 0, -55, 4, -3, 9, -2])
negatif: int = premierNegatif(tab)
print(negatif) # Affiche -55
```
```py
tab: npt.NDArray[np.int_] = np.array([1, 22, 0, 55, 4, 3, 9, 2])
negatif: int = premierNegatif(tab)
print(negatif) # Affiche 0
```

## Problème 8

Écrire une fonction nbPositif qui retourne le nombre d'entiers positifs se trouvant dans un tableau d'entiers.

Écrire une fonction tabPositif qui retourne un tableau contenant toutes les valeurs positives à partir d'un tableau d'entiers reçu en argument. Utilise la fonction nbPositif.

```py
tab: npt.NDArray[np.int_] = np.array([1, -22, 0, 55, -4, 3, -9, -2])
tabPos: npt.NDArray[np.int_] = tabPositif(tab)
print(tab)  # Affiche [  1 -22   0  55  -4   3  -9  -2]
print(tabPos)  # Affiche [ 1  0 55  3]
```

Écrire une fonction nbNegatif qui retourne le nombre d'entiers négatifs se trouvant dans un tableau d'entiers.

Écrire une fonction tabNegatif qui retourne un tableau contenant toutes les valeurs négatives à partir d'un tableau d'entiers reçu en argument. Utilise la fonction nbNegatif.

```py
tab: npt.NDArray[np.int_] = np.array([1, -22, 0, 55, -4, 3, -9, -2])
tabNeg: npt.NDArray[np.int_] = tabNegatif(tab)
print(tab)  # Affiche [  1 -22   0  55  -4   3  -9  -2]
print(tabNeg)  # Affiche [-22  -4  -9  -2]
```