from API.metier.article import Article

class Menu(): 
    def __init__(self, nom : str, prix : int, article1 : Article, article2 : Article, article3 : Article): 
        self.nom = nom
        self.prix = prix 
        self.article1 = article1
        self.article2 = article2
        self.article3 = article3
        self.id_menu = 1 
        # appel à add_menu -> recupere l'id 
    
    def recup_menu(self): 
        ''' grâce aux id article on peut récupérer les compositions et type d'articles '''
        menu = {"article1" : self.article1.article_desc(),"article2" : self.article2.article_desc(), "article3": self.article3.articledesc()}
