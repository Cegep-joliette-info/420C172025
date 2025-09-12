# Git

Git est un système de contrôle de version distribué, c'est gratuit et open-source. Historiquement il avait des compétiteurs (SVN, Subversion, Mercurial, etc.) mais il est rendu le #1 en entreprise.

Plusieurs sites offres l'hébergement de répertoire Git, dont Github, Gitlab et Bitbucket.

Chaque répertoire git est téléchargé au complet, chaque répertoire git pourrait être utilisé comme un serveur.

Lorsque vous utilisez Git, vous avez le choix de télécharger et télécharger en SSH ou HTTPS, le premier demande une petite config, le 2e va vous demander votre mot de passe à chaque fois.

## Installation

Git est déjà installé sur les ordinateurs du cégep.

### Windows

Allez sur ce site: https://gitforwindows.org/ et cliquez sur le bouton "Download". En bas de la page vous pouvez voir une liste de "Assets", choisir celui qui termine par "64-bit.exe", ça devrait être le 3e dans la liste. Suivez les étapes, en cas de doute suivez ce tutoriel: https://github.com/Singcaster-CRLJ/CLJ/blob/main/Documents/WINGit.md

### Mac

Devrait déjà être installé, vous pouvez vérifier en ligne de commande en écrivant `git version`.

S'il n'est pas installé, vous pouvez le faire avec Homebrew. Si vous n'avez pas HomeBrew installez le avec la ligne de commande disponible sur cette page: https://brew.sh/.

En ligne de commande, roulez la commande `brew install git` ce qui devrait installer Git.

### Linux

Devrait déjà être installé, sinon utilisez votre gestionnaire de paquet pour l'installer, en cas de doute: https://git-scm.com/download/linux

## Config SSH

### Générer la clé SSH

Ouvrez votre terminal (ou Git Bash sous Windows). Exécutez la commande `ls -la ~/.ssh`. Si vous voyez quelques fichiers, dont un qui ressemble à `id_ed25519.pub` (le nom peut changer) vous avez déjà une clé SSH.

Si vous n'avez pas de clé, générez la avec la commande `ssh-keygen -t ed25519`. Le fichier par défaut est bon (appuyez sur Enter), le passphrase est un mot de passe pour utiliser votre clé SSH. C'est conseillé d'en mettre une pour éviter que des vilaines personnes utilise votre clé SSH, mais c'est optionnel.

