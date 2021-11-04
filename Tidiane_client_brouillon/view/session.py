from Tidiane_client_brouillon.view.abstract_view import AbstractView
from brouillon.metier.commande import Commande
from brouillon.metier.menu import Menu
from brouillon.metier.commande import Commande
from brouillon.metier.restaurant import Restaurant


class Session(AbstractView):
    def __init__(self) -> None:
        """[Defini les objets que l'on stocke en session]
        """
        self.restaurant_actif : Restaurant = None 
        self.menu_actif : Menu = None
        self.commande_active : Commande = None
        self.localite = None
        self.nom_restaurant = None
        self.radius = None
        
        
        