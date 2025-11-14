# Dictionnaire

Un dictionnaire est une structure de données comme la liste. Une des grande différence est que le dictionnaire, au lieu d'avoir des indices numériques, a des indices de n'importe quel type simple (int, str, float, bool, tuple), souvent des str. Pourquoi les tuples sont inclus dans les indices? Car ils sont immuables.

Pour créer un dictionnaire:

```py
a: dict[str, int] = {'a': 1, 'b': 2}
b: dict[str, int] = dict('a'=1, 'b'=2)
```

Remarquez que pour typer, je donne le type des clés et le type des valeurs. Notez que le mot-clé `in` consule les clés, pas les valeurs.

```py
dictionnaire: dict[str, int] = {'a': 1, 'b': 2}
print(1 in dictionnaire)   # donne False
print('a' in dictionnaire) # donne True

for i in dictionnaire:
    print(i)               # donne 'a' et 'b'
    print(dictionnaire[i]) # donne 1 et 2
```

Les commandes des dictionnaires:

```py
d: dict[str, int] = {'a': 1, 'b': 2}
len(d) # Donne le nombre de clés dans le dictionnaire

d['a']        # Donne 1, plante si la clé n'existe pas
d.get('a', -1) # Donne 1, donne -1 si la clé n'existe pas

d['a'] = 4 # Modifie la valeur de 'a', ajoute 'a' si elle n'existe pas

del d['a'] # Retire 'a' du dictionnaire, plante si n'existe pas
d.pop('a') # Idem, mais donne la valeur en réponse
d.pop('a', -1) # Retire 'a' et donne la valeur en réponse ou -1 si n'existe pas
d.popitem() # Retire le dernier élément ajouté
d.clear()   # Vide le dictionnaire
```

Pour les dictionnaires, une exception sera faite sur "l'unicité des types dans une structure de données". Les clés doivent tous êtres de la même valeur, mais les valeurs pourraient en avoir plusieurs. Pour typer, il faut utiliser le `|`:

```py
# La clé est une string
# La valeur peut être une string ou un int
d: {str: str|int}
```

## Nommer les types

Comme les types peuvent devenir complexes, vous pouvez nommer les types. Notez que nos types vont débuter par une majuscule! Voici quelques exemples:

```py
from typing import NewType

Point = NewType('Point', tuple[int, int])
pt1: Point = (4, 5)

MonDict = NewType('MonDict', dict[str, str|int])
d1: MonDict = {}

ListeDeDictAvecTuple = NewType('ListeDeDictAvecTuple', list[dict[tuple[int, int], str|int]])
# Ou en plusieurs étapes, l'ordre est important:
DuoInt = NewType('DuoInt', tuple[int, int])
DictAvecTuple = NewType('DictAvecTuple', dict[DuoInt, str|int])
ListeDeDictAvecTuple2 = NewType('ListeDeDictAvecTuple2', list[DictAvecTuple])
```

Le dernier exemple peut devenir complexe dans le code, n'hésitez pas à vous faire des variables temporaries:

```py
liste: list[dict[tuple[int, int]: str|int]] = [{(1, 2): 5}]
dictionnaire = liste[0] # Contient {(1, 2): 5}
valeur = dictionnaire[(1, 2)] # Contient 5
```

Avec les dictionnaires il est possible d'utiliser un typage plus précis, votre IDE va vous avertir si vous utilisez une clé qui n'est pas définis dans le type (mais ça ne vous empêche pas de faire n'importe quoi):

```py
from typing import TypedDict

Etudiant: TypedDict = TypedDict('Etudiant', {'nom': str, 'da': int, 'coteR': float})

lorem: Etudiant = Etudiant({})
lorem['prenom'] = 'duuuuuude' # Warning, la clé n'existe pas dans le type
lorem['nom'] = 'ipsum' # OK
```