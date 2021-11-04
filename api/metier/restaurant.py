from API.metier.adresse import Adresse
from pydantic import BaseModel

class Restaurant (BaseModel) :
    id_restaurant : int
    adresse : Adresse
    nom : str
    statut : bool
