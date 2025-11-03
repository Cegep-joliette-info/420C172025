# Tests unitaires

Un test unitaire permet de tester de manière unitaire une fonction. Si toutes vos fonctions sont testés de manière unitaire, votre code devrait toujours fonctionner. Et si les tests sont toujours effectués, votre code n'arrêtera jamais de planter "par erreur".

Les tests unitaires sont plus souvent utilisés avec de l'orienté objet, mais nous allons l'utiliser sans classe.
Nous allons ignorer plusieurs "bonnes pratiques" de tests qui alourdiraient inutilement notre code.

Pour chaque fichier à tester, nous allons créer un fichier du même nom qui servira à faire des tests, ce fichier par contre terminera par `_test.py`. Par exemple, le module `mathematique.py` aura le fichier de test `mathematique_test.py`.

Les fichiers de tests peuvent être dans le même dossier que le fichier original, ou dans un sous-dossier `tests`.

Pour démarer les tests, il faut 2 lignes très importantes:

```py
import unittest
tc = unittest.TestCase()
```

La première importe le module intégré de test unitaires.
La deuxième crée un cas de test, cette variable servira à rouler tous nos tests.

Ensuite il faut importer notre module à tester, à faire les tests, puis de print que tout a bien été. La fonction principale pour les tests est `assertEqual` qui permet de vérifier que 2 variables sont égales. Exemple de test complet d'une fonction:

```py
import unittest
import lib.mathematique as m

tc = unittest.TestCase()

tc.assertEqual(m.division(4, 2), 2)
tc.assertEqual(m.division(4, -2), -2)
tc.assertEqual(m.division(8, 0), 0)
print("Fonction division OK")
```

Si un `assert` plante, il vous dit la valeur que la fonction a retourné, ce qui est bien pratique!
Le dernier `print` sert a savoir que le fichier a bien exécuté, si tout va bien, sans ce print, il ne se passe rien.

Testez avec au moins 2 jeux de tests, ainsi qu'avec les valeurs limites. Les valeurs limites sont des valeurs qui sont à risque de faire planter votre code, les cas classiques sont zéro et tableau vide.

## Quoi ne pas tester

Vous ne pouvez pas tester 2 choses: les fonctions aléatoires et les fonctions qui interagissent avec le terminal (`print` et `input`).

Les fonctions aléatoires donnent un résultat variable, ce qui empêche de comparer avec des valeurs fixes. Le terminal n'est pas accessible par les fonctions de tests, les fonctions `print` et `input` ne sont donc pas testables.

Dans votre TP1, les fonctions `motAleatoire` et `dessiner` seraient donc non testables.

Dans le cas de fonction non-testable, la logique doit être le plus simple possible afin de limiter le code non-testé. Les fonctions cités dans le paragraphe précédents sont des bons exemples, très peu de code à part l'aléatoire et le print.

## Assertions

Voici une liste de la majorité des fonctions `assert`, avec ce qu'ils font dans le code:

| Assertion                      | Code                         |
|--------------------------------|------------------------------|
| `assertEqual(a, b)`            | `a == b`                     |
| `assertNotEqual(a, b)`         | `a != b`                     |
| `assertTrue(a)`                | `a == True`                  |
| `assertFalse(a)`               | `a == False`                 |
| `assertIn(a, b)`               | `a in b`                     |
| `assertNotIn(a, b)`            | `a not in b`                 |
| `assertAlmostEqual(a, b)`      | `round(a, 7) == round(b, 7)` |
| `assertNotAlmostEqual(a, b)`   | `round(a, 7) != round(b, 7)` |
| `assertGreater(a, b)`          | `a == b`                     |
| `assertGreaterEqual(a, b)`     | `a == b`                     |
| `assertLess(a, b)`             | `a == b`                     |
| `assertLessEqual(a, b)`        | `a == b`                     |
| `assertRegexpMatches(a, b)`    | `b.search(a)`                |
| `assertNotRegexpMatches(a, b)` | `not b.search(a)`            |

Les 2 dernières utilisent les regex, qui seront vus plus tard dans la session.

Dans tous les exemples précédents, `a` devrait être la valeur donné par votre fonction à tester, `b` (s'il y en a un) devrait être la valeur fixe qui sert pour le test.