Maintenant que vous avez une clé (ou si vous l'aviez déjà), allez voir le fichier avec la commande `cat ~/.ssh/id_ed25519.pub`, copiez la ligne que ça donne, vous devez l'ajouter à Github.

### Activation dans Github

Dans github.com, une fois connecté, cliquez sur votre icône en haut à droite puis sur "Settings". Dans le menu de gauche, choisir "SSH and GPG keys". Cliquez sur le bouton "New SSH key" puis collez votre clé. Votre clé SSH est configuré.

Il faut faire cette procédure pour tout ordinateur où vous voulez utiliser une clé SSH.

## Configuration Git

Votre Git doit être configuré sur chaque ordinateur utilisé (à faire en plus de votre clé SSH). Exécutez les deux lignes de code suivantes, en changeant les strings par vos informations:

```
git config --global user.email "YOUR_EMAIL"
git config --global user.name "Votre Nom"
```

Les informations données à ces commandes seront les informations vues dans Github pour chaque commit.
En enlevant les "--global" vous pouvez faire une configuration particulière pour un répertoire git spécifique.

## Préparation

La majorité des IDE (comme PyCharm) vont vous proposer de gérer votre répertoire Git, refusez cette offre. En le gérant manuellement, vous aurez plus de contrôle et serez meilleur pour gérer les cas avancés.

Ouvrez l'application Git Bash, naviguez jusqu'au dossier contenant votre projet avec `cd`. Vous pourriez vous faire un répertoire Git contenant tous vos ateliers de Prog1, dans ce cas naviguez jusqu'au dossier contenant tous les projets. Il ne devrait y avoir rien d'autre que votre ou vos projets dans le dossier courant. Vérifiez avec `ls` et `pwd` que vous êtes au bon endroit.

À la racine de ce dossier, créez le fichier ".gitignore" (`touch .gitignore` ou `nano .gitignore`) puis collez le texte disponible à l'adresse: https://github.com/github/gitignore/blob/main/Python.gitignore.

Ce fichier donne tous les dossiers et fichier à ne pas mettre dans le répertoire git. Tous les fichiers qui sont créés automatiquement ou qui ne sont pas nécessaires ne doivent pas se retrouver sur le serveur, ce fichier le fait par magie.

## Mise en place Git - nouveau répertoire

Lorsque vous configurez un nouveau répertoire Git, il faut exécutez les commandes suivantes.

Commencez par aller dans le bon dossier et mettre le .gitignore comme dit plus haut.

```bash
git init
```

Cette commande crée un répertoire git vide dans le dossier actuel. Il crée un dossier caché `.git`, pour l'instant pas besoin d'y toucher, mais il ne faut pas le supprimer!

```bash
git add .
# OU
git add README.md
```

La commande avec le "." ajoute tous les fichiers et dossiers où vous êtes dans l'Index. La version avec le "README.md" montre qu'on peut ajouter 1 fichier à la fois à l'Index, je pourrais ajouter plusieurs fichiers de cette manière, séparés par des espaces.

```bash
git commit -m "Mon premier commit"
```

La commande ajoute tous les fichiers de l'Index dans un Commit, puis remet l'Index à zéro. Un Commit est un ensemble de modification prêt à être envoyé au serveur.
La String après le -m est le message qui identifie ce Commit. Le message doit être une courte phrase qui débute par une majuscule et un verbe à l'infinitif. En lisant ce message je dois savoir ce qui a été ajouté au projet. Idéalement un commmit ne contient qu'un ensemble d'ajout.

Bon exemple:

 * Ajouter choix B
 * Corriger choix A
 * Commencer choix C

Mauvais exemple:

 * commit d'hier
 * test
 * dernier commit
 * dernier commit (vrai)
 * Ajouter choix A et B

```bash
git branch -M main
```

Git est un système basé sur des branches. Cette session nous allons rester sur la même branche qui est créé avec cette commande. On peut créer des branches pour créer des fonctionnalités sans nuire à la branche principale, lorsque notre fonctionnalité est terminée nous pouvons fusionner les 2 branches.

```bash
git remote add origin git@github.com:Cegep/test.git
# OU
git remote add origin https://github.com/Cegep/test.git
```

Remplacez le lien (après "origin") par votre URL. Le premier exemple est avec SSH et le 2e avec HTTPS. Cette commande ajoute le lien github comme "origin", soit le serveur qui va être synchronisé avec notre Git local.

```bash
git push -u origin main
```

Cette commande envoie notre répertoire git local vers le serveur. On envoie la branche "main" vers l'"origin".

Votre code est donc rendu sur le serveur, vous pouvez continuer à travailler ou mettre votre code sur un autre ordinateur.

## Mise en place Git - répertoire existant

Vous avez créé votre répertoire Git avec les étapes précédentes, vous voulez mettre en place votre répertoire Git à la maison.

Ouvrez votre répertoire Git sur github.com, cliquez sur le bouton "<> Code", choisissez HTTPS ou SSH puis copiez le lien.

Avec le commande `cd` dans Git Bash, rendez-vous dans le dossier qui contiendra votre projet (git va créer un nouveau dossier). En remplacant l'URL par le vôtre, entrez la commande suivante:

```bash
git clone git@github.com:Cegep/test.git
```

Rentrez dans le nouveau dossier avec `cd`, vous êtes maintenant dans un répertoire Git synchronisé avec le serveur.

## Utilisation générale de Git

Lorsque votre Git est placé, il faut se souvenir de quelques commandes importantes:

```bash
git status
```

Donne des informations sur le répertoire Git: s'il reste des fichiers à ajouter à l'index, s'il reste des commits à push, etc.

```bash
git add .
```

Permet d'ajouter tous les nouveaux fichiers l'Index. Vous pouvez spécifier des fichiers au lieu du ".".

```bash
git commit -m "Ajouter question 2 du devoir 3"
```

Crée un Commit à partir de l'index avec le message spécifié, vide l'Index.

```bash
git push
```

Envoie les nouveaux commits au serveur.

```bash
git pull
```

Récupère les nouveaux Commits du serveur et les places sur votre ordinateur. Attention, si vous avez fait des modifications depuis le dernier pull ou push cette commande va échouer.