from Brouillon_Nikiema.metier.article import Article
class Menu :
    def __init__(self, id_menu : int, nom_menu : str, plat : str,
        dessert : str, boisson : str, prix_menu : float, 
        article : Article) -> None :
        self.id_menu=id_menu
        self.nom_menu=nom_menu
        self.plat=plat
        self.dessert=dessert
        self.boisson=boisson
        self.prix_menu=prix_menu
        self.article=article

   