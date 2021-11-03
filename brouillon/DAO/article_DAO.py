from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from brouillon.metier.article import Article
#find_menu_by_id_menu
#creer l'id_menu, définir de manière unique hash(id_menu+id_restaurant)
#get-article_by_id  
#un article peut nepas être encore dans un menu
class ArticleDao(metaclass=Singleton):
    def find_all_articles(self, limit:int=0, offest:int=0) -> List[Article]:
        """
        Get all menu in the db without any filter

        :param limit: how many menu are requested
        :type limit: int
        :param offest: the offset of the request
        :type offest: int
        """
        request= "SELECT * FROM ensaeats.menu;"
        if limit :
            request+=f"LIMIT {limit}"
        if offest :
            request+=f"OFFSET {offest}"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request
                )
                res = cursor.fetchall()
        menus = []
        if res :
            for row in res :
                menu = Menu(
                      id_menu = row["id_menu"]
                    , nom_menu=row['nom']
                    , prix_menu=row["prix"]
                )
                menus.append(menu)
        return menus
