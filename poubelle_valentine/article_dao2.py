from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from API.metier.article import Article

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
                res = cursor.fetchall()
        articles = []
        if res :
            for row in res :
                article = Article(nom=row['nom']
                    , type=row["type_article"]
                    , composition=row["composition"]
                )
                articles.append(article)
        return articles[0]

    @staticmethod
    def add_article(article : Article) -> bool: 
        #on peut ajouter un article même s'il n'est pas encore dans un menu
        created = False
        #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.article (id_article, nom,"\
                    " type_article, composition) VALUES "\
                    "(0, %(nom)s, %(type_article)s, %(composition)s)"\
                    "RETURNING id_article;"
                , { "nom": article.nom
                  , "type_article": article.type
                  , "composition": article.composition})
                res = cursor.fetchone()
        if res :
            created = True
        return created
    
    @staticmethod
    def update_article(id_article_ancien, article:Article):
        ''' Supprime la ligne avec l'id article ancien et ajouter l'article dans la base de données '''
        update_article = False 

        # Update dans la base de données des informations de l'article 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.article "\
                    " SET id_article=%(id_article)s,"\
                    "  nom = %(nom)s, "\
                    "  type_article = %(type)s, "\
                    "  composition = %(composition)s, "\
                    "  WHERE id_article = %(id_article)s ;"

                , {"id_article" : id_article_ancien})
                res = cursor.fetchone()
        if res :
            update_article = True

        #suppression de id_article_ancien dans la table table_menu_article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_menu_article "\
                    " WHERE id_article=%(id_article)s"\
                    " RETURNING id_article;"
                , {"id_article" : id_article_ancien})
                res = cursor.fetchone()
        if res :
            deleted_menu_article = True

        #suppression de id_article_ancien dans la table article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.article"\
                    " WHERE id_article=%(id_article)s"\
                    " RETURNING id_article;"
                , {"id_article" : id_article_ancien})
                res = cursor.fetchone()
        if res :
            deleted_article = True
        #vérification réussite suppression
        print("suppression dans table menu_article :"+str(deleted_menu_article),"suppression dans table article :"+str(deleted_article))
        #ajout de l'article dans la base de donnée
        return ArticleDao.add_article(article)

    @staticmethod
    def delete_article(article : Article) -> bool: 
        #on peut ajouter un article même s'il n'est pas encore dans un menu
        deleted_article,deleted_menu_article = False, False
        #supprimer son id_article de la table table_menu_article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_menu_article"\
                    " WHERE id_article=%(id_article)s"\
                    " RETURNING id_article;"
                , {"id_article" : article.id_article})
                res = cursor.fetchone()
        if res :
            deleted_menu_article = True
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