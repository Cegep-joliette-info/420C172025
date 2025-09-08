# Boucle while

Une boucle ou itération est l'exécution à répétition d'une instruction ou d'un bloc d'instructions. Le nombre d'itération n'est pas forcément connu en entrant dans la boucle.

Le `while` a la structure suivante:

```
while instruction_booléenne:
    code répété x fois
```

Exemple, au lieu de faire:

```py
print(5)
print(4)
print(3)
print(2)
print(1)
print("GO")
```

On peut faire:

```py
i: int = 5

while i > 0:
    print(i)
    i -= 1

print("GO") 
```

Avec la solution while, commencez le compteur à 200 si vous voulez, le code ne change presque pas.
Attention à la ligne `i -= 1`, sans cette ligne le while ne terminera jamais! C'est ce qu'on appel une boucle infini.

```py
i: int = 5

# Boucle infinie!
while i > 0:
    print(i)
    i += 1

print("GO") 
```

On peut mettre un else dans un while, dans ce cas le else sera exécuté à la fin du while:

```py
i: int = 5

while i > 0:
    print(i)
    i -= 1
else:
    print("GO") 
```

Les instructions `break` et `continue` (ou similaire) sont refusés dans ce cours.
Ces mots-clés seront supprimés des évaluations avant la correction s'ils sont utilisés.