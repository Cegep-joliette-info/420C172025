# Chapitre 1 - Atelier 1 - Fouille

## Numéro 1

Écrivez la fonction `fouilleInt` qui reçoit en paramètres un tableau NumPy et un nombre. La fonction doit retourner la position de la première occurrence de ce nombre dans le tableau, ou -1 si le nombre n’y apparaît pas.

Par exemple avec `np.array([4, 7, 2, 1, 5, 7, 0, 3])` et `7`, la fonction va me retourner `1`. Avec le même tableau mais le nombre `4`, la fonction va me retourner `-1`.

## Numéro 2

Écrivez la fonction `fouilleString` qui reçoit en paramètres une liste de chaînes et une chaîne à chercher.
La fonction doit retourner la position de la première occurrence, sans considérer la casse, ou `-1` si la valeur n’est pas trouvée.

Exemple :
Avec `["Chat", "CHIEN", "oiseau", "Poisson"]` et `"chien"`, la fonction retourne `1`.
Avec la même liste mais `"POULE"`, la fonction retourne `-1`.

## Numéro 3 - Défi

Écrivez la fonction `fouilleDict` qui reçoit en paramètres une liste de dictionnaires et une valeur à chercher.
La fonction doit retourner la position du premier dictionnaire contenant cette valeur (peu importe la clé).
Si aucun dictionnaire ne contient la valeur, la fonction doit retourner `-1`.

Exemple
```py
liste = [
    {"id": 12, "nom": "Alice"},
    {"id": 15, "nom": "Bob"},
    {"id": 12, "nom": "Charlie"}
]
```

Résultats attendus :

 * `fouilleDict(liste, 12)` → `0`
 * `fouilleDict(liste, "Bob")` → `1`
 * `fouilleDict(liste, "David")` → `-1`