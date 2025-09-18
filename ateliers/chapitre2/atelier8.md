# Chapitre 2 - Atelier 8 - Exceptions

## Numéro 1

Demandez 2 nombres à l'utilisateur, divisez le nombre 1 par le nombre 2. Si on divise par zéro, interceptez l'erreur (avec une exception) et donnez zéro comme résultat.

Exemple:

```
Veuillez choisir le nombre 1: 42
Veuillez choisir le nombre 2: 0
La réponse est: 0.0
```

## Numéro 2

Reprendre le [numéro 5 de l'atelier 2-7](atelier7.md). Validez que l'information donné par l'utilisateur est valide (le nombre est bien un int positif et le prix est un bien un float positif avec 2 décimales ou moins).

*Copie de l'énoncé du numéro 5 de l'atelier 2-5:*

Demandez à l'utilisateur un nombre de produits et un prix unitaire. Affichez sur 2 décimales: Le sous-total, la TPS, la TVQ et le total.

Exemple:
```
Veuillez entrer un nombre de produits: 4
Veuillez entrer un prix unitaire: 9.99

Sous-total: 39.96
TPS: 2.00
TVQ: 3.99
Total: 45.95
```

Exemple avec la gestion d'erreurs:
```
Veuillez entrer un nombre de produits: jhk
Ce n'est pas un nombre valide

Veuillez entrer un nombre de produits: -98
Le nombre de produits doit être plus grand que zéro

Veuillez entrer un nombre de produits: 10
Veuillez entrer un prix unitaire: sdfg
Ce n'est pas un nombre valide

Veuillez entrer un nombre de produits: 10
Veuillez entrer un prix unitaire: -98.25
Le prix unitaire doit être plus grand que zéro

Veuillez entrer un nombre de produits: 10
Veuillez entrer un prix unitaire: 98.999
Le prix ne peut pas avoir plus de 2 décimales
```