from API.metier.article import Article

class Menu(): 
    def __init__(self, nom : str, prix : int, id_article1 : int, id_article2 : int, id_article3 : int): 
        self.nom = nom
        self.id_article1 = id_article1
        self.id_article2 = id_article2
        self.id_article3 = id_article3
    