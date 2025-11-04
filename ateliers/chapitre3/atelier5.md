# Chapitre 3 - Atelier 5 - Tests unitaires

## Numéro 1

Reprenez votre chapitre 3 atelier 4, ajoutez des tests unitaires sur toutes les fonctions.

N'oubliez pas que pour respecter les normes, il faut faire 1 fichier de test par module.

## Numéro 2

Dans un nouveau modules, faites les fonctions suivantes avec leurs tests unitaires:

 * La fonction inverserTexte qui prend une chaîne en paramètre et retourne la même chaîne mais inversé ("asdf" deviendra "fdsa")
 * La fonction initiale qui prend un nom en paramètre et retourne les initiales, par exemple si je donne "Philippe Girard" la fonction retourne "PG"
 * La fonction compterMultiples qui prend un tableau de nombres et un nombre en paramètre et qui retourne un nombre. La fonction compte dans le tableau le nombre de multples trouvés. Par exemple si j'envoie [2, 5, 4, 9] et 2, ça va me retourner 2 (il y a 2 multiples de 2 dans le tableau).

## Numéro 3

Avec l'approche TDD, écrivez les fonctions suivantes:

 * Fonction fizzBuzz, qui reçoit un nombre en paramètre et qui retourne: Fizz si le nombre est un multiple de 3, Buzz s'il est multiple de 5 et FizzBuzz s'il est les deux
 * Fonction validationMotDePasse, qui reçoit une chaîne et qui retourne un booléen, vrai si le mot de passe contient au moins une minuscule, une majuscule, un chiffre et un caractère spécial. N'oubliez pas de faire un test par possibilités (un mot de passe sans minuscule, un sans majuscule, etc.) ainsi que le cas limite et le cas de réussite.