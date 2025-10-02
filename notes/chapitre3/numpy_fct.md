# Tableaux et fonctions

Lorsqu'une fonction est invoquée avec un tableau en argument, c'est une copie de la référence du tableau qui est transmise à la fonction.

La fonction agit directement sur le tableau reçu en argument.

Il est possible de modifier les éléments du tableau reçu en argument, mais il n'est pas possible de modifier la référence du tableau reçu en argument.

Lorsque une fonction retourne un tableau elle retourne la référence du tableau.

## Exemple

```py
import numpy as np
import numpy.typing as npt

def modifTabParDeux(tableau: npt.NDArray[np.int_]) -> None:
    """Double toutes les valeurs du tableau

    Args:
        tableau: Tableau d'entier à doubler
    """
    i: int
    for i in range(0, len(tableau)):
        tableau[i] *= 2


def creerTabParDeux(tableau: npt.NDArray[np.int_]) -> npt.NDArray[np.int_]:
    """Retourne un nouveau tableau qui contient tous les nombres doublés du tableau original

    Args:
        tableau: Tableau original à doubler

    Return:
        Un tableau d'entier
    """
    nouveauTableau: npt.NDArray[np.int_] = np.empty(len(tableau), int)
    i: int
    for i in range(0, len(tableau)):
        nouveauTableau[i] = tableau[i] * 2
    return nouveauTableau


tab1: npt.NDArray[np.int_] = np.array([1, 2, 3, 4, 5])
tab2: npt.NDArray[np.int_]

modifTabParDeux(tab1)
tab2 = creerTabParDeux(tab1)

print(tab1)
print(tab2)
```

Dans cet exemple:

 * Lorsque la fonction `modifTabParDeux(tab1)` est invoquée c'est la référence de tab1 qui est transmise à la fonction. Donc la fonction agit directement sur le tableau tab1.
 * Lorsque la fonction `creeTabParDeux` retourne un tableau, elle retourne la référence du tableau tab qui est affecté à tab2 dans le main.
 
Rappel : il n'est pas permis d'utiliser les instructions break, continue, return ou de même nature dans une boucle, la condition de la boucle doit être complète.