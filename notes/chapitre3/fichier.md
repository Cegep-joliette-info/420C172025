# Lire et écrire dans un fichier

Important, tous vos fichiers doivent suivre la notation serpent (tout en minuscule, mots séparés par des _, pas d'accent). Si vous ne suivez pas cette norme votre programme pourrait planter lors de la correction (je suis sur Linux).

## Lire un fichier

Pour lire un fichier, la majorité des sites vont vous donner le code suivant:

```py
with open('fichier.txt', 'r') as file:
    data = file.read()
```

Le `with` va supprimer la variable `file` à la fin de son bloc, sans le `with` (`open('fichier.txt', 'r').read()`), le fichier va rester ouvert en mémoire, vous ne pourrez pas modifier ou supprimer le fichier tant que votre programme est ouvert.

Le `r` dit que le fichier est ouvert en lecture seul. Les 2 lignes de codes vont donc sauvegarder le fichier dans la variable `data` que vous pourrez utiliser à l'extérieur du `with`.

Une autre solution, plus simple avec un import:

```py
from pathlib import Path
txt = Path('fichier.txt').read_text()
```

Notez que pour les 2 fonctions, vous pouvez utiliser un chemin relatif ou absolue.

## Écrire dans un fichier

Similaire à lire dans un fichier...

```py
# Ajoute à la fin du fichier
with open('fichier.txt', 'a') as file:
    file.write("asdf")

# Remplace le contenu du fichier
with open('fichier.txt', 'w') as file:
    file.write("asdf")

# Avec pathlib, le mode 'a' n'existe pas, on peut juste remplacer le contenu
from pathlib import Path
Path('fichier.txt').write_text("asdf")
```

## Lire et écrire

Les 2 en même temps:

```py
# En mode "append"
with open('fichier.txt', 'r+') as file:
    print(file.read()) # Vous devez read avant, et juste 1 fois
    file.write("asdf") # Ajoute asdf au fichier
```

## Vérifier que le fichier existe

Si on ouvre un fichier en lecture et qu'il n'existe pas, ça plante. Il faut donc s'assurer que tout fonctionne bien:

```py
# Version open
try:
    with open('fichier.txt', 'r') as file:
        data = file.read()
except FileNotFoundError:
    print("Erreur le fichier n'exite pas")

# Version pathlib
from pathlib import Path
p: Path = Path('fichier.txt')
if p.exists():
    txt: str = p.read_text()
```