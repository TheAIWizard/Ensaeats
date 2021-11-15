from brouillon.metier.commande import Commande
from api_minuscule.metier.menu import Menu
from brouillon.metier.commande import Commande
from api_minuscule.metier.restaurant import Restaurant
from api_minuscule.utils.singleton import Singleton


class Session(metaclass=Singleton):
    def __init__(self) -> None:
        """[Defini les objets que l'on stocke en session]
        """
        self.restaurant_actif : Restaurant = None 
        self.menu_actif : Menu = None
        self.quantite = None
        self.list_menu = []
        self.list_quantite = []
        self.commande_active : Commande = None
        self.localite = None
        self.nom_restaurant = None
        self.radius = None
        
        
        
        