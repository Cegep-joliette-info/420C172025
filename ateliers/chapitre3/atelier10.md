# Chapitre 3 - Atelier 10 - Lecture/écriture d'un fichier

Nous allons faire un outil pour gérer la liste de mots pour votre TP1. Le fichier (mots.txt), contient un mot par ligne. À l'ouverture du programme:

 * Si le fichier n'existe pas, on le crée avec des mots prédéfinis
 * Si le fichier existe, on charge la liste en mémoire

Ensuite on offre 3 choix à l'utilisateur, après chaque action on sauvegarde le fichier:

 1. Ajouter un mot
 2. Retirer un mot
 3. Quitter

Pour l'ajout, affichez un erreur si le mot existe déjà. Normalisez aussi le mot (tout en minuscule). Faites seulement un ajout au fichier.

Pour le retrait, affiche un erreur si le mot n'existe pas. Réécrivez le fichier au complet.

Exemple de résultat:

```
1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 1
Entrez un mot: reseau
Le mot existe déjà

1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 1
Entrez un mot: asdf

1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 2
Entrez un mot: qwer
Le mot n'existe pas

1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 2
Entrez un mot: asdf

1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 4
Choix invalide

1 - Ajouter un mot
2 - Retirer un mot
3 - Quitter
Votre choix: 3
```