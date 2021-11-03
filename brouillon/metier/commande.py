class Commande:
    """Constructeur des commandes
    """
    def __init__(self, id_commande: int,
                 date : int,
                 statut_commande: str,
                 liste_menu: list) -> None:
        self.id_commande = id_commande
        self.date = date
        self.statut_commande = statut_commande
        self.liste_menu = liste_menu
        
        
    def prix_total(self):
        """Calcul du prix total
        """
        prix_total = 0
        for menu in self.liste_menu:
            prix_total += menu.prix_menu
            
        return prix_total