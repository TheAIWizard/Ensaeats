from pydantic import BaseModel
from api.metier.article import Article

class Menu(BaseModel): 
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
    article1 : Article
    article2 : Article
    article3 : Article
    
    
    def recup_menu(self): 
        ''' grâce aux id article on peut récupérer les compositions et type d'articles '''
        menu = {"article1" : self.article1.article_desc(),"article2" : self.article2.article_desc(), "article3": self.article3.articledesc()}


    def __str__(self) -> str:
        output = self.nom
        output += "\n"
        output += "**    Article1: "
        output += self.article1.nom
        output += "\n"
        output += "**    Article2: "
        output += self.article2.nom
        output += "\n"
        output += "**    Article3: "
        output += self.article3.nom
        output += "\n"
        output += "**    Prix du menu: "
        output += str(self.prix)
        
        return output