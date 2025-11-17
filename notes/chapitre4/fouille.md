# Fouille séquentielle

Un algorithme de fouille retourne l'indice de la valeur trouvée ou -1 si la valeur n'est pas trouvée.

## Fonctionnement de la fouille séquentielle

 * `TantQue` (la valeur n'est pas trouvée et que le tableau n'a pas été parcouru au complet)
    * `Si` la valeur est trouvée, on arrête de chercher
    * `Sinon` on avance dans le tableau au prochain élément
 * `FinTantQue`
  
`Si` on a trouvé on retourne l'indice correspondant
`Sinon` on retourne -1

## Note

 * La fouille séquentielle n'exige pas que les éléments du tableau soient triés.
 * S'il y a plusieurs occurrences de la valeur recherchée dans le tableau, la fouille séquentielle retourne la position de la première occurence.
 * Si la valeur recherchée n'est pas dans le tableau, le nombre d'éléments consultés sera égal au nombre d'éléments dans le tableau.

## Pseudo code de la fouille séquentielle

```
indexDeX(tableau à parcourir, element recherché)

    i = 0 #index du tableau
    trouve = false #indicateur de recherche
    resultat = -1  #pour sauvegarder le résultat

    TantQue pas trouve et i < fin tableau
        Si element  == tableau[i]
             trouve = vrai
        Sinon
            i += 1

    Si trouve
        resultat = i
    Sinon
        resultat = -1
    return resultat
    # Ou faire un if ternaire à la place des 5 dernières lignes
```