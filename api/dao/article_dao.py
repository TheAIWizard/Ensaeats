from typing import List, Optional
from api.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.metier.article import Article
from api.dao.menu_dao import MenuDao 

class ArticleDao:

    """
    La classe ArticleDao permet d'inserer ou de recuperer des article dans la table article de notre  base de donnée. Cette classe joue un 
    rêle très important dans le projet. 


    Méthodes
    ---------
    find_article_by_id_article (id_article):
        retourne un  article

    add_article (article):
        retourne True si un article est ajouté à la table article de la base de donnée sinon False 

    update_article (article):
        retourne True si un article est modifié à la table article de la base de donnée sinon False 

    get_article ():
        retourne un eliste d'article 
    
    delete_article (article):
        retourne True si un article est supprimé sinon False

    
    """
    @staticmethod
    def find_article_by_id_article(id_article:int) -> Article:
        """
        find_article_by_id_article (id_article):
            Cette méthode nrecupère des des articles par identifiant dans la base de données

            Atttributes
            ----------
            id_article : int

            return : Article
            
        """
        
        request = "SELECT * FROM ensaeats.article "\
                  "WHERE id_article=%(id_article)s;"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_article": id_article}
                )
                res = cursor.fetchone()
        articles = []
        if res:
            return Article(id_article=res["id_article"], nom=res["nom"], type=res["type_article"], composition=res["composition"])
        

    @staticmethod
    def add_article(article : Article) -> bool: 

        """
        Cette fonction permet l'insertion de nouveau article dans la table article de notre base de donnée

        Attributes :
        -----------
        article : Article
        
            Return : Bool
        """
        created = False
        #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.article (nom,"\
                    " type_article, composition) VALUES "\
                    "(%(nom)s, %(type_article)s, %(composition)s)"\
                    "RETURNING id_article;"
                , { "nom": article.nom
                  , "type_article": article.type
                  , "composition": article.composition})
                res = cursor.fetchone()
        if res :
            created = True
            article.id_article = res['id_article']
        return created

    @staticmethod
    def update_article(article:Article):
        """
        Cette méthode permet de modifier un article dans latable article de la base de donnée

        Attribute:
        ----------
        article : Article

        return : bool
        """
        
        update_article = False 

        # Update dans la base de données des informations de l'article 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    " UPDATE ensaeats.article" \
                    " SET nom = %(nom)s, " \
                    " type_article = %(type)s, "\
                    " composition = %(composition)s "\
                    "WHERE id_article = %(id_article)s "\
                    "RETURNING * ; "
                    , {"nom" : article.nom
                    , "type" : article.type
                    , "composition" : article.composition
                    , "id_article" : article.id_article})   
                res = cursor.fetchone()
            if res : 
                return res
            
                
    @staticmethod 
        
    def get_articles() -> List[Article] : 
        """
        Cette fonction nous permet de recupèrer des article dans la base de donnée

        Attribute:
        --------
        
        return : List[Article]
        """
        with DBConnection().connection as connection : 
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * FROM ensaeats.article" )
                res = cursor.fetchall 
        if res : 
            return res 
           
    @staticmethod
    def delete_article(article : Article) -> Article : 
        """
        Cette fonction permet de supprimer un article

        Attribute:
        article : Article

        return bool
        """
        #on peut ajouter un article même s'il n'est pas encore dans un menu
        deleted_article,deleted_menu_article = False, False
        #supprimer son id_article de la table table_menu_article

        # Recuperer id des menus + supprimer menu + supprimer table menu article 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_menu_article"\
                    " WHERE id_article=%(id_article)s"\
                    " RETURNING id_menu;"
                , {"id_article" : article.id_article})
                res = cursor.fetchone()
        if res :
            deleted_menu_article = True
            MenuDao.MenuDao.delete_menu(MenuDao.find_menu_by_id_menu())

        #supprimer son id_article de la table article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.article"\
                    " WHERE id_article=%(id_article)s"\
                    " RETURNING id_article;"
                , {"id_article" : article.id_article})
                res = cursor.fetchone()
        if res :
            deleted_article = True
        return deleted_article,deleted_menu_article
