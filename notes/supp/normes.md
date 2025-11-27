# Normes de programmation

## Gabarit d'un fichier Python

```py
# Imports

# Constantes de couleurs

# Fonctions
# Pour chaque fonction respecter l'ordre aussi:
    # Constantes
    # Variables
    # Logique
    # Return ou print

# Constantes

# Variables

# Logique
```

## Commentaires

Toutes les fonctions doivent être commentés avec une docstring selon la norme Google, les sections args et returns sont retirés si elles sont vides.

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
```

## Typage

Toutes les variables, constantes, paramètres et types de retour doivent être typés.

Les tableaux numpy doivent être typés avec `numpy.typing`.

Une fonction qui n'a pas de return aura comme type de retour `None`.

## Nommage

Les identificateurs de variables et de fonctions doivent utiliser la notation chameau (lower camel case): `nomDeMaVariable` ou `nomDeMaFonction`.

Les identificateurs de constantes doivent utiliser la notation serpent criant (screaming snake case) `NOM_DE_MA_CONSTANTE`.

Les noms de fichiers doivent utiliser la notation serpent (snake case) `nom_de_mon_fichier.py`.

## Langue

Tout ce qui est affiché en console doit être en français.
Tous les commentaires doivent être en français.

Le code peut être en français ou en anglais, mais votre choix doit être constant (choisissez un ou l'autre pour votre code).