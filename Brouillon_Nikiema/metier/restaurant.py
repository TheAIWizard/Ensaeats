from Brouillon_Nikiema.metier.adresse import Adresse
from Brouillon_Nikiema.metier.avis import Avis
from Brouillon_Nikiema.metier.menu import Menu
from pydantic.main import BaseModel
class Restaurant (BaseModel) :
    id_restaurant : int
    adresse : Adresse
    nom_restaurant : str
    statut_restaurant : str
    specialite : str
    avis : Avis
    menu : Menu

        
    def ajout_menu(self, menu):
        pass
    
    def enleve_menu(self, menu):
        pass
    
    def ajout_avis(self):
        pass

    