class Article(): 
    def __init__(self, nom : str, composition : str, type : str):
        self.nom = nom
        self.composition = composition
        self.type = type
        self.id_article = 1 
        
    
    def article_desc(self):
        article = {"nom" : self.nom , "type" : self.type, "composition" : self.composition}
        return article 
