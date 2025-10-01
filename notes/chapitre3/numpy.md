# Tableaux avec Numpy

Les tableaux n'existent pas vraiment dans Python, nous allons donc utiliser NumPy.

NumPy (Numerical Python) est un logiciel libre, largement utilisé. Vous pouvez l'utiliser autant en programmation standard qu'en physique ou qu'en AI.

Les tableaux NumPy sont plus rapides que les listes Python (que nous allons voir plus tard), mais un peu plus complexe à manipuler.

Pourquoi plus rapide? Un tableau a un nombre prédéfinie d'éléments, on assigne donc la bonne taille en mémoire lors de l'utilisation. La liste a une taille variable d'éléments, les éléments ne sont donc pas conjoints ce qui ralentis le processus.

## Installation

En ligne de commande, exécutez: `pip install numpy`.

En haut de votre fichier, il faudra importer NumPy:

```py
import numpy as np
```

Le `as` sert a renommer une librairie, dans ce cas nous devront écrire `np` pour utiliser NumPy, c'est la norme avec NumPy.

## Utilisation

Un tableau numpy peut contenir des éléments de plusieurs types différents, mais nous allons l'utiliser comme un tableau "classique", donc tous les éléments du tableau doivent être du même type.

Les indices du tableau sont de type int le premier indice est à 0. Lorsque le tableau est créé sa taille est fixée et elle ne peut plus varier.

```py
a:  np.ndarray[int] = np.array([1, 2, 3])
print(a[0])
```

Le code précédent va créer un tableau de int de 1 dimension de taille 3. Ensuite on affiche le contenu de la première case, soit zéro.

La taille d'un tableau est immuable, mais nous pouvons modifier le contenu:

```py
a: np.ndarray[int] = np.array([1, 2, 3])
a[1] += 10
print(a[1]) # Affiche 12
```

Pour connaitre la taille d'un tableau, utilisez la fonction `len`:

```py
a: np.ndarray[int] = np.array([1, 2, 3])
print(len(a)) # Affiche 3
```

Si vous ne connaissez pas le contenu au moment de la création du tableau, vous pouvez quand même en créer un avec une des fonctions suivantes:

```py
a: np.ndarray[int] = np.empty(10, int) # Crée un tableau de type int de 10 cases, les valeurs sont aléatoires
a: np.ndarray[int] = np.zeros(10, int) # Crée un tableau de type int de 10 cases, tous à zéro
a: np.ndarray[int] = np.full(10, 42, int) # Crée un tableau de type int de 10 cases, tous à 42
```

On peut utiliser tous les types Python en 2e arguements. Si omis, float est utilisé.

Notez que Numpy supporte plusieurs autres types plus précis, par exemple le `np.uint8` qui est un entier non signé sur 1 octet.

## Parcours d'un tableau

La méthode usuelle pour parcourir un tableau est de parcourir les indices du tableau. C'est la méthode utilisé dans la majorité des langages.

```py
a: np.ndarray[int] = np.array([1, 2, 3])
for i in range(len(a)):
    a[i] *= 2

# Le tableau vaut maintenant [2, 4, 6]
```

Vous pouvez aussi faire ce qu'on appel un "foreach" dans d'autres langages (pas toujours disponible). Dans ce cas par contre vous ne pouvez pas modifier le contenu du tableau:

```py
a: np.ndarray[int] = np.array([1, 2, 3])
somme: int = 0
for i in a:
    somme += 1
print(somme) # Affiche 6
```