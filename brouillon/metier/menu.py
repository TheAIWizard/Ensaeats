
from Brouillon_Nikiema.metier.article import Article
from pydantic import BaseModel

class Menu (BaseModel) :
    id_menu : int
    nom : str
    plat : Article
    dessert : Article
    boisson : Article
    prix : float

        
    

