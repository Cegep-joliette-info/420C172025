# Cheatsheet Python

## Types

* Simples: int, float, bool et str
* Spécial: None
* Composés: npt.NDArray, list, set, tuple, dict

## Priorité des opérateurs

1. `()`
2. `**`
3. Opérateurs unaires : `+`, `-`, `~`
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `<<`, `>>`
7. `&`
8. `^`
9. `|`
10. `==`, `!=`, `>`, `<`, `>=`, `<=`
11. `not`
12. `and`
13. `or`

## Structures de contrôle

```py
if condition:
    instructions
elif autre_condition:
    autres_instructions
else:
    autres_instructions
```

```py
x = a if condition else b
```

```py
match variable:
    case valeur1:
        instructions
    case valeur2 | valeur3:
        instructions
    case _:
        instructions
```

```py
for i in range(debut, fin, pas):
    instructions
```

```py
for i in collection:
    instructions
```

```py
while condition:
    instructions
```

## Transtypage

```py
i = int("42")
f = float("3.14"
b = bool(1)
s = str(42)
```

## Console

```py
input("Message à afficher à l'utilisateur: ")
print("Message à afficher")
print("Message", sep=' ', end='\n')

print(f"Valeur de la variable: {variable}")
print(f"PI: {pi:.2f}")
```

## Git

```sh
git init
git add .
git commit -m "Message du commit"
git push
git pull
git clone <url-du-repo>
git status
```

## Fonctions intégrées

### Conversion

* `bool(x)`
* `int(x)`
* `float(x)`
* `str(x)`

### Fonctions intégrées

* `type(x)`
* `abs(x)`
* `bin(x)`
* `chr(x)`
* `format(x, f)`
* `hex(x)`
* `max(x, y, ...)`
* `min(x, y, ...)`
* `oct(x)`
* `pow(x, y)`
* `round(x[, ndigits])`
* `ord(x)`

### Fonctions str

* `s.capitalize()`
* `s.upper()`
* `s.lower()`
* `s.casefold()`
* `s.swapcase()`
* `s.title()`
* `s.center(width)`
* `s.ljust(width)`
* `s.rjust(width)`
* `s.expandtabs(tabsize)`
* `s.lstrip()`
* `s.rstrip()`
* `s.strip()`
* `s.removeprefix(prefix)`
* `s.removesuffix(suffix)`
* `s.replace(old, new)`
* `s.count(sub[, start[, end]])`
* `s.endswith(suffix)`
* `s.startswith(prefix)`
* `s.find(sub[, start[, end]])`
* `s.rfind(sub[, start[, end]])`
* `s.isalnum()`
* `s.isalpha()`
* `s.isascii()`
* `s.isdecimal()`
* `s.isdigit()`
* `s.isnumeric()`
* `s.islower()`
* `s.isupper()`
* `s.istitle()`
* `s.isspace()`

### Fonctions mathématiques (module math)

* `math.pi`
* `math.e`
* `math.ceil(x)`
* `math.floor(x)`
* `math.trunc(x)`
* `math.comb(n, k)`
* `math.perm(n, k)`
* `math.copysign(x, y)`
* `math.fabs(x)`
* `math.factorial(x)`
* `math.fmod(x, y)`
* `math.gcd(a, b, ...)`
* `math.lcm(a, b, ...)`
* `math.isclose(a, b)`
* `math.isfinite(x)`
* `math.isinf(x)`
* `math.isnan(x)`
* `math.isqrt(n)`
* `math.exp(x)`
* `math.exp2(x)`
* `math.pow(x, y)`
* `math.sqrt(x)`
* `math.cbrt(x)`
* `math.log(x[, base])`
* `math.log2(x)`
* `math.log10(x)`

## Exceptions

```py
try:
    instructions
except ValueError:
    instructions
except ZeroDivisionError:
    instructions
except FileNotFoundError:
    instructions
except IndexError:
    instructions
else:
    instructions
```

## Fonctions

```py
def nomDeLaFonction(parametre1, parametre2):
    instructions
    return valeur
```

## Numpy

```py
import numpy as np
import numpy.typing as npt

a:  npt.NDArray[np.int_] = np.array([1, 2, 3])
```

Autres fonctions numpy:

* `np.zeros`
* `np.ones`
* `np.full`
* `np.empty`

## Chaînes avancées

```py
chanson.find("give")
"give" in chanson
chanson.split()
'-'.join(mots)
```

## Tests unitaires

```py
import unittest
tc = unittest.TestCase()
tc.assertEqual(valeur1, valeur2)
tc.assertNotEqual(valeur1, valeur2)
tc.assertTrue(condition)
tc.assertFalse(condition)
```

