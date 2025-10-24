# Chapitre 3 - Atelier 4 - Modules

Pour tous les numéros, votre module Python principal (celui que vous executez) devrait contenir seulement des imports, des appels de fonctions et des prints. Par exemple:

```py
import mathematique
print(mathematique.addition(2, 4))
```

Faites plusieurs tests (avec des valeurs différentes et les valeurs limites) pour chaque fonction.

## Numéro 1

Complétez le module mathematique avec les fonctions suivantes qui prennent 2 nombres en paramètres et qui retournent un nombre:

 * `addition`
 * `soustraction`
 * `division`, la fonction doit retourner zéro (0) s'il y a une division par zéro
 * `multiplication`


## Numéro 2

Créez un module math_tableau_entier avec les fonctions suivantes. Toutes les fonctions prennent en paramètre un tableau d'entier numpy.
Attention, vos fonctions doivent fonctionner avec un tableau vide (taille zéro).

 * `somme`: donne la somme entre tous les nombres
 * `moyenne`: fait la moyenne (float) du tableau, utilisez la fonction précédente


## Numéro 3

Créer un module chaines avec les fonctions suivantes. Pour toutes ces fonctions, retournez une chaîne vide s'il n'y a pas de réponse.

 * `plusLong`: parmis un tableau de chaînes reçu en paramètre, retourne le plus long
 * `deLongueur`: parmis un tableau de chaînes et une longueur reçus en paramètres, retourne le premier mot de la longueur donné
 * `plusDeLettre`: parmis un tableau de chaînes et une lettre reçus en paramètres, retourne le mot qui contient le plus souvent la lettre reçu