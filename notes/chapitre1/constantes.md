# Constantes

Attention, les constantes n'existent pas en Python, mais nous allons les simuler.

Une constante est une variable immuable, elle est identifié par une casse en majuscule seulement en notation serpent.

Par exemple, le taux de taxe ne devrait pas changer lors de l'exécution du programme, nous allons donc utiliser une constante:

```py
TAUX_TPS: float = 0.05
```

Toutes les valeurs numériques de votre programme doivent être dans une variable ou une constante. Exception: ce qui ne changera JAMAIS, comme le nombre de secondes dans une minute. Dans ce cas vous pouvez utiliser 60 au lieu d'une constante dans vos conversions de secondes en minutes ou inversement.