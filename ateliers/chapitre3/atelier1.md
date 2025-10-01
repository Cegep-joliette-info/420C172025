# Chapitre 3 - Atelier 1 - Tableaux

## Partie 1 - Compréhension

### Numéro 1

Que va afficher ce code à la console?

```py
tabInt: np.ndarray[int] = np.array([-5, 40, -1000, 50, -3000, 3000, 5000, 0, -4, -7])
nb: int = tabInt[0]
i: int = 0

while nb != 0:
    if nb < 0:
        print(nb)
    i += 1
    nb = tabInt[i]
```

### Numéro 2

Que va afficher ce code à la console?

```py
tabSolde: np.ndarray[int] = np.array([100, 6000, 5000, 2000, 1500, 4000, 10000, -100])
somme: int = 0
i: int = 0
solde: int = tabSolde[0]

while solde > 0:
    if (solde >= 1000) and (solde <= 5000):
        somme += 1
    i += 1
    solde = tabSolde[i]
print(somme)
```

### Numéro 3

Que va afficher ce code à la console?

```py
tabLettre: np.ndarray[str] = np.array(['I','N','F','O','R','M','A','T','I','Q','U','E'])
i: int = 0
while tabLettre[i] != 'Q':
    i += 1
print(i)
```

### Numéro 4

Que va afficher ce code à la console?

```py
tabLettre: np.ndarray[str] = np.array(['I','N','F','O','R','M','A','T','I','Q','U','E'])
somme: int = 0
i: int

for i in range(1, 6):
    if tabLettre[i] == 'A':
        somme += 1
print(somme)
```

### Numéro 5

Que va afficher ce code à la console?

```py
tabSexe: np.ndarray[str] = np.array(['M','F','M','F','M','M','A','F','M','A','A'])
tabAge: np.ndarray[int] = np.array([15,18,17,20,38,14,10,69,84,16,27,0])
nbHommes: int = 0
nbFemmes: int = 0
nbAutres: int = 0
nbMajeurs: int = 0
nbLus: int = 0
age: int = tabAge[nbLus]

while age != 0:
    if age >= 18:
        if tabSexe[nbLus] == 'M':
            nbHommes += 1
        elif tabSexe[nbLus] == 'F':
            nbFemmes += 1
        else:
            nbAutres += 1
        nbMajeurs += 1
    nbLus += 1
    age = tabAge[nbLus]

print(nbMajeurs, nbHommes, nbFemmes, nbAutres)
```

### Numéro 6

Faire la trace de l’algorithme suivant.

Faire la trace: sur une feuille, inscrire les valeurs de chaque variable, et suivre la progression du code mentalement en ajustant les valeurs des variables sur la feuille. Une fois terminé, refaites l'exercice avec le débogeur pour voir si la progression est bien celle que vous avez pensé.

```py
tab1: np.ndarray[int] = np.array([33, 2, 5, 34, 25, 4, 8, 13, -1])
tab2: np.ndarray[int] = np.empty(9, int)
tab3: np.ndarray[int] = np.empty(9, int)
ind1: int
ind2: int = 0
ind3: int = 0

for ind1 in range(0, 7):
    if tab1[ind1] % 2 == 0:
        tab2[ind2] = tab1[ind1]
        ind2 += 1
    else:
        tab3[ind3] = tab1[ind1]
        ind3 += 1
```

## Partie 2 - Algorithmie

Vous n'avez pas à valider l'entrée de donnée.
Les étapes données dans les listes à puces doivent être réalisés de manière distincts, donc le code doit réaliser la première puce au complet avant de pouvoir commencer la 2e.

### Algorithme 1

 * Lire au clavier une série de cinq valeurs entières et les conserver dans un tableau.
 * Il faut calculer et afficher la somme et la moyenne des cinq nombres.

Exemple:

```
Veuillez entrer le nombre 1: 1
Veuillez entrer le nombre 2: 2
Veuillez entrer le nombre 3: 3
Veuillez entrer le nombre 4: 4
Veuillez entrer le nombre 5: 5
La somme est: 15
La moyenne est: 3.0
```

### Algorithme 2

 * Créer un tableau d'entiers et l'initialiser avec les valeurs 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
 * Lire au clavier nb et afficher les nb premiers éléments du tableau.
 * Attention à l'exeption IndexError, si nb est plus grand que le nombre d'éléments du tableau afficher tout le tableau.

```
Nombres à afficher: 5
1 2 3 4 5
```
```
Nombres à afficher: 25
1 2 3 4 5 6 7 8 9 10
```

### Algorithme 3

 * Lire la taille du tableau d'entier à créer.
 * Créer le tableau selon la taille et le remplir en ordre croissant à partir de la valeur 5.
 * Afficher le tableau créé.

```
Entrez la taille du tableau: 23
[ 5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27]
```

### Algorithme 4

 * Lire la taille du tableau d'entier à créer.
 * Créer le tableau selon la taille et le remplir des valeurs en ordre décroissant de nb à 1 où nb est la taille.
 * Afficher le tableau créé.

```
Entrez la taille du tableau: 4
[4 3 2 1]
```

### Algorithme 5

 * Créer un tableau d'entiers et l'initialiser de valeurs dont un zéro.
 * Trouver l'indice de l'entier dont la valeur est "zéro" dans le tableau.
 * Afficher le tableau et l'indice trouvé

Pour vous amuser, utilisez `np.random.shuffle(votreTableau)` pour mélanger le tableau.

Les 3 premiers tests suivants ont été fait manuelle, le dernier est avec le random.

```
[0 1 2 3 4 5]
Indice du zéro: 0
```
```
[1 2 3 4 5 0]
Indice du zéro: 5
```
```
[1 2 3 0 4 5]
Indice du zéro: 3
```
```
[4 0 1 2 5 3]
Indice du zéro: 1
```