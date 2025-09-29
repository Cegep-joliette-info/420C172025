# Fonction

## Présentation

Une fonction (méthode) permet de créer des algorithmes que l'on appellera au besoin. Ça permet de réduire les lignes de code du main et ça permet aussi de réutiliser du code.

Une fonction:

 * Bloc d'instructions chargé d'accomplir une tâche spécifique.
 * Peut recevoir des arguments (des paramètres). Toute donnée nécessaire à la réalisation de la fonction doit être reçue en argument.
 * Peut retourner une valeur ou non (None).
 * Ne fait pas de lecture d'entrée au clavier (input) ni d'affichage à la console (print) à moins que ce soit dans l'objectif de la fonction.
 * Identificateur de la fonction utilise la même syntaxe qu'une variable.

## Syntaxe

```py
def nomFonction(arg1: type, arg2: type, ...) -> type:
    # corps de la fonction ici
```

 * `-> type` est le type retourné par la fonction.
 * (arg1: type, ...) sont les arguments de la méthode.

## Vocabulaire

On appelle signature l'entête d'une fonction.

On appelle le corps le code écrit à l'intérieur d'une fonction.

On dit invoquer une fonction pour faire appel à une fonction.

## Arguments et valeur de retour

Méthode qui ne retourne rien:

```py
def maMethode1(arg1: int, arg2: float) -> None:
```

Méthode qui retourne une valeur:

```py
def maMethode2(arg1: str, arg2: bool, arg3: int) -> int:
```

## Exemple

```py

def sommeInt(nombre1: int, nombre2: int) -> int:
    """Additionne deux entiers

    Args:
        nombre1: Premier entier à additionner
        nombre2: Deuxième entier à additionner

    Returns:
        La somme des deux entiers reçus
    """

    somme: int

    somme = nombre1 + nombre2

    return somme


nb1: int
nb2: int
somme: int

nb1 = int(input())
nb2 = int(input())

somme = sommeInt(nb1, nb2)

print("nb1 + nb2:", somme)
```

Le commentaire (qui est juste une chaîne de caractère) de fonction (docstring) suis la norme de Google: https://google.github.io/styleguide/pyguide.html

Notez qu'après une fonction il faut mettre 2 lignes vides.