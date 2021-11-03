from API.metier.article import Article

class ArticleDao:

    def __init__(self):
        pass

    def get_article_by_id(self, id_article) -> Article:
        ''' Recupère l'article par l'identifiant '''
        pass

    
    def update_article(self, article, id_article_ancien):
        ''' Supprime la ligne avec l'id article ancien et ajouter l'article dans la base de données '''
        pass

    def add_article(self, article):
        ''' Ajoute un article à la base de données'''
        pass