# TP1 - Jeu du nombre mystère

Travail formatif (ne compte pas), mais sera corrigé comme un vrai projet.

Travail indiviuel, à remettre avant le 22 septembre 8h00.

## Objectif

Un jeu de nombre mystère consiste à trouver un nombre sélectionné au hasard, selon un nombre d’essais limités.

## Menu

Au début du jeu, offrez les difficultés suivantes à l'utilisateurs:

 * Facile: Nombre entre 1 et 19, 10 essais
 * Normal: Nombre entre 1 et 49, 5 essais
 * Difficile: Nombre entre 1 et 99, 5 essais
 * Impossible: Nombre entre 1 et 999, 1 essai

En cas de choix invalide, affichez un message d'erreur puis reposez la question.

Défi: Ajoutez un 5e élément dans le menu: "Personnalisé", le joueur devra choisir le nombre maximal et le nombre d'essais.

## Indications

Le nombre d'essais et les limites du nombre mystère doivent être affichés de cette façon (attention aux espaces, l'apparence doit être soignée):

```
(1/5) 0 < ? < 100 :
```

Le nombre entrée doit être un entier. Si l'utilisateur n'entre pas un nombre, afficher un message d'erreur puis réafficher l'essaie courant sans pénalité. Si l'utilisateur ne respecte pas les bornes, afficher un message d'erreur et enlever un essaie.

## Suivi

Suite à une tentative, les informations doivent êtres ajustées :

```
(1/5) 0 < ? < 100 : 50
(2/5) 50 < ? < 100 : 75
(3/5) 50 < ? < 75 : 
```

## Résultats 

 * Féliciter l'utilisateur dans le cas d'une tentative exacte.
 * Indiquer quel était le nombre mystère si le nombre de tentatives est épuisé.

## Normes

 * Les commentaires et les messages en console doivent être en français, le code peut être en anglais ou français, tant que vous êtes constant. Pénalité de 10% pour les fautes de français (vous perdez le 10% si tout est en anglais).
 * Ne pas avoir d'inclusion inutile ou de code mort
 * Les identificateurs doivent êtres significatifs et doivent respecter les normes de casses
 * Le code doit être bien aéré (pas trop) et bien indenté
 * Pas de code inutile (incluant pléonasmes et redondances)

## Remarque 

 * Ce travail est à réaliser seul. 
 * Le plagiat est non toléré et entraîne systématiquement la note de zéro et une note au dossier.
 * Interdiction d’utiliser les instructions break, continue ou return (ou équivalent) dans une boucle/condition.
 * Toute instruction non-vue en classe sera retirée avant la correction
 * Si l'utilisateur entre une donnée invalide, affichez un message d'erreur clair et redemandez la "question".

## Démo

[Vidéo de ma solution](../imgs/tps/tp1.mp4)

## Remise 

 * Remise sur le répertoire Git suivant: https://classroom.github.com/a/BnIhXscQ
 * Aucune autre méthode de remise ne sera accepté, les fichiers compressés seront refusé, votre répertoire Git doit respecter les normes vues en classe. Votre répertoire Git doit seulement contenir les fichiers du TP0 (1 seule version). En cas de non-respect de cette règle vous devrez corriger la situation, la pénalité de retard s'appliquera.
 * En cas de retard avertissez moi, sinon je télécharge les projets au moment de la remise

## Correction

 * La grille exhaustive est disponible sur Moodle
 * La grille remplis sera sur Moodle

 * Gestion du menu
 * Gestion des bornes
 * Gestion du nombre d'essaie
 * Fin de partie (victoire/défaite)
 * Gestion des entrées (input)
 * Respect des normes
 * Bon choix d'instruction (if vs match, for vs while, if vs exceptions, etc.)

## Annexe

Couleurs dans le terminal:

```py
# \033[91m  Affiche en Rouge
# \033[92m  Affiche en Vert
# \033[0m   Affiche en Blanc/Noir (reset la couleur)
# La couleur (vert ou rouge) reste pour tous les prints

print('\033[91m' + 'ROUGE' + '\033[0m') # Affiche ROUGE en rouge puis remet en default pour la suite
print('\033[92m' + 'VERT' + '\033[0m')  # Affiche VERT en vert puis remet en default pour la suite
```

Pour le nombre au hasard:

```py
import random # importe la librairie qui fait des aléatoires

# mettre les constantes ici

# mettre les variables ici

# mettre le reste du code ici

random.randint(1, 100) # Donne un nombre aléatoire entre 1 et 100 inclusivement
```
