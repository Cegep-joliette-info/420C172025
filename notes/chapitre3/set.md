# Ensemble - *set*

Les ensembles sont une structure de données comme les listes, mais l'ensemble ne garantis pas l'ordre des éléments et ne permet pas les doublons.
Comme ils ne sont pas ordonnés, vous ne pouvez pas utiliser les crochets pour parcourir l'ensemble (`s[0]` ne fonctionne pas).

Les ensembles sont optimisés pour la recherche car ils utilisent une map de hash qui permet de situer un élément rapidement.
Ils incluent aussi plusieurs fonctions utiles comme l'union et l'intersection.

Pour créer un set:

```py
s1: set[int] = {1, 2, 3}
s2: set[int] = set([1, 2, 3])

vide1: set[int] = {}
vide2: set[int] = set()
```

Voici les fonctions de comparaison des sets:

```py
s1: set[int] = {1, 2, 3}
s2: set[int] = {4, 5, 6}
s3: set[int] = {1}

# Les exemples suivants donnent tous True
1 in s1           # Recherche normale
1 not in s2       # Inverse du précédent
s1.isdisjoint(s2) # Donne True si l'intersection est vide
s3.issubset(s1)   # Donne True si l'ensemble est entièrement dans l'autre
s3 <= s1          # Idem
s3 < s1           # Idem, en plus ne sont pas égaux
s1.issuperset(s3) # Donne True si l'ensemble contient entièrement l'autre
s1 >= s3          # Idem
s1 > s3           # Idem, en plus ne sont pas égaux

# Les exemples suivants donnent des sets
# Les exemples sans commentaires font la même chose que le précédent
s1.union(s2)        # {1, 2, 3, 4, 5, 6}
s1 | s2
s1.intersection(s2) # {}
s1 & s2
s1.difference(s2)   # {1, 2, 3}
s1 - s2
s1.symmetric_difference(s2) # {1, 2, 3, 4, 5, 6}, tous les éléments qui sont dans 1 des 2 ensembles, mais pas les 2
s1 ^ s2
```

Les fonctions suivantes modifies les sets:

```py
s1.update(s2)                      # Ajoute s2 à s1
s1 |= s2                           # Idem
s1.intersection_update(s2)         # Garde seulement les éléments présents dans s1 et s2
s1 &= s2                           # Idem
s1.difference_update(s2)           # Retire les éléments de s1 qui sont dans s2
s1 -= s2                           # Idem
s1.symmetric_difference_update(s2) # Garde les éléments qui sont dans s1 ou s2, mais pas dans les 2
s1 ^= s2                           # Idem
s1.add(4)                          # Ajoute 4 au set
s1.remove(4)                       # Retire 4 du set, plante s'il n'est pas présent
s1.discard(4)                      # Retire 4 du set si présent, ne plante pas
s1.pop()                           # Retire un élément du set, pas aléatoire mais on ne sais pas lequel, retourne l'élément retiré
s1.clear()                         # Vide la liste
```

Notez que les opérateurs (`&, |, -, ^`) ne fonctionne que si les 2 opérandes sont des ensembles.
Les fonctions (update, intersection, etc.) fonctionne avec tableau, liste, ensemble, etc.