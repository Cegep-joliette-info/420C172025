# Fonctions intégrées (*built-in functions*)

Les fonctions intégrées sont des fonctions qui existent déjà dans le langage Python.

Les fonctions [input et print](console.md) sont des exemples de fonctions intégrées.

## Conversion

 * `bool(x)` -> Convertis x en booléen
 * `int(x)` -> Convertis x en int
 * `float(x)` -> Convertis x en float
 * `str(x)` -> Convertis x en string

Le tableau suivant montre des exemples de conversions possibles:

| valeur de x | bool(x) | int(x) | float(x) | str(x)    |
|-------------|---------|--------|----------|-----------|
| True        | True    | 1      | 1.0      | "True"    |
| False       | False   | 0      | 0.0      | "False"   |
| 42          | True    | 42     | 42.0     | "42"      |
| 42.9        | True    | 42     | 42.9     | "42.9"    |
| -42.9       | True    | -42    | -42.9    | "-42.9"   |
| "False"     | True    | Erreur | Erreur   | "False"   |
| "0"         | True    | 0      | 0.0      | "0"       |
| "42.5"      | True    | Erreur | 42.5     | "42.5"    |
| "Bonjour"   | True    | Erreur | Erreur   | "Bonjour" |
| ""          | False   | Erreur | Erreur   | ""        |

## Fonctions intégrées

La fonction suivante est valide pour tous les types:

 * `type(x)` -> Donne le type de la variable x

Les fonctions suivantes sont bonnes pour les int:

 * `abs(x)` -> Donne la valeur absolue de x
 * `bin(x)` -> Convertis le nombre en binaire puis le met dans une chaîne, préfixé de "0b"
 * `chr(x)` -> Donne le caractère de la table ascii associé à x
 * `format(x, f)` -> Convertis en string selon le format f, similaire à `f"{x:f}"`
 * `hex(x)` -> Convertis le nombre en hexadécimal puis le met dans une chaîne, préfixé de "0x"
 * `max(x, y, z, ...)` -> Donne le plus grand nombre parmis tous les nombres reçus
 * `min(x, y, x, ...)` -> Idem, mais le plus petit
 * `oct(x)` -> Convertis le nombre en hexadécimal puis le met dans une chaîne, préfixé de "0o"
 * `pow(x, y)` -> Équivalent à `x ** y`
 * `round(x, y)` -> Arrondis le nombre x par le nombre de décimales y. Par exemple `round(3.1415, 2)` donne `3.14`. Si y est omis, le résultat sera un int.

Les fonctions `abs`, `format`, `max`, `min`, `pow` et `round` sont aussi disponibles pour les floats.

La fonction suivante est valide pour les strings:

 * `ord(x)` -> Pour une chaîne d'un seul caractère, donne le code ascii correspondant

Documentation: https://docs.python.org/3/library/functions.html

## Fonctions str

Plusieurs fonctions sont disponibles pour votre chaînes de caractères:

 * `s.capitalize()` -> La première lettre devient majuscule, toutes les autres en minuscule
 * `s.upper()` -> Convertis tous les caractères en majuscule
 * `s.lower()` -> Idem, mais en minuscule
 * `s.casefold()` -> Idem, mais peut convertir des symboles spéciaux (ne change rien en français ou anglais)
 * `s.swapcase()` -> Convertis les majuscule en minuscule et vice-versa
 * `s.title` -> La première lettre de chaque mot devient en majuscule, toutes les autres lettres deviennent en minuscule

 * `s.center(20)` -> Ajoute des espaces jusqu'à ce que la chaîne soit de 20 caractères, les espaces sont ajoutés au début et à la fin pour centrer le texte initial
 * `s.ljust(20)` -> Idem, mais les espaces sont ajoutés à la fin
 * `s.rjust(20)` -> Idem, mais les espaces sont ajoutés au début
 * `s.expandtabs(x)` -> Remplace les `\t` par des espaces afin de respecter des tabulations de taille x
 * `s.lstrip()` -> Retire les caractères d'espacement au début de la chaîne
 * `s.rstrip()` -> Idem, mais à la fin
 * `s.strip()` -> Combinaison de `lstrip` et `rstrip`

 * `s.removeprefix(x)` -> Retire x de la chaîne si elle est présente au début de la chaîne
 * `s.removesuffix(x)` -> Idem mais à la fin
 * `s.replace(old, new)` -> Remplace tous les old par des new dans la chaîne

 * `s.count(x, a, b)` -> Compte le nombre de fois que la chaîne x se trouve dans s. Comme à chercher à la lettre numéro a et termine à la lettre numéro b. Si a et b son omis, cherche dans toute la chaîne.
 * `s.endswith(x)` -> Retourne True si la chaîne s termine par x
 * `s.startswith(x)` -> Retourne True si la chaîne s débute par x
 * `s.find(x)` -> Donne l'indice (le numéro de caractère) où débute la chaîne x dans s. Donne -1 si x n'est pas dans s
 * `s.rfind(x)` -> Idem, mais commence à chercher à la fin

 * `s.isalnum()` -> True si tous les caractères sont alphanumériques
 * `s.isalpha()` -> True si tous les caractères sont des lettres
 * `s.isascii()` -> True si tous les caractères ont une valeur numérique correspondante dans la table ascii
 * `s.isdecimal()` -> True si tous les caractères sont des chiffres
 * `s.isdigit()` -> Idem, mais supporte les caractères spéciaux comme le `²`
 * `s.isnumeric()` -> Idem, mais supporte encore plus de caractères spéciaux comme le `½`
 * `s.islower()` -> True si tous les caractères (au moins un) pouvant être minuscule ou majuscule, sont minuscules
 * `s.isupper()` -> Idem, mais tous doivent être majuscules
 * `s.title()` -> True si tous les mots de la chaîne débutes par une majuscule suivit de minuscules
 * `s.isspace()` -> True si tous les caractères sont des caractères d'espacements (espace, tabulation, saut de ligne, etc.)

