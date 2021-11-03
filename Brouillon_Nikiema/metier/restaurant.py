from Brouillon_Nikiema.metier.adresse import Adresse
from Brouillon_Nikiema.metier.avis import Avis
from Brouillon_Nikiema.metier.menu import Menu
class Restaurant :
    """Constructeur des restaurants
    Nous avons mis le type de l'attribute statut_restauarant en str 
    """
    
    def __init__(self, id_restau : int, adresse : Adresse,
                 nom_restau : str,
                 statut_restau : str,
                 specialite : str,
                 avis : Avis,
                 menu : Menu) -> None:
        self.id_restaurant = id_restau
        self.nom_restaurant = nom_restau
        self.statut_restaurant = statut_restau
        self.specialite = specialite
        self.adresse=adresse
        self.avis=avis
        self.menu=menu
        
    def ajout_menu(self, menu):
        pass
    
    def enleve_menu(self, menu):
        pass
    
    def ajout_avis(self):
        pass

    def str(self):
           
        return "{} {} {} {} {} {} {}".format(str(self.id_restaurant),
        str(self.nom_restaurant), str(self.statut_restaurant), str(self.specialite),
        str(self.test_adresse.affiche()),str(self.test_avis.affiche()),str(self.test_menu.affiche()))

    def affiche(self):
        print(self.str())