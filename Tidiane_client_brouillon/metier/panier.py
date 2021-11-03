### Ensemble de menu:

### Contient une méthode qui renvoie le prix total (prix_total)

### Attribut liste des menus 

from brouillon.metier.menu import Menu  

class Panier:
    def __init__(self, list_menu) -> None:
        self.list_menu = list_menu
        
        
    def calcul_total(self):
        prix_total = 0
        for menu in self.list_menu:
            prix_total += menu.prix_menu
            
        return prix_total