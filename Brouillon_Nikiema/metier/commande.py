class Commande:
    """Constructeur des commandes
    """
    def __init__(self, id_commande : int,
                 date : str,
                 paiement : float,
                 statut_commande : str,
                 liste_menu: list) -> None:
        self.id_commande = id_commande
        self.date = date
        self. paiement = paiement
        self.statut_commande = statut_commande
        self.liste_menu = liste_menu
        