from Brouillon_Nikiema.metier.menu import Menu 
from pydantic import BaseModel
from Brouillon_Nikiema.metier.adresse import Adresse
class Commande:
    """Constructeur des commandes
    """

class Commande (BaseModel):
    id_commande : int
    date : str
    #paiement : float
    statut_commande : str
    liste_menu : list
    liste_quantite : list
        
    def prix_total(self):
        """Calcul du prix total
        """
        prix_total = 0
        for menu in self.liste_menu:
            prix_total += menu.prix_menu
            
        return prix_total
    
    def ajout_menu(self, menu):
        self.liste_menu.append(menu)
        
    

