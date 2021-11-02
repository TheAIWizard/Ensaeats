from Brouillon_Nikiema.metier.user import User
from Brouillon_Nikiema.metier.commande import Commande
from Brouillon_Nikiema.metier.utilisateur import Utilisateur

class Restaurateur (Utilisateur) :
    def __init__(self, user : User, commande : Commande, nom : str, prenom : str, 

    role : bool,  id_restaurateur) -> None:
        self.id_restaurateur=id_restaurant
        super().__init__( nom , prenom , telephone ,role , user, commande) 
    