# Boucle for

La boucle while va être utilisé lorsque le nombre de séquence est inconnue, par exemple lorsqu'on attends que l'utilisateur entre le chiffre zéro, ou si nous voulons voir combien de cycle sont nécessaire pour arriver à un résultat.

Lorsque le nombre de séquence est connue, on va utiliser le `for`.

```
for x in ensemble:
    code répété x fois
```

Exemple, au lieu de faire:

```py
i: int = 5

while i > 0:
    print(i)
    i -= 1

print("GO") 
```

On peut faire:

```py
for i in range(5, 0, -1):
    print(i)

print("GO")
```

La fonction est une fonction spéciale qui nous donne une suite de chiffre, elle accepte entre 1 et 3 arguments:

 * `range(5)`: De 0 à 4
 * `range(5, 10)`: De 5 à 9
 * `range(0, 10, 2)`: De 0 à 10, avec des bons de 2 (0, 2, 4, 6, 8, 10)

Notez que la boucle infinie n'est pas possible avec le for.
Tout comme le while, il y a un else:

```py
for i in range(5, 0, -1):
    print(i)
else:
    print("GO") 
```

Les instructions `break` et `continue` (ou similaire) sont refusés dans ce cours.
Ces mots-clés seront supprimés des évaluations avant la correction s'ils sont utilisés.