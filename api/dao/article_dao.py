from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from API.metier.article import Article
#find_menu_by_id_menu
#creer l'id_menu, définir de manière unique hash(id_menu+id_restaurant)
#get-article_by_id  

class ArticleDao(metaclass=Singleton):

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
                article = Article(
                      id_article = row["id_article"]
                    , nom=row['nom']
                    , type_article=row["type_article"]
                    , composition=row["composition"]
                )
                articles.append(article)
        return articles[0]

    def add_article(article : Article) -> bool: 
        #on peut ajouter un article même s'il n'est pas encore dans un menu
        created = False
        #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.article (id_article, nom,"\
                    " type_article, composition) VALUES "\
                    "(%(id_article)s, %(nom)s, %(type_article)s, %(composition)s)"\
                    "RETURNING id_article;"
                , {"id_article" : article.id_article
                  , "nom": article.nom
                  , "type_article": article.type
                  , "composition": article.composition})
                res = cursor.fetchone()
        if res :
            created = True
        return created
        
    def update_article(article:Article, id_article_ancien):
        ''' Supprime la ligne avec l'id article ancien et ajouter l'article dans la base de données '''
        deleted_menu_article,deleted_article = False,False
        #suppression de id_article_ancien dans la table table_menu_article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_menu_article "\
                    "WHERE id_article=%(id_article_ancien)s"\
                    "RETURNING id_article;"
                , {"id_article" : id_article_ancien})
                res = cursor.fetchone()
        if res :
            deleted_menu_article = True
        #suppression de id_article_ancien dans la table article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.article"\
                    "WHERE id_article=%(id_article_ancien)s"\
                    "RETURNING id_menu;"\
                , {"id_article" : id_article_ancien})
                res = cursor.fetchone()
        if res :
            deleted_article = True
        #vérification réussite suppression
        print("suppression dans table menu_article :"+str(deleted_menu_article),"suppression dans table article :"+str(deleted_article))
        #ajout de l'article dans la base de donnée
        return ArticleDao.add_article(article)