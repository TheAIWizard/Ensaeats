from Brouillon_Nikiema.metier.adresse import Adresse
class Commande:
    """Constructeur des commandes
    """
    def __init__(self, id_commande: int,
                 date : int,
                 statut_commande: str,
                 liste_menu: list,
                 liste_quantite: list) -> None:
        
        self.id_commande = id_commande
        self.date = date
        self.statut_commande = statut_commande
        self.liste_menu = liste_menu
        self.list_quantite = liste_quantite
        
        
    def prix_total(self):
        """Calcul du prix total
        """
        prix_total = 0
        for menu in self.liste_menu:
            prix_total += menu.prix_menu
            
        return prix_total
    
    def ajout_menu(self, menu):
        self.liste_menu.append(menu)
        
    

