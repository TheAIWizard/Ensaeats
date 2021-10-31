from typing import List, Optional
from utils.singleton import Singleton
from DAO.db_connection import DBConnection
from metier.menu import Menu
from metier.article import Article

class MenuDao(metaclass=Singleton):
    def find_all_menus(self, limit:int=0, offest:int=0) -> List[Menu]:
        """
        Get all menu in the db without any filter

        :param limit: how many menu are requested
        :type limit: int
        :param offest: the offset of the request
        :type offest: int
        """
        request = "SELECT * FROM ensaeats.menu"
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
                    #, plat=row['attack_name'] faire un lien avec menu.article
                    #, boisson=row['attack_description'] et dessert alors?
                    , prix=row["prix"]
                )
                menus.append(menu)
        return menus

    def find_all_menus_by_id_restaurant(self,id_restaurant:int) -> List[Menu]:
        """
        Get all menu of a specific restaurant with the given id

        :param id_menu: The menu id
        :type id_menu: int
        """
        request = "SELECT * FROM ensaeats.menu JOIN ensaeats.table_restaurant_menu USING(id_menu)"\
                  "JOIN ensaeats.restaurant USING(id_restaurant)"\
                  "WHERE id_restaurant=%(id_restaurant)s"

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
                menu = Menu(
                      id_menu = row["id_menu"]
                    , nom_menu=row['nom']
                    #, plat=row['attack_name'] faire un lien avec menu.article
                    #, boisson=row['attack_description'] et dessert alors?
                    , prix=row["prix"]
                )
                menus.append(menu)
        return menus


    def add_menu(self, menu : Menu) -> bool:
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.menu (id_menu, nom,"\
                    " prix) VALUES "\
                    "(%(id_menu)s, %(nom)s, %(prix)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                  , "name": menu.nom
                  , "prix": menu.prix})
                res = cursor.fetchone()
        if res :
            menu.id=res['id_menu']
            created = True
        return created

    def delete_menu(self, menu : Menu) -> bool:
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "DELETE FROM ensaeats.menu "\
                    "WHERE id_menu=%(id_menu)s"\
                    "DELETE FROM ensaeats.table_restaurant_menu "\
                    "WHERE id_menu=%(id_menu)s"
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
        if res :
            menu.id=res['id_menu']
            created = True
        return created

    def update_menu(self, menu:Menu)-> bool:
        updated = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "UPDATE ensaeats.menu SET" \
                    " id_menu = %(id_menu)s"\
                    ", nom = %(nom)s"\
                    ", prix = %(prix)s"
                , {"id_menu" : menu.id_menu
                  , "nom": menu.nom
                  , "prix": menu.prix})
                if cursor.rowcount :
                    updated = True
        return updated
