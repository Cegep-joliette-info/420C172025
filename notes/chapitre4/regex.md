# Regex

Regex (Regular Expression)

Une expression régulière (regex) est une chaîne de caractères qui décrit, selon un motif, un ensemble de chaînes de caractères possibles. Un regex permet plusieurs traitements, par exemple:

 * mise en correspondance (matching) : s'assurer qu'une chaîne correspond à un motif
 * substitution : remplacer une ou plusieurs occurrences
 * extraction :  récupérer une sous-chaîne

Règles et conventions des motifs:

| Règle         | Description                                                         |
| :-----------: | ------------------------------------------------------------------- |
| .             | n'importe quel caractère                                            |
| abc           | la suite de ces caractères                                          |
| \[abc\]       | n'importe quel de ces caractères                                    |
| \[a-c\]       | un caractère entre cette plage                                      |
| \[^abc\]      | pas ces caractères                                                  |
| \[^a-z\]      | pas les caractères de cette plage                                   |
| \[abc\]\[oa\] | un parmis a, b, c suivi de une lettre o ou a                        |
| X\|Z          | X ou Z                                                              |
| ^             | en début de ligne                                                   |
| $             | en fin de ligne                                                     |
| {n}           | n fois                                                              |
| {n,m}         | de n à m fois                                                       |
| *             | {0,}                                                                |
| +             | {1,}                                                                |
| ?             | {0,1}                                                               |
| \\s           | espace                                                              |
| \\S           | non espace                                                          |
| \\d           | chiffres (digit) \[0-9\]                                            |
| \\D           | \[^0-9\]                                                            |
| \\w           | les caractères de mot \[A-Za-z0-9\]                                 |
| \\W           | \[^A-Za-z0-9\]                                                      |
| \\b           | boundary -> limite de mot                                           |

Notez que pour que votre regex sélectionne un caractère spécial pour `.` ou `?`, il faut mettre un `\` devant.

Pour capturer un groupe, il faut mettre des parenthèses autour de la règle. Pour faire un groupe non capturé, il faut mettre `?:` au début de la parenthèse. Exemple: la regex `(\d)(?:e|er|ere)` va prendre les nombres qui sont suivit de e, er ou ere, mais la recherche va seulement nous donner les nombres comme résultat. Donc il va nous dire qu'il a trouvé `2` de la chaîne `J'avais le numéro 4 et j'ai finis 2e`. Notez que s'il n'y a pas de parenthèses, la regex au complet est capturée.

## Exemple 1 regex

Regex pour un code postal:

`J0K 3P0`

```regex
[A-Z]\d[A-Z]\s\d[A-Z]\d
```

## Exemple 2 regex

Regex pour un numéro de téléphone dans plusieurs formats:
   
`ddd-ddd-dddd` `ddd.ddd.dddd` `(ddd)ddd-dddd` `ddd ddd dddd`

Les deux regex sont équivalents, le deuxième utilise des ou |

```regex
\(?\d{3}[\)\.\s-]\d{3}[-\.\s]\d{4}
\d{3}-\d{3}-\d{4}|\d{3}\.\d{3}\.\d{4}|\(\d{3}\)\d{3}-\d{4}|\d{3}\s\d{3}\s\d{4}
```

## Python

Notez que les chaînes contenant les expressions régulières ont un `r` devant l'ouverture de la chaîne. Le `r` veut dire *raw*, mais pourrait aussi dire *regex*. Dans une chaîne *raw*, le `\` n'est pas un caractère spécial.

```py
import re

texte: str = "Texte à fouiller"
filtre: str = r"Chaine du regex"

for correspondance in re.finditer(filtre, texte):
    print(correspondance.group(), correspondance.span()[0], correspondance.span()[1])
```

```py
import re

texte: str = "Alice au pays des merveilles avec ses amis Tigrou et Amélie."
filtre: str = r"(\w+)"
for correspondance in re.finditer(filtre, texte):
    print(correspondance.group(), correspondance.span()[0], correspondance.span()[1])
```

Méthodes de `re`:

 * `findall` donne une liste de chaîne de tous les résultats
 * `search` donne un match d'un résultat
 * `finditer` donne un itérateur qui permet d'avoir les matchs de tous les résultats
 * `split` donne une liste de chaînes, chaque élément trouvé devient un changement de case, donc les éléments non-trouvés deviennent des cases
 * `sub` remplace tous les éléments trouvés par la chaîne donné

```py
texte: str = "Alice au pays des merveilles avec ses amis Tigrou et Amélie."
re.findall(r"(es)", texte) # Donne ['es', 'es', 'es']
re.search(r"(es)", texte) # Donne un match, utilisez les fonctions group() et span()
re.split(r"\W", texte) # Donne ['Alice', 'au', 'pays', 'des', 'merveilles', 'avec', 'ses', 'amis', 'Tigrou', 'et', 'Amélie', '']
texte = re.sub(r"e", "", texte) # Donne "Alic au pays ds mrvills avc ss amis Tigrou t Améli."
```

Le search donne `None` s'il ne trouve rien. Exceptionnelement, vous pouvez utiliser le `is None` avec le résultat de la fonction.

Vous pouvez ajouter le paramètre `flags=re.IGNORECASE` à toutes les fonctions précédentes pour que votre regex trouve majuscule et minuscule, exemple:

```py
texte: str = "Alice au pays des merveilles avec ses amis Tigrou et Amélie."
re.findall(r"a", texte, flags=re.IGNORECASE) # Donne ['A', 'a', 'a', 'a', 'a', 'A']
```