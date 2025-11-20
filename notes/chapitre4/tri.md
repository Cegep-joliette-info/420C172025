# Tris BS / SSS

## Tri Bulle (Bubble Sort)

### Fonctionnement tri Bulle

 * Première passe l'indice i parcourt tous les éléments du tableau sauf le dernier
 * Deuxième passe l'indice j parcourt tous les éléments du tableau suivant i jusqu'au dernier
    * Si l'élément à l'indice j est plus petit que l'élément à l'indice i, on permute les deux valeurs

### Pseudo code tri Bulle

```
for (int i = 0; i < index avant dernier élément du tableau; i++)
   for (int j = i+1; j < index dernier élément du tableau; j++)
        if (élément du tableau[j] < élément du tableau[i])
            permuter les éléments aux indices i et j du tableau
```

## Tri Sélection SSS (Straight Selection Sort)

### Fonctionnement tri SSS

 * Première passe l'indice i parcourt tous les éléments du tableau sauf le dernier
 * Deuxième passe l'indice j parcourt tous les éléments du tableau suivant i jusqu'au dernier
    * Trouve l'indice imin du plus petit élément
    * Si l'indice imin n'est pas l'indice i, on permute les valeurs aux indices imin et i

### Pseudo code tri SSS

```
int imin;

for (int i = 0; i < index avant dernier élément du tableau; i++)

    imin = i;

    for (int j = i+1; j < index dernier élément du tableau; j++)
        if (élément du tableau[j] < élément du tableau[imin])
            imin = j;

    if (imin != i)
        permuter les éléments aux indices i et imin du tableau
```