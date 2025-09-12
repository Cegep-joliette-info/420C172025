# Atelier 6 - Tutoriel Git

Suivre les étapes, si vous avez une erreur arrêtez puis demandez à l'enseignant comment continuer.

## Pour les portables

Il faut installer Git sur vos portables, passez cette étape si vous utilisez l'ordinateur du cégep (passez à l'étape Préparation).

### Windows

 1. Installez https://gitforwindows.org/

### MAC

 1. Ouvrez le terminal (Ouvrir le Launchpad puis recherchez Terminal)
 2. Écrire `git` puis enter, si vous l'avez ça affiche une aide, sinon ça affiche une erreur et un popup vous propose de l'installer, dites oui

## Préparation

Ces étapes sont à faire sur chaque ordinateur que vous allez utiliser.

 1. Ouvrez `Git bash`
 2. Entrez la commande `ssh-keygen -t ed25519`
 3. Appuyez sur enter 3 fois afin de passer toutes les questions, ça devrait vous afficher un carré plein de symboles
 4. Entrez la commande `cat .ssh/id_ed25519.pub`, copiez toute la ligne résultante qui débute par `ssh-ed25519` et qui termine par le nom de l'ordinateur (termine par un chiffre sur les ordi du cégep)
 5. Ouvrez le site https://github.com
 6. Créez un compte avec votre adresse du cégep ou votre adresse personnelle. Ou connectez-vous si vous avez déjà un compte
 7. En haut à droite vous avez un symbole qui représente votre compte, cliquez dessus puis sur `Settings`, puis sur `SSH and GPG keys`.
 8. Appuyez sur le bouton vert `New SSH key`, donnez un nom à la clé dans le champ Title (ordi du cégep, mon portable, etc.) puis collez la clé copié à l'étape 4 dans le champ "Key". Enregistrez avec le bouton vert `Add SSH key`.
 9. Retournez à la page d'accueil de Github en cliquant sur le logo de chat en haut à gauche de l'écran

## Nouveau projet

Ces étapes sont à faire pour chaque projet que vous commencez de zéro.

 1. Créez un dossier sur votre ordinateur qui contiendra votre projet. Ce dossier ne doit pas se trouver dans un dossier qui contient déjà git et idéalement, ne doit pas être synchronisé à OneDrive
 2. Ouvrez VSCode, allez dans le menu `File/Open Folder...` et ouvrez le dossier créé à l'étape 1.
 3. Créez un fichier Python dans le dossier, ajoutez seulement un commentaire dans le fichier, sauvegardez le
 4. Ouvrez un terminal dans VSCode (menu `Terminal/New Terminal`)
 5. Dans Github, sur la page d'accueil, créez un nouveau repository git avec le bouton `New` à gauche ou le bouton `+` en haut.
 6. Donnez un nom (par exemple `atelier git`), ignorez toutes les autres options puis cliquez sur `Create repository`
 7. Dans la boite bleu `Quick setup`, vous avez le choix entre `HTTPS` et `SSH`, cliquez sur `SSH`, le lien à droite de ces choix devrait débuter par un `git@github.com`
 8. Faites toutes les étapes, une à la fois, qui sont listés sous `…or create a new repository on the command line` SAUF: ignoré la première ligne (qui débute par `echo`) et modifiez la 3e pour qu'elle donne `git add .`
 9. Raffraichissez la page de github, vous devriez vous votre fichier apparaitre

## Modification du projet

Ces étapes sont à faire pour chaque nouvelle version du projet

 1. Modifiez votre fichier python, ajoutez un print par exemple. Sauvegardez le
 2. Dans le terminal de VSCode:
    1. Entrez `git add .`
    2. Entrez `git commit -m "Ajouter un print"`
    3. Entrez `git push`
 3. Rafraichissez la page de github et cliquez sur votre fichier python, vous devriez voir votre print

## Travailler à 2 ordinateurs

Si vous travaillez sur 2 ordinateurs, sur votre 2e ordinateur il faut faire:

 1. Dans github, dans la page principale de votre projet, vous devriez avoir un bouton vert `Code`, assurez-vous que l'option `SSH` est sélectionné puis copiez le lien
 2. Dans vos dossier de votre ordinateur, allez dans le dossier qui contiendra le futur dossier de projet (par exemple, votre Bureau ou vos Documents), faites un clique droit puis choisissez `Ouvrir la console` (le texte peut être différent selon votre version)
 3. Entrez la commande `git clone ...` en remplacant les `...` par le lien copié à l'étape 1. Vous devriez avoir le code sur votre 2e ordinateur maintenant.

Par la suite, si sur votre ordinateur 1 vous faites un `push`, sur le 2e ordinateur il faudra faire un `git pull` avant de commencer à travailler.