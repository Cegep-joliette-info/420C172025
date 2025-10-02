# Chaînes et tableaux

Les chaînes de caractères sont des tableaux de caractères!
Par contre, le tableau est en lecture seule, je ne peux donc pas changer une seule lettre avec une assignation.

```py
s: str = "asdf"
s[0] = "A" # Ne fonctionne pas, le tableau est en lecture seule
print(s[0]) # Affiche a
for c in s:
    print(c) # Affiche asdf, une lettre à la fois
```

Le mot-clé `in` permet de faire une recherche. Exemple:

```py
chanson: str = "Never gonna give you up"
# Tous les langages font quelque chose de similaire
if chanson.find("give") > -1:
    print("Rick est l'meilleur")

# En Python on peut seulement faire:
if "give" in chanson:
    print("Rick est l'meilleur")

# Ou l'inverse
if "give" not in chanson:
    print("Pas Rick :(")
```

Vous pouvez aussi séparer une chaîne en plusieurs plus petits morceaux avec un `split`. N'oubliez pas de convertir le résultat en tableau numpy!

```py
import numpy as np
import numpy.typing as npt
chanson: str = "Never gonna give you up"
mots: npt.NDArray[np.int_] = np.array(chanson.split())
print(mots) # Tableau de 5 cases: Never, gonna, give, you, up
```

Je peux manipuler le tableau puis mettre le tout dans une chaîne avec:

```py
s: str = '-'.join(mots)
print(s) # Affiche: Never-gonna-give-you-up
```