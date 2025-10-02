# Chapitre 3 - Atelier 3 - Chaînes et tableaux

## Numéro 1

Demandez du texte à l'utilisateur, affichez le nombre de caractères saisies

```
Entrez du texte: asdf
Vous avez saisie 4 caractères

Entrez du texte: Never gonna give you up
Vous avez saisie 23 caractères
```

## Numéro 2

Demandez du texte à l'utilisateur. Répétez le même texte à l'utilisateur, mais attendez 0.1 seconde entre chaque lettre.

Pour attendre 1 seconde, ajoutez le import `import time`, puis vous pourrez utiliser `time.sleep(1)` pour attendre 1 seconde avant de continuer le code.

## Numéro 3

Demandez du texte à l'utilisateur, affichez le nombre de chiffre, lettre minuscule, lettre majuscule, caractère blanc et caractère autre.

```
Entrez du texte: 1234 abc ERT É!@
4 chiffres
3 minuscules
4 majuscules
3 caractères blancs
2 autres caractères
```

## Numéro 4

Demandez une phrase à l'utilisateur, affichez le mot le plus long et le plus court.

```
Entrez du texte: Never gonna give you up
Le mot le plus long est: Never
Le mot le plus court est: up

Entrez du texte: aaaaa aa a aaaaaaaaaaaaaaa a
Le mot le plus long est: aaaaaaaaaaaaaaa
Le mot le plus court est: a
```

## Numéro 5 - défi

Demandez du texte à l'utilisateur, affichez le nombre de chaque lettre saisie par l'utilisateur.

 * Les caractères accentués francophones, les minuscules et les majuscules comptent ensemble (exemple, e, E et É sont comptés ensemble).
 * Ne pas afficher les lettres manquantes dans le texte
 * Comptez les caractères autres, les caractères d'espacement ne comptent pas

Ne créez pas 26 variables avec un match de 26 possibilités, utilisez un tableau.

```
Entrez du texte: Petit papa noël, ça va au pôle nord?
a: 5
c: 1
d: 1
e: 3
i: 1
l: 2
n: 2
o: 3
p: 4
r: 1
t: 2
u: 1
v: 1
Autres: 2
```