# Tuple

Un tuple est une structure de données comme les listes, par contre le tuple est immuable, on ne peut pas modifier ses valeurs!

Le tuple peut être créé de plusieurs manière, mais on va préférer la première:

```py
t1: tuple[int, int] = (1, 2)
t2: tuple[int, int] = 1, 2    # À éviter
t3: tuple[int, int] = tuple([1, 2]) # À éviter

t4: tuple[str, int, bool] = ('coucou', 4, True) # OK
```

Tout comme la liste et le tableau, je peux accéder à un élément spécifique du tuple avec les crochets:

```py
t1: tuple[int, int] = (1, 2)
print(t1[0]) # Affiche 1
```

On utilise les tuples pour:

 * Retourner plusieurs valeurs avec une fonction
 * Représenter des coordonnées (x, y)
 * Représenter des données liés immuables (nom et prénom, les multiples champs d'adresses, etc.)