# Lecture et écriture en console

## Écriture

Vous connaissez déjà la fonction `print` qui permet d'afficher une valeur en console, cette fonction permet plus que juste ça.

Premièrement, vous pouvez afficher plusieurs valeurs sur la même ligne:

```py
a: int = 3
b: str = "ABC"
print(a, b) # Affiche: 3 ABC
```

Par défaut, `print` sépare chaque élément par un espace et termine par un retour à la ligne (un enter). Vous pouvez changer ce comportement avec des paramètres nommés:

```py
print(a, b, sep=' ', end='\n') # Ne fait rien de différent
print(a, b, sep='') # Ne fait plus d'espace entre les éléments
print(a, b, sep=',') # Ajoute une virgule entre chaque élément
print(a, b, end='') # Ne fait plus de retour à la ligne à la fin
```

Vous pouvez aussi utiliser un littéral chaîne (*string literal*) afin de simplifier le print:

```py
print(f'Bonjour {a} et {b}') # Affiche: Bonjour 3 et ABC
```

Un littéral chaîne est une chaîne débutant par f, le contenu entre accolades dans la chaîne seront interprétés par Python.
On peut formatter des nombres facilement avec ce mode. En ajoutant un `:` après le nom de la variable on entre en mode "formatage". Dans l'exemple suivant, les 2 formats débutes par un `.` pour spécifier une précision, le nombre suivant (2 ou 0 dans l'exemple) donne le nombre de décimales à afficher. Finalement, le `f` dit que c'est un `float` normal tandis que le `%` multiplie la valeur par 100 et ajoute le symbole pourcentage.

```py
PI: float = 3.141592653589793238462643383279502884197
taxes: float = 0.05
print(f'{PI:.2f} et {taxes:.0%}') # Affiche: 3.14 et 5%
```

Voici les autres caractères de formattage disponibles (liste non exhaustive):

 * `:<8` Ajoute des espaces à droite de la valeur jusqu'à ce que le texte prenne 8 "espaces" (on aligne la valeur à gauche)
 * `:>8` Idem, mais aligne la valeur à droite
 * `:^8` Idem, mais aligne la valeur au centre
 * `:=8` Place le signe négatif à gauche, la valeur à droite, puis ajoute des espaces entre les 2
 * `:+` Ajoute un symbole `+` pour les nombres positifs et le `-` pour les nombres négatifs
 * `:-` Idem, mais juste pour les négatifs (donc ne sers à rien)
 * `: ` (un espace après le `:`) Idem au `:+`, mais utilise un espace au lieu du `+`
 * `:,` Utilise un espace comme séparateur de miliers
 * `:_` Idem, mais avec un souligné
 * `:b` Formatte le nombre en binaire
 * `:c` Affiche la lettre correspondant au nombre selon le code ASCII
 * `:d` Affiche le nombre en format décimal, donc ne fait rien
 * `:e` Affiche le nombre en format scientifique avec un `e`
 * `:E` Idem mais avec `E`
 * `:f2` Nombre de décimales fixes, 2 décimales dans ce cas
 * `:F2` Idem, mais infini va être `INF` au lieu de `inf`
 * `:g` Similaire au `:e`
 * `:G` Similaire au `:E`
 * `:o` Affiche le nombre en format octal
 * `:x` Affiche le nombre en format hexadécimal
 * `:X` Idem, mais les lettres sont majuscules
 * `:%` Affiche le nombre décimal en pourcentage, donc multiplie le nombre par 100 et ajoute le symbole `%`

On peut aussi utiliser les litéraux pour écrire différement nos chaînes:

```py
"Coucou {} et {}".format("Alice", "Bob")
# Coucou Alice et Bob

"{0} dit coucou {0} et {1}".format("Alice", "Bob")
# Alice dit coucou Alice et Bob

"Coucou %s et %s" % ("Alice", "Bob")
# Coucou Alice et Bob
```

## Lecture

Pour prendre des données saisies par l'utilisateur, on utilise la fonction `input`. On peut poser la question à l'utilisateur directement dans `input` ou préalablement dans un `print`.

```py
nom: str

print('Veuillez écrire votre nom:')
nom = input()

# OU

nom = input('Veuillez écrire votre nom: ')
```

Si vous avez besoin d'un entier, vous pouvez le convertir avec la fonction `int`:

```py
ageEntree: str
age: int

ageEntree = input('Entrez votre âge: ')
age = int(ageEntree)

# OU

age = int(input('Entrez votre âge: '))
```

Attention, si l'utilisateur entre autre chose qu'un entier le programme va planter, on va résoudre ce problème plus tard.