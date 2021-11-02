
class Article:
    """Constructeur des articles qui composent les menus
    """
    def __init__(self, id_article: int,
                 type_article: str,
                 nom_article: str) -> None:
        self.id_article = id_article
        self.type_article = type_article
        self.nom_article = nom_article
        
        
        
        