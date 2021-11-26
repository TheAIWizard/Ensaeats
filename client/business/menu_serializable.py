from pydantic import BaseModel
from client.business.article import Article

class Menu_serializable(BaseModel): 
    """
    Cette classe nous permet de definir un menu pour notre client

    Attribute
    --------
    id_menu : int 
            Identoifiant du menu

    nom_menu : str
            Nom du menu

    article1 : article
             soit le plat ou la boisson ou le dessert

    article2 : article
              soit le plat ou la boisson ou le dessert

    article 3 : article
              soit le plat ou la boisson ou le dessert

    Méthodes
    ------
    recup_menu()
        Permet d'affichier un menu

        return : menu
        Elle retourne un menu
    """
    id_menu : int 
    nom : str
    prix : int
    article1 : dict
    article2 : dict
    article3 : dict