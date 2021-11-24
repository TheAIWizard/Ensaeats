from pydantic import BaseModel

class Article(BaseModel): 
    """
    La classe Article permet de definir un article d'un restaurant

    Atributes
    ---------
    id_article : int
                Permet d'identifier 

    nom        : str
              Le nom de notre article. Le nom permet de reconnître nôtre article

    composition : str
                contient tout les ingrédients de l'article

    type        : str 
                le type faire reférence soit au dessert, soit au plat ou la boisson
    Méthode :
    -------
    article_desc() :
                Permet d'afficher notre Article

    """
    id_article:int
    nom:str
    composition:str        
    type:str 
    
    def article_desc(self):
        article = {"nom" : self.nom , "type" : self.type, "composition" : self.composition}
        return article 

