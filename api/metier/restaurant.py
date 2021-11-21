from api.metier.adresse import Adresse
from pydantic import BaseModel

class Restaurant (BaseModel) :
    """
    Cette classe permet de definir un restaurant dans notre application

    Attributes
    ----------
    nom : str
        Donne le nom du restaurant

    adresse : Adresse
        Adresse du restaurant

    statut : bool
        Permet de savoir si le restaurant est fermé ou ouvert

    id_restaurant : str
        Identifiant du restaurant

    """
    id_restaurant : str
    adresse : Adresse
    nom : str
    statut : bool
