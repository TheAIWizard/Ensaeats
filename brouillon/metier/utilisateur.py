from pydantic.main import BaseModel
from pydantic import BaseModel
from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande


class Utilisateur (BaseModel):
    nom :str
    prenom : str
    user : User
    commande : Commande
    