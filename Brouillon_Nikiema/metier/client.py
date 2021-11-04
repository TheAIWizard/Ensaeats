from Brouillon_Nikiema.metier.utilisateur import Utilisateur
from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande


class Client (Utilisateur) :
    def __init__(self, user : User, commande : Commande, 
    nom : str, prenom : str, id_client : int) -> None:
        self.id_client=id_client
        self.telephone=telephone
        super().__init__( nom , prenom , telephone ,role , user, commande) 
    