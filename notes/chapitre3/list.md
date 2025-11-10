# Listes

Une liste s'utilise comme un tableau et a une utilité similaire. La liste est plus flexible que le tableau numpy, mais sera plus lent. Un tableau numpy va réserver des espaces mémoires continus dans la ram, tandis que la liste va être séparé ce qui explique la différence de rapidité.

```py
tab: np.ndarray[int] = np.array([1, 2, 3])
tab[0] = 4
print(tab[0])
# Idem mais avec une liste:
tab: list[int] = [1, 2, 3]
tab[0] = 4
print(tab[0])
```

La liste sera donc à prévilégier lorsque la taille de la liste/tableau est modifiable dans le temps, pas besoin de créer un nouvel objet avec la liste!

C'est une des 4 structure de données en Python. En théorie on peut mélanger les types, mais nous allons faire des listes du même type, exemple:

```py
lst1: list = [1, True, "asdf", 42.3] # Fonctionne, mais à éviter
lst2: list[int] = [1, 2, 3] # Parfait!
```

Il n'y a pas d'équivalent à `empty`, `zeroes`, `ones` et `full`, il faut donc connaître la liste avec les valeurs initiales ou en liste vide.

```py
lst1: list[int] = [1, 2, 3]
lst2: list[int] = []
```

Comme la liste est faite pour être plus flexible, il faut pouvoir modifier la taille:

```py
lst: list[int] = [1, 2, 3]
lst.append(4) # ajoute une case contenant 4 à la fin
lst.insert(0, 5) # ajoute une case contenant 5 à la position 0, donc au début
lst.pop(2) # retire la case à la position deux
lst.pop() # retire la dernière case du tableau, équivalent à pop(-1)
lst.clear() # retire toutes les cases du tableau
```

Les fonctions de listes non écrites dans ce document ne seront pas acceptés au TP2.

Il est possible de faire quelques opérations mathématiques:

```py
[1, 2, 3] + [4, 5, 6] # Donne la liste [1,2,3,4,5,6]
[0] * 5 # Donne la liste [0,0,0,0,0]
```

## Indices négatifs

Notez que les indices négatifs existent, ça permet d'aller chercher des cases à partir de la droite, commençant à -1.

```py
lst: list[int] = [1, 2, 3, 4, 5]
print(lst[len(lst) - 1]) # Affiche 5
print(lst[-1]) # Affiche 5
print(lst[-2]) # Affiche 4
print(lst[-6]) # Plante, OutOfBound
```

## Découpage

Je peux créer des tableaux basés sur un premier tableau, on appel ce processus le découpage (*slicing*). Un *slice* utilise une logique similaire au `range`:

```py
lst: list[int] = [1, 2, 3, 4, 5]
lst[1:] # [2, 3, 4, 5]
lst[:3] # [1, 2, 3]
lst[:-1] # [1, 2, 3, 4]
lst[1:3] # [2, 3]
lst[::2] # [1, 3, 5]
```

Un *slice* va faire une copie du tableau, il y a 3 paramètres possibles et doit avoir au moins un `:` pour faire un *slice*.

## Compréhension de liste

Similaire au if ternaire, on peut faire des boucles simples en une ligne sur des listes:

```py
lst: list[int] = [1, 2, 3, 4, 5]
# Solution 1
for i in range(len(lst)):
    lst[i] = lst[i] ** 2

# Solution 2
lst = [x ** 2 for x in lst]
```

On peut utiliser la même logique pour avoir une liste de nombres comme la précédente:

```py
lst: list[int] = [i for i in range(1, 6)]
```

On peut aussi ajouter une condition à tout ça, avec un if ou un if ternaire:

```py
lst: list[int] = [1, 2, 3, 4, 5]
lst = [x for x in lst if x > 2] # [3, 4, 5]
lst = [x if x > 2 else 0 for x in lst] # [0, 0, 3, 4, 5]
```