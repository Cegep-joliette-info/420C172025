# Match

Le *match* est similaire au *switch* des autres langages, mais il est conçu pour gérer la structure au lieu des valeurs. Pour l'instant, nous allons l'apprendre comme les *switch*. Les autres utilisations seront ajoutés lorsque nous aurons les bons outils.

Une suite if-elif-else permet de faire plusieurs conditions sur des valeurs booléennes. Un *switch* permet de faire des branchements selon les possibilités d'une variable. Exemple:

```py
nb: int = int(input("Entrez 1 pour pile, 2 pour face: "))

if nb == 1:
    print("Pile")
elif nb == 2:
    print("Face")
else:
    print("Invalide")

# Avec le match:

match nb:
    case 1:
        print("Pile")
    case 2:
        print("Face")
    case _:
        print("Invalide")
```

Tous les `case` sont des cas possibles de la variable donné au `match`, le cas `_` est l'équivalent du `else`.

Exemple plus complexe:

```py
nb: int = int(input("Entrez le résultat du lancé du dé: "))

if nb == 1 or nb == 2:
    print("Échec")
elif nb == 3:
    print("Bof")
elif nb == 4 or nb == 5:
    print("Ok")
elif nb == 6:
    print("Parfait")
else:
    print("Invalide")

# Avec le match:

match nb:
    case 1 | 2:
        print("Échec")
    case 3:
        print("Bof")
    case 4 | 5:
        print("Ok")
    case 6:
        print("Parfait")
    case _:
        print("Invalide")
```

La barre verticale dans ce cas est un `or`.

```py
nb: int = int(input("Entrez le résultat du lancé du dé: "))

if 1 <= nb <= 3:
    print("Échec")
elif 4 <= nb <= 6:
    print("Réussite")
else:
    print("Invalide")

# Avec le match:

match nb:
    case nb if 1 <= nb <= 3:
        print("Échec")
    case nb if 4 <= nb <= 6:
        print("Réussite")
    case _:
        print("Invalide")
```

Ce dernier exemple montre la flexibilité du match, mais aussi qu'il est possible de mal l'utiliser. Dans ce cas le if était bien plus simple.

Le *switch* devient intéressant lorsqu'on a 4 branchements (choix) ou plus. Si vous avez une liste de choix préféfinis, on prends le *switch*, sinon on prend un *if*. Si vous avez des intervalles, prenez un *if*.