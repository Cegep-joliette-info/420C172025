# Module

Chaque fichier Python est appelé un module.
Chaque script Python est composé d'un module principal et peut avoir plusieurs modules *secondaires*.
Les modules secondaires ne doivent pas avoir de code "globale", ils doivent seulement contenir des fonctions.

Vous pouvez donc créer vos propres modules, ou utiliser ceux qui sont inclus par Python (random, time, math, etc.) ou par pip (numpy).

Lorsque vous faites un import, Python cherche un module qui a le nom spécifié (sans le .py).
Pour voir les dossiers où Python cherche, exécutez le code suivant:

```py
import sys
print(sys.path)
```

## Module personnalisé

Vous pouvez donc faire un module qui contient vos fonctions utilitaires.
Votre module principal peut utiliser le module utilitaire. Par exemple le code suivant:

```py
# Fichier mathematique.py
def addition(a: int, b: int) -> int:
    return a + b

# Fichier main.py
import mathematique
a: int
a = mathematique.addition(4, 2)
print(a)
```

Si votre module secondaire se trouve dans un sous-dossier, le séparateur de dossier est le `.` pour les modules.
Par exemple, si vous déplacez le fichier mathematique.py précédent dans un dossier lib, votre fichier main.py devient:

```py
import lib.mathematique
a: int
a = lib.mathematique.addition(4, 2)
print(a)
```

N'oubliez pas que le as existe lorsque le nom du import devient long:

```py
import lib.mathematique as monMath
a: int
a = monMath.addition(4, 2)
print(a)
```

Notez qu'on ne peut pas reculer dans les dossier. Si j'ai 2 sous-dossier: lib et lib2. Les modules de lib ne peuvent pas utiliser les modules et lib2 et inversement.

Comme Windows ne considère pas la casse, les modules vont être nommés en notation serpent. Donc tout en minuscule, sans accent, avec un `_` entre chaque mot. Par exemple: `mathematique_tableau.py`.

Si votre module se trouve dans un sous dossier et qu'il doit utiliser un autre module du même sous-dossier, votre dossier doit contenir un fichier vide nommé `__init__.py` (il y a 2 `_` au début et à la fin). Sans ce fichier Python ne trouvera pas le fichier.

## Import

L'import possède quelques variantes intéressantes, par exemple:

```py
from lib.mathematique import *
```

Avec cet import vous pouvez utiliser les fonctions du module directement, sans mettre le nom du module en préfixe. Vous pouvez donc faire directement: `a = addition(4, 2)`.
Notez que cette synthaxe, bien qu'utile, peut surcharger votre programme principal. Il est préférable de garder le préfixe du module lorsque possible.

Au lieu du `*` du import précédent, vous pouvez spécifier les fonctions à importer, par exemple:

```py
from lib.mathematique import addition, soustraction as sous
```

Les fonctions addition et soustraction seulement sont donc importés, et la fonction soustraction est renommé.
Notez que tous les expert sont d'accord, bien que le `*` est plus simple, il est fortement déconseillé de l'utiliser, si vous utilisez cette variante vous devez nommer les fonctions à importer.

La différence du `import` avec et sans `from` est plus grande. Considérez le code suivant du module `lib/mathematique.py`:

```py
# Ne pas reproduire, ce code ne respecte pas nos règles
multi: int = 2

def testMult(a: int) -> int:
    return a * multi
```

Vois le résultat avec les 2 types de imports:

```py
from lib.mathematique import *
multi = 4
print(testMult(3)) # Affiche 6
```
```py
import lib.mathematique as m
m.multi = 4
print(m.testMult(3)) # Affiche 12
```

Explication simple: avec le `from`, les variables sont copiés, le code du module `lib.mathematique` a donc encore la valeur initiale de `multi` qui ne peut pas être changé dans mon module principal. Par contre, on utilise encore les fonctions directement du module.

Explication complexe (pour ceux qui ont des connaissances en Orienté Objet et/ou C++): Le import fait des pointeurs vers ce qui est importé. Sans le `from`, on a un pointeur vers le module, on accède donc directement aux symboles du module.
Avec le `from` on copie les valeurs vers le module principal. Comme les fonctions sont des "objets", ça copie la référence vers la fonction au lieu de copier la fonction, on continue donc d'utiliser la fonction originale. Par contre les valeurs statiques sont copiés tout simplement, on pert la référence pour ces valeurs.

## Fonction privé

Certaines fonctions sont utiles seulement pour votre module et ne devraient pas être utilisés par les autres modules. Dans ce cas, préfixez le nom de la fonction par un `_`. Ça n'empêche rien, mais ça demande aux autres programmeurs de ne pas l'utiliser.
Votre IDE connais cette norme, il vous donnera un avertissement si vous utilisez une fonction privé.

## Référence

 * https://docs.python.org/3/tutorial/modules.html