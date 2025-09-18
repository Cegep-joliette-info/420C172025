# Exceptions

Les exceptions sont des erreurs déclanchés par le système ou par le programmeur. Nous en avons croisé 2 à date:

 * `ValueError` lorsqu'on essaie de convertir une chaîne en int ou float et que ce n'est pas un nombre
 * `ZeroDivisionError` lorsqu'on essaie de diviser par zéro

Ces erreurs peuvent être interceptés par le programmeur avant que ça explose sur l'utilisateur. Exemple:

```py
try:
    i = int(input("Veuillez entrer un nombre: "))
    print("Merci d'avoir saisie un nombre")

except ValueError:
    print("Ce n'était pas un nombre")
```

Dès que l'erreur spécifié dans le except est croisé dans le try, le programme saute dans le code du except sans continuer le code du try. Dans l'exemple précédent un seul des deux print sera exécuté.

Vous pouvez intercepter plusieurs erreurs pour le même code:

```py
try:
    i = 100 / int(input("Veuillez entrer un nombre: ))

except (ValueError, ZeroDivisionError):
    print("Erreur, valeur invalide")

# OU encore mieux, un message personnalisé:

try:
    i = 100 / int(input("Veuillez entrer un nombre: ))

except ValueError:
    print("Erreur, ce n'était pas un nombre")

except ZeroDivisionError:
    print("Erreur, division par zéro")

else:
    print("Tout a bien été")
```

Dans le 2e exemple il y a un else, c'est le code qui sera exécuté s'il n'y a pas eu d'exception. Le code présent dans le try et les except doivent être le plus simple possible, il ne faut pas mettre tout votre code dans un try!