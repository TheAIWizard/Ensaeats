from Brouillon_Nikiema.metier.adresse import Adresse
from pydantic.main import BaseModel
class Restaurant (BaseModel) :
    id_restau : int
    adresse : Adresse
    nom_restau : str
    statut_restau : str
    specialite : str
    
    
    def ajout_menu(self, menu):
        pass
    
    def enleve_menu(self, menu):
        pass
    
    def ajout_avis(self):
        pass