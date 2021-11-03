from Brouillon_Nikiema.metier.adresse import Adresse
class Commande:
    """Constructeur des commandes
    """
<<<<<<< HEAD
    def __init__(self, id_commande : int,
                 date : str,
                 paiement : float,
                 statut_commande : str,
                 liste_menu: list,
                 adresse : Adresse) -> None:
=======
    def __init__(self, id_commande: int,
                 date : int,
                 paiement: float,
                 statut_commande: str,
                 liste_menu: list) -> None:
>>>>>>> 680eeb6588d5f561a8910f71a1613c8d1955dd46
        self.id_commande = id_commande
        self.date = date
        self.paiement = paiement
        self.statut_commande = statut_commande
        self.liste_menu = liste_menu
        self.adresse=adresse