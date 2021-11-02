
class Menu:
    """Constructeur des menus
    """
    def __init__(self, id_menu: int,
                 nom_menu: str,
                 plat: str,
                 boisson: str,
                 dessert: str,
                 prix_menu: float) -> None:
        self.id_menu = id_menu
        self.nom_menu = nom_menu
        self.plat = plat
        self.boisson = boisson
        self.dessert= dessert
        self.prix_menu = prix_menu
        #tu as oublié le dessert
        
    @property
    def id_menu(self):
        return self.id_menu

    @property
    def nom_menu(self):
        return self.nom_menu

    @property
    def plat(self):
        return self.plat

    @property
    def boisson(self):
        return self.boisson

    @property
    def dessert(self):
        return self.dessert

    @property
    def prix_menu(self):
        return self.prix_menu

    # il faudrait réfléchir à des méthodes pour gérer la différentiation des articles en plat,boisson ou dessert, elles seront implémentées dans la DAO
