from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from brouillon.metier.article import Article
#find_menu_by_id_menu
#creer l'id_menu, définir de manière unique hash(id_menu+id_restaurant)
#get-article_by_id  
#un article peut nepas être encore dans un menu
class ArticleDao(metaclass=Singleton):
    def find_menu_by_id_menu(self,id_article:int) -> Article:
        """
        Get an article with the given id_article

        :param id_menu: The menu id
        :type id_menu: int
        """
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
                      id_menu = row["id_menu"]
                    , nom_menu=row['nom']
                    , prix_menu=row["prix"]
                )
                articles.append(Article)
        return articles[0]

