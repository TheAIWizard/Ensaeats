from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande
from Brouillon_Nikiema.metier.utilisateur import Utilisateur
from pydantic.main import BaseModel
class Restaurateur (Utilisateur, BaseModel) :
    id_restaurateur : int
    user : User
    commande : Commande
    nom : str
    prenom : str