## Liste

```py
lst: list[int]
```

```py
lst = [1, 2, 3]
lst.append(4)
lst.insert(0, 0)
lst.pop(2)
lst.pop()
lst.clear()
```

```py
lst = [1, 2, 3] + [4, 5, 6]
lst = [0] * 3
print(lst[-1])
lst[1:]
lst[:2]
lst[1:4]
lst[::2]
```

```py
lst = [x for x in lst if x > 2 == 0]
lst = [x if x > 2 else 0 for x in lst]
```

## Ensemble

```py
s: set[int]
```

```py
s = set()
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(5)
s.pop()
s.clear()
```

```py
1 in s1
s1.isdisjoint(s2)
s1.issubset(s2)
s1 <= s2
s1 < s2
s1.issuperset(s2)
s1 >= s2
s1 > s2

s1.union(s2)
s1 | s2
s1.intersection(s2)
s1 & s2
s1.difference(s2)
s1 - s2
s1.symmetric_difference(s2)
s1 ^ s2

s1.update(s2)
s1 |= s2
s1.intersection_update(s2)
s1 &= s2
s1.difference_update(s2)
s1 -= s2
s1.symmetric_difference_update(s2)
s1 ^= s2
```

## Tuple

```py
t: tuple[int, str, float]
```

```py
t = (1, 'a', 3.14)
```

## Dictionnaire

```py
d: dict[str, int]
```

```py
d = {'a': 1, 'b': 2}
d['a'] = 3
d.get('a', 0)
del d['b']
d.pop('a')
d.pop('b', 0)
d.popitem()
d.clear()
```

## Lire et écrire des fichiers

```py
with open("fichier.txt", "r") as f:
    contenu = f.read()
with open("fichier.txt", "w") as f:
    f.write("Bonjour le monde!")
with open("fichier.txt", "a") as f:
    f.write("\nAjout de texte.")
```

## Classes

```py
from pathlib import Path
txt = Path("fichier.txt").read_text()
Path("fichier.txt").write_text("Bonjour le monde!")

p: Path = Path("dossier")
p.exists()
```
# Types

 * Simples: int, float, bool et str
 * Spécial: None
 * Composés: npt.NDArray, list, set, tuple, dict

# Priorité des opérateurs

 1. `()`
 2. `**`
 3. Opérateurs unaires : `+`, `-`, `~`
 4. `*`, `/`, `//`, `%`
 5. `+`, `-`
 6. '<<`, `>>`
 7. `&`
 8. `^`
 9. `|`
 10. `==`, `!=`, `>`, `<`, `>=`, `<=`
 11. `not`
 12. `and`
 13. `or`

# Structures de contrôle

```py
if condition:
    instructions
elif autre_condition:
    autres_instructions
else:
    autres_instructions
```

```py
x = a if condition else b
```

```py
match variable:
    case valeur1:
        instructions
    case valeur2 | valeur3:
        instructions
    case _:
        instructions
```

```py
for i in range(debut, fin, pas):
    instructions
```

```py
for i in collection:
    instructions
```

```py
while condition:
    instructions
```

# Transtypage

```py
i = int("42")
f = float("3.14"
b = bool(1)
s = str(42)
```

# Console

```py
input("Message à afficher à l'utilisateur: ")
print("Message à afficher")
print("Message", sep=' ', end='\n')

print(f"Valeur de la variable: {variable}")
print(f"PI: {pi:.2f}")
```

# Git

```sh
git init
git add .
git commit -m "Message du commit"
git push
git pull
git clone <url-du-repo>
git status
```

# Fonctions intégrées

# Fonctions intégrées (*built-in functions*)

## Conversion

* `bool(x)`
* `int(x)`
* `float(x)`
* `str(x)`

## Fonctions intégrées

* `type(x)`
* `abs(x)`
* `bin(x)`
* `chr(x)`
* `format(x, f)`
* `hex(x)`
* `max(x, y, ...)`
* `min(x, y, ...)`
* `oct(x)`
* `pow(x, y)`
* `round(x[, ndigits])`
* `ord(x)`

## Fonctions str

