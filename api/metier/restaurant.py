from api.metier.adresse import Adresse
from pydantic import BaseModel

class Restaurant (BaseModel) :
    id_restaurant : str
    adresse : Adresse
    nom : str
    statut : bool
