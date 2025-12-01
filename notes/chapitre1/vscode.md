# Configuration de VSCode pour Python

Dans les extensions, installez l'extension Python officielle de Microsoft:
https://marketplace.visualstudio.com/items?itemName=ms-python.python

Ensuite, ouvrez la palette de commande (Ctrl+Shift+P), et cherchez "Python: Select Interpreter", puis choisissez l'interpréteur Python que vous avez installé. Dans les labs il faut utiliser le `python.exe`, pas le `python3.13t.exe`.

Dans les paramètres (Ctrl+,) ou File > Preferences > Settings:

 * Cherchez `python.terminal.focusAfterLaunch` et activez cette option. Cela permet de focus le terminal après le lancement d'un script.
 * Cherchez `python.analysis.typeCheckingMode` et mettez `strict`. Cela permet d'avoir une analyse de type plus stricte, ce qui est utile pour apprendre le typage.

## Raccourcis utiles

Raccourcis pour Linux et Windows, pour Mac remplacez `Ctrl` par `Cmd` et `Alt` par `Option`.

### Raccourcis standards

 * `Ctrl+S`: Sauvegarder le fichier courant
 * `Ctrl+Shift+S`: Sauvegarder tous les fichiers
 * `Ctrl+F`: Chercher dans le fichier courant
 * `F2`: Renommer
 * `Ctrl+C`: Copier
 * `Ctrl+X`: Couper
 * `Ctrl+V`: Coller

### Raccourcis VSCode pour Python

 * Sélectionner un bloc puis `Tab` pour indenter
 * Sélectionner un bloc puis `Shift+Tab` pour désindenter
 * Accepter une suggestion d'auto-complétion: `Tab` ou `Enter`
 * Sélectionner un bloc puis `Ctrl+É` pour commenter/décommenter
 * `Ctrl+Shift+K`: Supprimer la ligne courante
 * `Alt+Flèche Haut/Bas`: Déplacer la ligne courante vers le haut ou le bas
 * `Ctrl+Espace`: Afficher les suggestions d'auto-complétion
 * `Ctrl+F5`: Lancer le script Python courant dans le terminal intégré
 * `F5`: Lancer le débogueur sur le script Python courant
 * `Ctrl+Shift+F`: Rechercher dans tous les fichiers