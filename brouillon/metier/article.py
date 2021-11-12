
""" class Article:
    Constructeur des articles qui composent les menus
    def __init__(self, id_article: int,
                 type_article: str,
                 nom_article: str) -> None:
        self.id_article = id_article
        self.type_article = type_article
        self.nom_article = nom_article """
        
from pydantic import BaseModel

class Article(): 
    id_article : int
    nom_article : str
    type_article : str
    
    def article_desc(self):
        article = {"nom" : self.nom , "type" : self.type, "composition" : self.composition}
        return article 
        