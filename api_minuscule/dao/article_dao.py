from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from api_minuscule.metier.article import Article
#from API.dao.menu_dao import MenuDao

class ArticleDao:

    @staticmethod
    def find_article_by_id_article(id_article:int) -> Article:
        ''' Recupère l'article par l'identifiant '''

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
        #on peut ajouter un article même s'il n'est pas encore dans un menu
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
        ''' Modification de l'article '''
        update_article = False 

        # Update dans la base de données des informations de l'article 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    " UPDATE ensaeats.article" \
                    " SET nom = %(nom)s, " \
                    " type_article = %(type)s, "\
                    " composition = %(composition)s "\
                    "WHERE id_article = %(id_article)s ;"
                    , {"nom" : article.nom
                    , "type" : article.type
                    , "composition" : article.composition
                    , "id_article" : article.id_article})
                

    @staticmethod
    def delete_article(article : Article) -> Article : 
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
            MenuDao.delete_menu(MenuDao.find_menu_by_id_menu())

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