* `s.capitalize()`
* `s.upper()`
* `s.lower()`
* `s.casefold()`
* `s.swapcase()`
* `s.title()`
* `s.center(width)`
* `s.ljust(width)`
* `s.rjust(width)`
* `s.expandtabs(tabsize)`
* `s.lstrip()`
* `s.rstrip()`
* `s.strip()`
* `s.removeprefix(prefix)`
* `s.removesuffix(suffix)`
* `s.replace(old, new)`
* `s.count(sub[, start[, end]])`
* `s.endswith(suffix)`
* `s.startswith(prefix)`
* `s.find(sub[, start[, end]])`
* `s.rfind(sub[, start[, end]])`
* `s.isalnum()`
* `s.isalpha()`
* `s.isascii()`
* `s.isdecimal()`
* `s.isdigit()`
* `s.isnumeric()`
* `s.islower()`
* `s.isupper()`
* `s.istitle()`
* `s.isspace()`

## Fonctions mathématiques (module math)

* `math.pi`
* `math.e`
* `math.ceil(x)`
* `math.floor(x)`
* `math.trunc(x)`
* `math.comb(n, k)`
* `math.perm(n, k)`
* `math.copysign(x, y)`
* `math.fabs(x)`
* `math.factorial(x)`
* `math.fmod(x, y)`
* `math.gcd(a, b, ...)`
* `math.lcm(a, b, ...)`
* `math.isclose(a, b)`
* `math.isfinite(x)`
* `math.isinf(x)`
* `math.isnan(x)`
* `math.isqrt(n)`
* `math.exp(x)`
* `math.exp2(x)`
* `math.pow(x, y)`
* `math.sqrt(x)`
* `math.cbrt(x)`
* `math.log(x[, base])`
* `math.log2(x)`
* `math.log10(x)`

# Exceptions

```py
try:
    instructions
except ValueError:
    instructions
except ZeroDivisionError:
    instructions
except FileNotFoundError:
    instructions
except IndexError:
    instructions
else:
    instructions
```

# Fonctions

```py
def nomDeLaFonction(parametre1, parametre2):
    instructions
    return valeur
```

# Numpy

```py
import numpy as np
import numpy.typing as npt

a:  npt.NDArray[np.int_] = np.array([1, 2, 3])
```

Autres fonctions numpy:

* `np.zeros`
* `np.ones`
* `np.full`
* `np.empty`

# Chaînes avancées

```py
chanson.find("give")
"give" in chanson
chanson.split()
'-'.join(mots)
```

# Tests unitaires

```py
import unittest
tc = unittest.TestCase()
tc.assertEqual(valeur1, valeur2)
tc.assertNotEqual(valeur1, valeur2)
tc.assertTrue(condition)
tc.assertFalse(condition)
```

# Liste

```py
lst: list[int]
```

```py
lst = []
lst = [1, 2, 3]
lst.append(4)
lst.insert(0, 0)
lst.pop(2)
lst.pop()
lst.clear()
```

```py
lst = [1, 2, 3] + [4, 5, 6]
lst = [0] * 3
print(lst[-1])
lst[1:]
lst[:2]
lst[1:4]
lst[::2]
```

```py
lst = [x for x in lst if x > 2 == 0]
lst = [x if x > 2 else 0 for x in lst]
```

# Ensemble

```py
s: set[int]
```

```py
s = set()
s = {1, 2, 3}
s.add(4)
s.remove(2)
s.discard(5)
s.pop()
s.clear()
```

```py
1 in s1
s1.isdisjoint(s2)
s1.issubset(s2)
s1 <= s2
s1 < s2
s1.issuperset(s2)
s1 >= s2
s1 > s2

s1.union(s2)
s1 | s2
s1.intersection(s2)
s1 & s2
s1.difference(s2)
s1 - s2
s1.symmetric_difference(s2)
s1 ^ s2

s1.update(s2)
s1 |= s2
s1.intersection_update(s2)
s1 &= s2
s1.difference_update(s2)
s1 -= s2
s1.symmetric_difference_update(s2)
s1 ^= s2
```

# Tuple

```py
t: tuple[int, str, float]
```

```py
t = ()
t = (1, 'a', 3.14)
```

## Dictionnaire

```py
d: dict[str, int]
```

```py
d = {}
d = {'a': 1, 'b': 2}
d['a'] = 3
d.get('a', 0)
del d['b']
d.pop('a')
d.pop('b', 0)
d.popitem()
d.clear()
```

## Lire et écrire des fichiers

### Avec with open

```py
with open("fichier.txt", "r") as f:
    contenu = f.read()
with open("fichier.txt", "w") as f:
    f.write("Bonjour le monde!")
with open("fichier.txt", "a") as f:
    f.write("\nAjout de texte.")
```

### Avec pathlib

```py
from pathlib import Path
txt = Path("fichier.txt").read_text()
Path("fichier.txt").write_text("Bonjour le monde!")

p: Path = Path("dossier")
p.exists()
```