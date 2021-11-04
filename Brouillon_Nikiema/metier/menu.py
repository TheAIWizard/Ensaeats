from Brouillon_Nikiema.metier.article import Article
from pydantic import BaseModel

class Menu (BaseModel) :
    id_menu : int
    nom_menu : str
    plat : str
    dessert : str
    boisson : str
    prix_menu : float
    article : Article

    