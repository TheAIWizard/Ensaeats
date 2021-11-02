from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande
"""
Le type de telephone est str 
"""
class Utilisateur :
    def __init__(self, nom : str, prenom : str, telephone : str,
    role : bool, user=User, commande : Commande) -> None:
        self.nom= nom
        self.prenom=prenom
        self.telephone=telephone
        self.role=role
        self.user=user
        self.commande=commande

