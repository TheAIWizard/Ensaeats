
""" class Article:
    Constructeur des articles qui composent les menus
    def __init__(self, id_article: int,
                 type_article: str,
                 nom_article: str) -> None:
        self.id_article = id_article
        self.type_article = type_article
        self.nom_article = nom_article """
        
        
class Article(): 
    def __init__(self, nom : str, composition : str, type : str):
        self.nom = nom
        self.composition = composition
        self.type = type
        self.id_article = 5687693
    
    def article_desc(self):
        article = {"nom" : self.nom , "type" : self.type, "composition" : self.composition}
        return article 
        