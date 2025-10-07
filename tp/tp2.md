# TP2

Travail individuel, à remettre avant 8h00 le lundi 20 octobre.

Attention, bien que vous pouvez choisir le thème du jeu, vous devez respecter les règles du cégep (pas de violence, intidimation ou de propos à caractère sexuel).

Une démo est disponible [en gif](../imgs/tps/TP2.gif) et [en mp4](../imgs/tps/tp2.mp4).

## Objectif

Un jeu de bonhomme *sus*pendu qui consiste à trouver un mot choisi aléatoirement parmis une liste, en essayant une lettre à la fois. À la fin de chaque partie, des statistiques sont affichés et l'utilisateur peut repartir une nouvelle partie sans fermer le programme.

## Liste de mots

Votre jeux doit se baser sur une catégorie (programmation, zelda, thés, poulet, etc.). Vous devez avoir une liste de 20 mots liés à votre catégorie, les mots doivent être en français, en minuscule sans accent (écrire "reseau" au lieu de "réseau"). Au début de chaque partie vous devez choisir un mot au hasard.

## Tentative

À chaque tentative vous devez afficher:

Le dessin du bonhomme suspendu (ou un équivalent). Voici l'ascci art que j'ai pris pour mon [exemple](tp2_ascci_art.md). Au début on voit une base pour le dessin, à chaque erreur on ajoute un élément au dessin. Lorsque le dessin est complet (nombre d'erreur max atteints), la partie est terminée (défaite).

Ensuite pour chaque lettre du mot à deviner, on met un trait de soulignement séparé par une espace. Chaque lettre trouvé doit être affichée au lieu du trait de soulignement.

Ensuite, sauf pour la première tentative d'une partie, on affiche toutes les lettres essayés par le joueur.

Finalement, on demande à l'utilisateur de saisir une lettre.

Exemple après 2 tentatives (1 réussite et 1 erreur):

```
 _______
|/      |
|       |
|       O
|       
|       
|
_ a _ a _ _ _ _ _ _ 
Lettres essayés: a e 
-> Entrez une lettre: 
```

## Fin de partie

À la fin de la partie, on affiche à l'utilisateur le nombre de partie gagnés, le nombre de partie perdus et la moyenne de gain pour toutes les parties (moyenne avec 2 décimales).

Ensuite on demande à l'utilisateur s'il veut recommencer une partie. Si oui on recommence le jeu avec un nouveau mot, sinon on ferme le jeu.

## Validation

Aucune saisie utilisateur ne doit provoquer d'exception.

Vous devez accepter les minuscules et les majuscules.

Au courant d'une partie, si j'entre plusieurs caractère, seul le premier est pris en compte. Les caractères qui ne sont pas des lettres ($, *, 9, é, œ, etc.) ne compte pas comme une tentative. Répéter une lettre compte pour une erreur par contre!

Pour recommencer la partie, l'utilisateur peut répondre 'o', 'O', 'n' ou 'N'. En cas de choix non valide, on repose la question.

## Rétroaction

Le joueur doit savoir ce qui est arrivé, en cas d'une bonne lettre il faut afficher un message en bleu, en cas d'erreur il faut afficher un message en rouge. Pour changer la couleur:

```py
# Constantes déclarées globales:
ANSI_RESET: str = "\u001B[0m"
ANSI_RED: str = "\u001B[31m"
ANSI_BLUE: str = "\u001B[34m"
# Afficher en rouge:
print(ANSI_RED + "Travail pratique 1")
# Enlever la couleur
print(ANSI_RESET + "Travail pratique 1")
```

## Fonctions

Vous devez avoir les fonctions suivantes, vous pouvez traduire les noms si votre code est en anglais. Toutes les fonctions doivent être utilisés dans votre résultat final. Certaines fonctions peuvent être utilisés par d'autres fonctions au lieu d'être utilisé dans le code principal.

### `motAleatoire`

Retourne un mot choisis aléatoirement parmis un tableau de chaîne reçu

Test:
Je lui donne `['a', 'b', 'c']`, il me donne `'a'`.
Faites plusieurs tests avec les mêmes valeurs, il devrait vous donner les 3 possibilités.

### `validerRejouer`

Demande au joueur s'il veut jouer une nouvelle partie, retourne vrai ou faux.

Test:
Essayez toutes les possibilités (o, N, z, etc.)

### `copieTableau`

Copie un tableau vers un autre tableau. Les 2 sont reçu en paramètres, attention on ne sais pas lequel est le plus petit. Par exemple copier un tableau de 3 éléments vers un tableau de 4 éléments ne copie que 3 éléments peut importe l'ordre.

Tests:
 * Avec `['a', 'A']` et `['', '']`, le 2e tableau devient `['a', 'A']`
 * Avec `['a', 'A', 'z']` et `['', '']`, le 2e tableau devient `['a', 'A']`
 * Avec `['a', 'A']` et `['', '', '']`, le 2e tableau devient `['a', 'A', '']`

### `ajouterElement`

Ajoute un élément (une case et une valeur) à un tableau.

Tests:
 * Avec `[]` et `'a'`, ça me donne `['a']`
 * Avec `['a', 'A', 'z']` et `o`, ça me donne `['a', 'A', 'z', 'o']`

### `dessiner`

Affiche le bonhomme suspendu selon le nombre d'erreurs reçu

Tests: Essayez tous les nombres possibles, incluant des nombres trop gros

### `estDansTableau`

Retourne un vrai ou faux qui indque si la lettre reçu se trouve dans le tableau reçu. Vous ne pouvez pas utiliser `in` ou un équivalent dans cette fonction.

Tests:
 * Avec `'a'` et `[]`, donne `False`
 * Avec `'a'` et `['a', 'b', 'c']`, donne `True`
 * Avec `'z'` et `['a', 'b', 'c']`, donne `False`

### `creerEtRemplir`

Crée un tableau de la longeur donnée puis le remplis entièrement avec le caractère donnée

Tests:
 * Avec `5` et `''`, donne `['', '', '', '', '']`
 * Avec `3` et `'_'`, donne `['_', '_', '_']`
 * Avec `4` et `'nah'`, donne `['nah', 'nah', 'nah', 'nah']`

### `afficherTableau`

Affiche le tableau de caractère reçu

Tests:
 * Avec `['_', '_', '_']`, affiche `_ _ _`
 * Avec `['a', 'b', 'c']`, affiche `a b c`

### `remplacer`

Reçoit une chaîne, un tableau de caractère et une lettre. Le tableau et la chaîne doivent être de la même longeur. Pour chaque instance de la lettre qu'on trouve dans le mot, remplacer la case correspondante du tableau avec la lettre.

Tests:

 * Avec `"allo"`, `['_', '_', '_', '_']` et `'a'`. Le tableau deviendra `['a', '_', '_', '_']`
 * Avec `"allo"`, `['a', '_', '_', '_']` et `'l'`. Le tableau deviendra `['a', 'l', 'l', '_']`

## Spécifications

 * Toute instruction non-vue en classe (break, continue, plus de 1 return dans une fonction, etc.) est retiré de votre code lors de la correction
 * Aucune variable globale (déclarés au-dessus des fonctions) sauf les couleurs sont acceptés
 * Toutes les fonctions doivent être commentés avec les docStrings
 * Vous devez respecter les normes de programmation du département (casse, aération, nommage, indentation, position des accolades, code mort, etc.).
 * Utilisez les bonnes instructions selon le cas (foreach, for ou while. if ou match. etc.)
 * Chaque action de l'utilisateur doit avoir une rétroaction claire
 * Utilisez les couleurs (rouge et bleu) au bon moment, on se sert des couleurs pour mettre l'emphase sur un message important

## Remise 

 * Remise sur le répertoire Git suivant: https://classroom.github.com/a/0TyNskxr
 * Aucune autre méthode de remise ne sera accepté, les fichiers compressés seront refusé, votre répertoire Git doit respecter les normes vues en classe. Votre répertoire Git doit seulement contenir les fichiers du TP2 (1 seule version). En cas de non-respect de cette règle vous devrez corriger la situation, la pénalité de retard s'appliquera.
 * En cas de retard avertissez moi, sinon je télécharge les projets au moment de la remise
 * Assurez-vous de remettre le bon fichier (avec la bonne version)

## Correction

 * La grille exhaustive est disponible sur Moodle
 * La grille remplis sera sur Moodle

## Annexe - facultatif

Pour faire comme ma démo et vider la console à chaque étape, ajoutez les lignes suivantes à votre fichier:

```py
# Ajoutez cette ligne en haut du fichier, dans vos imports
import os
```

```py
# Ajoutez cette ligne après les imports mais avant vos fonctions
cls = lambda: os.system('cls' if os.name=='nt' else 'clear')
```

```py
# Appelez la fonction au moment où vous voulez effacer la console
cls()
```