# Chapitre 2 - Atelier 9 - Fonctions

## Numéro 1

```py
def concatener(ch1: str, ch2: str) -> None:
    ch1 += ch2


s: str = "Bonjour"
print(s)
concatener(s, " Monde")
print(s)
```

Modifier le code pour qu'il affiche:

```
Bonjour
Bonjour Monde
```

## Numéro 2

Sans exécuter le code, que va-t-il afficher? Testez ensuite votre réponse en l'exécutant.

```py
def calculer1(x: int, y: int) -> None:
    x = 878
    y += 1
    print("3. x =", x)
    print("4. y =", y, "\n")


def calculer2(a: int, b: int) -> None:
    x: int = 33
    y: int = 44
    a = 2 * x
    b = 2 * y
    print("7. x =", x)
    print("8. y =", y)
    print("9. a =", a)
    print("10. b =", b, "\n")


x: int = 11
y: int = 22
print("1. x =", x)
print("2. y =", y, "\n")

calculer1(x, y)
print("5. x =", x)
print("6. y =", y, "\n")

calculer2(x, y)
print("11. x =", x)
print("12. y =", y, "\n")
```

## Section 2

Attention, n'oubliez pas qu'il ne faut pas mettre de input ou print dans les fonctions à moins que c'est son but direct!

## Numéro 3

Écrire une méthode `estMajeur` qui détermine si un âge reçu en argument est majeur ou non.  On considère que 18 est l'âge majeur. 
 
Test dans méthode main : À partir d’un age afficher l'état d'une personne "majeur" ou "mineur" en invoquant la méthode `estMajeur`. 

## Numéro 4

Écrire une méthode `estMajeurUniversel` qui détermine si un âge reçu en argument est majeur universel ou non. On considère que 21 est l'âge majeur universel. 

## Numéro 5

Écrire une méthode `estReussite` qui détermine, à partir d'une note entière reçue en argument, si la note est une réussite ou non. On considère une réussite lorsque la note est 60 et plus. 

## Numéro 6

Écrire une méthode `exposantDeux` qui retourne un entier reçu en argument exposant 2.

## Numéro 7

Écrire une méthode `estPair` qui détermine si un entier reçu en argument est un nombre pair ou non.

## Numéro 8

Écrire une méthode `prixDiff` qui retourne la différence entre deux montants reçus en argument.

Test: À partir de deux montants afficher "perte de x.xx$" ou "profit de x.xx$" en invoquant la méthode `prixDiff`.

## Numéro 9

Écrire une méthode `estPlusGrand` qui détermine si un premier entier est plus grand qu'un deuxième entier, les entiers sont reçus en argument.  
 
Test: Afficher deux entiers en ordre croissant en invoquant la méthode `estPlusGrand`.

## Numéro 10

Écrire une méthode `plusGrand` qui retourne l'entier le plus grand entre trois entiers reçus en argument.

## Numéro 11

Écrire une méthode `estDivisible` qui détermine si un entier reçu en argument est divisible ou non par 3 et 13.

## Numéro 12

Écrire une méthode `nbJours` qui à partir d'un numéro du mois reçu en argument retourne le nombre de jours de ce mois. 
(Ici on ne considère pas les années bissextiles)

 * 31 jours: Janvier, Mars, Mai, Juillet, Aout, Octobre, Décembre
 * 30 jours: Avril, Juin, Septembre, Novembre
 * 28 jours: Février
 * 0 jours: Autre

## Numéro 13

Écrire une méthode `selLangue` qui à partir d’une lettre reçue en argument retourne la langue correspondante parmi (A)nglais, (E)spagnol et (F)rançais. Si la lettre n'est pas reconnue retourne "Inconnu". Exemple pour le caractère 'a' retourne "Anglais" ou pour le caractère 'A' retourne "Anglais".

## Numéro 14

Écrire une fonction `calculer` qui à partir de deux entiers et d’un opérateur arithmétique ('+', '-', '*', '/', '%') reçus en argument, retourne le résultat de l’expression. 
\* Nous ne gérons pas dans la fonction les modulo et division par zéro. 
 
Test: Afficher le résultat d'une expression arithmétique en invoquant la méthode `calculer`. Attention si le deuxième opérande est 0 et que l'opérateur est modulo ou division, la méthode n'est pas invoquée et afficher "erreur deuxième opérande zéro". Les opérandes sont des entiers.

## Numéro 15

Écrire une méthode `couleurSecondaire` qui à partir de deux couleurs reçues en argument parmi le (R)ouge, le (J)aune et le (B)leu, retourne la couleur résultante ou "Aucune" si les lettres ne correspondent pas aux choix. On figure que les lettres sont en majuscules. 

Exemple:

 * avec les caractères 'R' et 'J' (ou 'J' et 'R') retourne "Orange", 
 * avec les caractères 'J' et 'B' (ou 'B' et 'J') retourne "Vert", 
 * avec les couleurs 'R' et 'B' (ou 'B' et 'R') retourne "Violet", 
 * avec les couleurs 'X' et 'Z' retourne "Aucune".

## Numéro 16

Écrire une méthode `nbCentral` qui à partir de trois nombres entiers reçus en argument retourne le nombre central. 

## Numéro 17

Écrire une méthode `max2` qui retourne l'entier le plus grand entre deux entiers reçus en argument.

## Numéro 18

On refait le numéro 4 de l'atelier 2 du chapitre 2.

Faites une fonction qui affiche la phrase `Veuillez entrer la note #1: ` en permettant de changer le numéro, puis elle retourne la réponse de l'utilisateur.

Appelez cette fonction 5 fois puis calculez la moyenne. Vous pouvez faire cette partie dans une autre fonction ou dans la partie globale du fichier.

```
Veuillez entrer la note #1: 75
Veuillez entrer la note #2: 92
Veuillez entrer la note #3: 41
Veuillez entrer la note #4: 60
Veuillez entrer la note #5: 88

La moyenne est de: 71.20%
```

## Numéro 19

Faire plusieurs fonctions mathématiques qui traitent 2 nombres: `additionner`, `diviser`, `soustraire`, `multiplier` et `modulo`. Faites ensuite la fonction `calculer2`, qui demande 2 nombres et une opération à l'utilisateur, appel la bonne fonction pour calculer puis affiche le résultat.

## Numéro 20 - Petit défi

Écrire une méthode `max4` qui retourne l'entier le plus grand entre quatre entiers reçus en argument. Vous ne pouvez pas utiliser d'opérateur de comparaison dans cette fonction, mais vous pouvez utiliser la fonction du numéro 17 `max2`.

## Numéro 21 - Défi

ATTENTION, faire ce numéro sans boucle.

Écrire une fonction `ajouterNombre` qui demande un nombre à l'utilisateur. S'il ne réponds pas "0", reposer la question de nouveau. Additionnez tous les nombres reçus et retourner le total.

Indice: Une fonction peut appeler une fonction.

Exemple de résultat en console:

```
Veuillez entrer un nombre, zéro pour quitter: 5
Veuillez entrer un nombre, zéro pour quitter: 7
Veuillez entrer un nombre, zéro pour quitter: -1
Veuillez entrer un nombre, zéro pour quitter: 0
Total: 11
```