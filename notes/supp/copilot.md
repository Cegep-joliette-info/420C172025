# Github Copilot

## Sur github.com

Si ce n'est pas fait, demandez le [Github student developer pack](https://education.github.com/pack) pour avoir accès gratuitement à Copilot.

En tout temps, dans vos paramètres Github, section "GitHub Copilot", vous pouvez gérer votre abonnement à Copilot. Vous pouvez voir votre utilisation à cette adresse: https://github.com/settings/copilot/features

## Dans VS Code

Dans la barre de titre de VS Code, cliquez sur l'icône de Copilot (un petit robot) pour ouvrir le panneau de Copilot.

Cliquez sur la flèche vers le bas à côté de "GitHub Copilot" pour ouvrir les paramètres puis cliquez sur "Configure Code Completions". La 4e option devrait être "Disable GitHub Copilot". Choisissez cette option pour désactiver Copilot dans VS Code.

Rappel: Vous devez être capable d'écrire du code sans l'aide de Copilot pour votre futur travail et pour l'examen.

Dans le panneau de Copilot, en bas à gauche, cliquez sur "Agent" puis sélectionnez "Ask".

 * Le mode "Agent" est là pour écrire du code, ça ne vous aidera pas à apprendre.
 * Le mode "Ask" est là pour poser des questions sur votre code ou sur des concepts de programmation. C'est comme un ChatGPT qui a accès à votre projet.

## Corriger votre projet avec Copilot

Créez un dossier `correction` à la racine de votre projet. Dans ce dossier, copiez les fichiers suivants qui sont dans le Github du cours:

 * [tp3.md](tp/tp3.md)
 * [normes.md](notes/supp/normes.md)

Finalement, dans le panneau de conversation de Copilot, posez la question suivante:

```
enonce.md specify what i must do, normes.md specify the coding standards, can you grade my code?
Ignore pays.py
```