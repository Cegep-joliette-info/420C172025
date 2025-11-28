import numpy as np
import numpy.typing as npt
import json
from typing import TypedDict

Pays = TypedDict('Pays', {'nom': str, 'capitale': str, 'population': int, 'superficieKm2': int, 'continent': str, 'languesOfficielles': list[str]})

# Typer un tableau de TypeDict ne fonctionne pas
_listePays = np.array([])


def _trouverPays(paysNom: str) -> Pays | None:
    return next((pays for pays in _listePays if pays['nom'] == paysNom), None)


def listeContinents() -> npt.NDArray[np.str_]:
    return np.unique([pays['continent'] for pays in _listePays], sorted=True)


def listePaysComplete() -> npt.NDArray[np.str_]:
    return np.array([pays['nom'] for pays in _listePays])


def obtenirContinent(paysNom: str) -> str:
    pays: Pays | None = _trouverPays(paysNom)
    return pays['continent'] if pays is not None else "N/D"


def obtenirCapitale(paysNom: str) -> str:
    pays: Pays | None = _trouverPays(paysNom)
    return pays['capitale'] if pays is not None else "N/D"


def obtenirPopulation(paysNom: str) -> int:
    pays: Pays | None = _trouverPays(paysNom)
    return pays['population'] if pays is not None else -1


def obtenirSuperficie(paysNom: str) -> int:
    pays: Pays | None = _trouverPays(paysNom)
    return pays['superficieKm2'] if pays is not None else -1


def obtenirLanguesOfficielles(paysNom: str) -> npt.NDArray[np.str_]:
    pays: Pays | None = _trouverPays(paysNom)
    return np.array(pays['languesOfficielles']) if pays is not None else np.array([])


def listeLanguesOfficielles() -> npt.NDArray[np.str_]:
    langues: set[str] = set()
    for pays in _listePays:
        for langue in pays['languesOfficielles']:
            langues.add(langue)
    return np.array(sorted(langues))


if len(_listePays) == 0:
    with open('fichiers/continents_pays.json', 'r', encoding='UTF-8') as f:
        fichierPays = f.read()
    _listePays = np.array(json.loads(fichierPays))