from pydantic import BaseModel

class Article(BaseModel): 
    id_article:int
    nom:str
    composition:str        
    type:str 
    
    def article_desc(self):
        article = {"nom" : self.nom , "type" : self.type, "composition" : self.composition}
        return article 

