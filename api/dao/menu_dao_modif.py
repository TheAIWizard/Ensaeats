from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from API.dao.article_dao import ArticleDao 
from API.metier.menu import Menu

#find_menu_by_id_menu
#creer l'id_menu, définir de manière unique hash(id_menu+id_restaurant)
#get-article_by_id  
#un article peut nepas être encore dans un menu

class MenuDao(metaclass=Singleton):

    #on récupère les id_article pour pouvoir entrer les objets articles en attribut des classes menus
    def find_all_id_article_by_id_menu(id_menu:int) -> List[int]:
        request = "SELECT id_article FROM ensaeats.table_menu_article "\
                  "WHERE id_menu=%(id_menu)s;"
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_menu": id_menu})
                res = cursor.fetchall()
        id_articles = []
        if res :
            for row in res :
                id_articles.append(row["id_article"])
        return id_articles

    #on en déduit la liste des objets articles pour un id_menu donné par la méthode "find_article_by_id_article" de la classe ArticleDao
    def find_all_article_by_id_menu(id_menu:int):
        return [ArticleDao.find_article_by_id_article(id_article) for id_article in MenuDao.find_all_id_article_by_id_menu(id_menu)]

    def find_all_menus(limit:int=0, offest:int=0) -> List[Menu]:
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
                id_menu = row["id_menu"]
                liste_articles_menu=MenuDao.find_all_article_by_id_menu(id_menu)  
                menu = Menu(
                      nom=row['nom']
                    , prix=row["prix"]
                    , article1=liste_articles_menu[0]
                    , article2=liste_articles_menu[1]
                    , article3=liste_articles_menu[2]
                )
                menus.append(menu)
        return menus

    """ pour agréger : SELECT city, STRING_AGG(email,';') WITHIN GROUP (ORDER BY email) email_list FROM sales.customers GROUP BY city; """

    def find_all_menus_by_id_restaurant(id_restaurant:int) -> List[Menu]:
        """
        Get all menu of a specific restaurant with the given id

        :param id_menu: The menu id
        :type id_menu: int
        """
        request = "SELECT * FROM ensaeats.menu "\
                  "JOIN ensaeats.table_restaurant_menu USING(id_menu) "\
                  "WHERE id_restaurant=%(id_restaurant)s;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_restaurant": id_restaurant}
                )
                res = cursor.fetchall()
        menus = []
        if res :
            for row in res :
                id_menu = row["id_menu"]
                liste_articles_menu=MenuDao.find_all_article_by_id_menu(id_menu)  
                menu = Menu(
                      nom=row['nom']
                    , prix=row["prix"]
                    , article1=liste_articles_menu[0]
                    , article2=liste_articles_menu[1]
                    , article3=liste_articles_menu[2]
                )
                menus.append(menu)
        return menus

    def find_menu_by_id_menu(id_menu:int) -> Menu:
        """
        Get a menu with the given id_menu

        :param id_menu: The menu id
        :type id_menu: int
        """
        request = "SELECT * FROM ensaeats.menu "\
                  "WHERE id_menu=%(id_menu)s;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_menu": id_menu}
                )
                res = cursor.fetchall()
        menus = []
        if res :
            for row in res :
                id_menu = row["id_menu"]
                liste_articles_menu=MenuDao.find_all_article_by_id_menu(id_menu)  
                menu = Menu(
                      nom=row['nom']
                    , prix=row["prix"]
                    , article1=liste_articles_menu[0]
                    , article2=liste_articles_menu[1]
                    , article3=liste_articles_menu[2]
                )
                menus.append(menu)
        return menus[0]


    def add_menu(menu : Menu) -> bool: # ajout id_restaurant
        created = False
    #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.menu (id_menu, nom,"\
                    " prix) VALUES "\
                    "(%(id_menu)s, %(nom)s, %(prix)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                  , "nom": menu.nom
                  , "prix": menu.prix})
                res = cursor.fetchone()
        if res :
            created = True
        return created

    def add_menu_by_id_restaurant(menu : Menu, id_restaurant:int) -> bool:
        created_menu,created_restaurant_menu = False,False
        #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.menu (id_menu, nom,"\
                    " prix) VALUES "\
                    "(%(id_menu)s, %(nom)s, %(prix)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                  , "nom": menu.nom
                  , "prix": menu.prix})
                res = cursor.fetchone()
        if res :
            created_menu = True
        # ajout du couple (id_menu, id_restaurant) dans la table table_restaurant_menu
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.table_restaurant_menu (id,id_menu,"\
                    " id_restaurant) VALUES "\
                    "(0,%(id_menu)s, %(id_restaurant)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                , "id_restaurant": id_restaurant})
                res = cursor.fetchone()
        if res :
            created_restaurant_menu = True
        
        return created_menu,created_restaurant_menu

    def delete_menu(menu : Menu) -> bool:
        deleted_menu,deleted_restaurant_menu,deleted_menu_article = False,False,False
        #suppression du menu dans la table table_restaurant_menu
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_restaurant_menu "\
                    "WHERE id_menu=%(id_menu)s"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
        if res :
            deleted_restaurant_menu = True
        #suppression de l'id_menu dans la table table_menu_article
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.table_menu_article "\
                    "WHERE id_menu=%(id_menu)s"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
        if res :
            deleted_menu_article = True
        #suppression du menu dans la table menu
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.menu "\
                    "WHERE id_menu=%(id_menu)s"\
                    "RETURNING id_menu;"\
                , {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
        if res :
            deleted_menu = True
        return deleted_menu,deleted_restaurant_menu,deleted_menu_article

    def update_menu(menu:Menu)-> bool: # id_retaurant,ancien identifiant, add_menu,delete_menu)
        updated_menu,updated_restaurant_menu = False, False
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.menu SET" \
                    " nom = %(nom)s,"\
                    " prix = %(prix)s "\
                    "WHERE id_menu=%(id_menu)s;"
                , {"id_menu" : menu.id_menu
                  , "nom": menu.nom
                  , "prix": menu.prix})
                if cursor.rowcount :
                    updated_menu = True
        # modification du couple (id_menu, id_restaurant) dans la table table_restaurant_menu
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.table_restaurant_menu SET" \
                    " id_menu = %(id_menu)s "\
                    "WHERE id_menu=%(id_menu)s;"
                , {"id_menu" : menu.id_menu})
                if cursor.rowcount :
                    updated_restaurant_menu = True
        return updated_menu,updated_restaurant_menu

      