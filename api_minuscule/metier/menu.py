from pydantic import BaseModel
from api_minuscule.metier.article import Article

class Menu(BaseModel): 
    id_menu : int 
    nom : str
    prix : int
    article1 : Article
    article2 : Article
    article3 : Article
    
    
    def recup_menu(self): 
        ''' grâce aux id article on peut récupérer les compositions et type d'articles '''
        menu = {"article1" : self.article1.article_desc(),"article2" : self.article2.article_desc(), "article3": self.article3.articledesc()}
