from client.business.commande import Commande
from client.business.menu import Menu
from client.business.commande import Commande
from client.business.restaurant import Restaurant
from client.utils.singleton import Singleton


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
        
        self.client = None
        self.nouveau_client = None
        self.id_client = None
        self.identifiant = None
        self.mot_de_passe = None
        self.nom = None
        self.prenom = None
        self.adresse = None
        self.telephone = None
        self.term = None
        self.radius = None
        
        self.listeAvis = []
        
        