Documentation: https://docs.python.org/3/library/stdtypes.html#string-methods

## Fonctions mathématiques

Vous avez accès à plus de fonctions mathématiques en important le module math. Un module est un ensemble de fonction que nous pouvons importer dans notre projet. La première ligne de votre fichier devrait être `import math` pour utiliser les fonctions suivantes.

Notez que tout ce qui est dans le module math débute par `math.` et que votre fichier ne peut pas s'appeler `math.py`.

Le module définis les constantes suivantes:

 * `math.pi` -> Pi (3.141592...) avec 15 décimales
 * `math.e` -> e (2.718281...) avec 15 décimales

 * `math.ceil(x)` -> Donne l'entier le plus petit entier qui est plus grand ou égal au nombre x
 * `math.floor(x)` -> Donne l'entier le plus grand entier qui est plus petit ou égal au nombre x
 * `math.trunc(x)` -> Retire les décimales pour faire un int

 * `math.comb(x, y)` -> Donne le nombre de possibilités lorsque je choisi y éléments parmis un ensemble de x éléments, sans considérer l'ordre
 * `math.perm(x, y)` -> Donne le nombre de possibilités lorsque je choisi y éléments parmis un ensemble de x éléments, l'ordre est important

 * `math.copysign(x, y)` -> Donne x, mais avec le signe (positif ou négatif) de y
 * `math.fabs(x)` -> Comme `abs` mais donne toujours un float, même si x est un int
 * `math.factorial(x)` -> x doit être un int, donne le factoriel de x, si x vaut 5 ça va faire `5 * 4 * 3 * 2 * 1`
 * `math.fmod(x, y)` -> Équivalent à `x % y`, mais plus précis pour les décimales

 * `math.gcd(x, y, ...)` -> Donne le plus grand commun diviseur des int reçus
 * `math.lcm(x, y, ...)` -> Plus petit commun multiple entre plusieurs int

 * `math.isclose(x, y)` -> Donne True si x est identique à y jusqu'à 9 décimales, utile pour les erreurs d'arrondis
 * `math.isfinite(x)` -> Donne False si x vaut inifini ou NaN (Not a Number)
 * `math.isinf(x)` -> Donne True si x vaut infini
 * `math.isnan(x)` -> Donne True si x vaut NaN
 * `math.isqrt(x)` -> Racine carré arrondis à l'entier inférieur

 * `math.exp(x)` -> Plus de précision pour faire `math.e ** x`
 * `math.exp2(x)` -> Équivalent de `2 ** x`
 * `math.pow(x, y)` -> Équivalent à `x ** y`, mais le résultat sera toujours un float
 * `math.sqrt(x)` -> Racine carré de x
 * `math.cbrt(x)` -> Racine cubique de x

 * `math.log(x, y)` -> Log de x à la base y, si y est omis c'est un logarithme naturel (base de `math.e`)
 * `math.log2(x)` -> Log de x à la base 2, plus précis que `math.log(x, 2)`
 * `math.log10(x)` -> Log de x à la base 10, plus précis que `math.log(x, 10)`

Le module `math` inclus plusieurs autres fonctions: trigonométrie (`acos`, `cos`, `sin`, ...), conversion d'angle (`degrees`, `radians`) et hyperboliques (`acosh`, `sinh`, ...).

Documentation: https://docs.python.org/3/library/math.html