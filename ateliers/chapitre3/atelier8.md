# Chapitre 3 - Atelier 8 - Tuples

## Numéro 1

Faites une fonction `demanderNom` qui demander le nom et le prénom de l'utilisateur, on repose la question si l'entrée est vide ou seulement des caractères blancs. La fonction retourne un tuple contenant les informations.

Faites une deuxième fonction `saluer` qui accepte en paramètre un tuple généré par la fonction `demanderNom`, saluez la personne.

```
Entrez votre prénom:   
Invalide, veuillez recommencer
Entrez votre prénom: Phil
Entrez votre nom de famille: Girard
Bonjour Phil Girard
```

## Numéro 2

Écrivez les fonctions suivantes:

 1. `demanderPoint` qui demande un point à l'utilisateur et retourne les deux entier x et y
 2. `validerPoint` qui vérifier si le point donné existe selon la formule 2x<sup>2</sup> + 3x - 1

```
Entrez la coordonnée x: z
Invalide, veuillez recommencer
Entrez la coordonnée x: 4
Entrez la coordonnée y: 8
Point invalide

Entrez la coordonnée x: 2
Entrez la coordonnée y: 13
Point valide
```

## Numéro 3 - Défi

Créez les fonctions suivantes:

 1. `genererDate` qui choisi des nombres aléatoires entre 1000 et 2000 (année), 1 et 12 (mois) et 1 et 31 (jours) sans rien valider et retourne les 3 nombres
 2. `validerDate` qui reçoit en paramètre 3 nombres sous forme de tuple et retourne un booléen, True si le tuple représente une date valide*
 3. `essayerDates` qui essaie de générer 10 dates valides de suite, vous pouvez afficher chaque date essayé

*Attention aux années bissextiles, le mois de février a 29 jours si l'année est divisible par 4 mais pas pas 100, sauf si l'année est divisible par 400. Donc 2400 est bissextile car divisible par 400, mais pas 2100. Faites des tests unitaires pour le essayerDates.