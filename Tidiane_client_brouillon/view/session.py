from brouillon.metier.commande import Commande
from brouillon.metier.menu import Menu
from brouillon.metier.commande import Commande
from brouillon.metier.restaurant import Restaurant
from brouillon.utils.singleton import Singleton


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
        
        self.nouveau_client = None
        self.id_client = None
        self.identifiant = None
        self.mot_de_passe = None
        self.nom = None
        self.prenom = None
        self.adresse = None
        self.create_identifiant = None
        self.create_mot_de_passe = None
        self.create_telephone = None
        
        self.listeAvis = []
        
        