
from Brouillon_Nikiema.metier.article import Article
from pydantic import BaseModel

class Menu (BaseModel) :
    id_menu : int
    nom_menu : str
    plat : Article
    dessert : Article
    boisson : Article
    prix_menu : float

        
    

