from Brouillon_Nikiema.metier.utilisateur import Utilisateur
from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande
from pydantic.main import BaseModel

class Client (Utilisateur, BaseModel) :
    id_client : int
    telephone : str
    user : User
    commande : Commande
    nom : str
    prenom : str
