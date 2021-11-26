from typing import List, Optional
#from brouillon.utils.singleton import Singleton
from api.dao.db_connection import DBConnection
from api.metier.menu import Menu
import api.dao.article_dao as ArticleDao

#find_menu_by_id_menu
#creer l'id_menu, définir de manière unique hash(id_menu+id_restaurant)
#get-article_by_id  
#un article peut nepas être encore dans un menu

class MenuDao():
    """
    Cette classe nous permet de recupèrer et inserer des menu dans notre base de données

    Methodes:
    --------
    find_all_id_article_by_id_menu(id_menu):
        retourne une liste des identifiant des menus 

    get_id_restaurant_by_menu(menu : Menu)
        retourne l'identifiant d'un restaurant

    get_id_restaurant_by_id_menu(id_menu )
         retourne l'identifiant d'un restaurant

     find_all_menus(limit, offest)
        retourne la liste des menus

    find_all_menus_by_id_restaurant(id_restaurant):
        retoune une liste de restaurant

    find_menu_by_id_menu(id_menu):
        retourne un menu

    add_menu(menu : Menu):
        retourne vrai si le menu est ajouté sinon faux

    add_menu_by_id_restaurant(menu , id_restaurant):
        retourne vrai si le menu est ajouté sinon faux

    delete_menu(menu : Menu):
        retourne vrai si un menu est supprimé sion faux
    """
    
    @staticmethod
    #on récupère les id_article pour pouvoir entrer les objets articles en attribut des classes menus
    def find_all_id_article_by_id_menu(id_menu:int) -> List[int]:
        """
        Cette fonction nous permet de recupèrer les identifiant des menus dans la base de données

        Attribute :
        ---------
        id_menu:int

        return id_menu
        """
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

    @staticmethod 
    def get_id_restaurant_by_menu(menu : Menu) -> str: 
        """
        cette fonction sert à trouver les menu associés au restauarant

        Attribute :
        -----------
        menu : menu

        return : str
        """
        with DBConnection().connection as connection : 
            with connection.cursor() as cursor : 
                cursor.execute(
                    "SELECT id_restaurant FROM ensaeats.table_restaurant_menu"\
                    " WHERE id_menu = %(id_menu)s ;",
                    {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
        if res : 
            return res['id_restaurant']
    
    @staticmethod 
    def get_id_restaurant_by_id_menu(id_menu : int) -> str: 
        """
        cette fonction sert à trouver les identifiant associés au restauarant

        Attribute :
        -----------
        id_menu : int

        return : str
        """
        with DBConnection().connection as connection : 
            with connection.cursor() as cursor : 
                cursor.execute(
                    "SELECT id_restaurant FROM ensaeats.table_restaurant_menu"\
                    " WHERE id_menu = %(id_menu)s ;",
                    {"id_menu" : id_menu})
                res = cursor.fetchone()
        if res : 
            return res['id_restaurant']
        
        
    @staticmethod
    #on en déduit la liste des objets articles pour un id_menu donné par la méthode "find_article_by_id_article" de la classe ArticleDao
    def find_all_article_by_id_menu(id_menu:int):
        return [ArticleDao.ArticleDao.find_article_by_id_article(id_article) for id_article in MenuDao.find_all_id_article_by_id_menu(id_menu)]

    @staticmethod
    def find_all_menus(limit:int=0, offest:int=0) -> List[Menu]:
        """
        cette foinction permet d'obtenir tous les menus dans la base de données sans les filtrer

        Attribute :
        ----------
        limit:int
        offest:int

        return : list
       
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

    @staticmethod
    def find_all_menus_by_id_restaurant(id_restaurant:int) -> List[Menu]:
        """
        Cette fonction permet de recuperer les restaurant selon un id

        Attribute :
        ----------
        id_restaurant:int

        return : list
        
        """
        request = "SELECT * FROM ensaeats.menu "\
                  "JOIN ensaeats.table_restaurant_menu USING(id_menu) "\
                  "WHERE table_restaurant_menu.id_restaurant=%(id_restaurant)s;"

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
                    id_menu = row['id_menu']
                    , nom=row['nom']
                    , prix=row["prix"]
                    , article1=liste_articles_menu[0]
                    , article2=liste_articles_menu[1]
                    , article3=liste_articles_menu[2]
                )
                menus.append(menu)
        return menus

    @staticmethod
    def find_menu_by_id_menu(id_menu:int) -> Menu:
        """
        Trouver un menu selon son id_menu:int

        Attribute :
        ---------
        id_menu:int
        return : menu

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

    @staticmethod
    def add_menu(menu : Menu) -> bool:
        """
        Cette fonction permet d'ajouter un menu dans la table menu de la base de donnée

        Attribute :
        ----------
        menu : Menu

        return : bool
        """
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

    @staticmethod
    def add_menu_by_id_restaurant(menu : Menu, id_restaurant:str) -> bool:
        """
        ajouter un menu a un restaurant 

        Attribute :
        ----------
        menu : Menu
        id_restaurant:str

        return : bool
        """
        created_menu,created_restaurant_menu, created_menu_article_1, created_menu_article_2, created_menu_article_3 = False,False,False,False, False
        #rajouter identification restaurateur
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    " INSERT INTO ensaeats.menu (nom,"\
                    " prix) VALUES "\
                    "(%(nom)s, %(prix)s)"\
                    "RETURNING id_menu;"
                , {"nom": menu.nom
                  , "prix": menu.prix})
                res = cursor.fetchone()
        if res :
            menu.id_menu = res['id_menu']
            created_menu = True

        
        # ajout du couple (id_menu, id_article) dans la table table_article_menu

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                    " id_article) VALUES "\
                    "(%(id_menu)s, %(id_article)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                , "id_article": menu.article1.id_article})
                res = cursor.fetchone()
            if res :
                created_menu_article_1 = True
        

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                    " id_article) VALUES "\
                    "(%(id_menu)s, %(id_article)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                , "id_article": menu.article2.id_article})
                res = cursor.fetchone()
            if res :
                created_menu_article_2 = True

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                    " id_article) VALUES "\
                    "(%(id_menu)s, %(id_article)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                , "id_article": menu.article3.id_article})
                res = cursor.fetchone()
            if res :
                created_menu_article_3 = True

        
        # ajout du couple (id_menu, id_restaurant) dans la table table_restaurant_menu
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.table_restaurant_menu (id_menu,"\
                    " id_restaurant) VALUES "\
                    "(%(id_menu)s, %(id_restaurant)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                , "id_restaurant": id_restaurant})
                res = cursor.fetchone()
        if res :
            created_restaurant_menu = True 

        return created_menu,created_restaurant_menu, created_menu_article_1, created_menu_article_2, created_menu_article_3
        
  
    @staticmethod
    def delete_menu(menu : Menu) -> bool:

        """
        Cette fonction permet de supprimer un menu dans la table menu

        Attribute :
        -----------
        menu : menu

        return : bool
        """
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

    @staticmethod
    def update_menu(menu:Menu)-> Menu :
        
        updated_menu = False
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


        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_article FROM ensaeats.table_menu_article " \
                    "WHERE id_menu=%(id_menu)s;"
                , {"id_menu" : menu.id_menu})
                res = cursor.fetchone()
                
        if res : 
            # voir si les identifiants des articles ont changé 
            if menu.article1.id_article not in res : 
                update_article1 = False
                ArticleDao.ArticleDao.add_article(article = menu.article1)
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "DELETE FROM ensaeats.table_menu_article " 
                            "WHERE id_menu=%(id_menu)s AND id_article = %(id_article)s;"
                                , {"id_menu" : menu.id_menu, 
                                "id_article" : menu.article1.id_article})
                            
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                                " id_article) VALUES "\
                                "(%(id_menu)s, %(id_article)s)"\
                                "RETURNING id_menu;"
                                , {"id_menu" : menu.id_menu,
                                   "id_article": menu.article1.id_article})
                        res = cursor.fetchone()
                if res :
                    update_article1 = True            
                            
            if menu.article2.id_article not in res : 
                update_article2 = False
                ArticleDao.ArticleDao.add_article(article = menu.article2)
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "DELETE FROM ensaeats.table_menu_article " 
                            "WHERE id_menu=%(id_menu)s AND id_article = %(id_article)s;"
                            , {"id_menu" : menu.id_menu, 
                            "id_article" : menu.article2.id_article})
                        
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                                " id_article) VALUES "\
                                    "(%(id_menu)s, %(id_article)s)"\
                                        "RETURNING id_menu;"
                                        , {"id_menu" : menu.id_menu,
                                        "id_article": menu.article2.id_article})
                        res = cursor.fetchone()
                    if res :
                        update_article2 = True        

                
            if menu.article3.id_article not in res : 
                update_article3 = False
                ArticleDao.ArticleDao.add_article(article = menu.article3)
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "DELETE FROM ensaeats.table_menu_article " 
                                "WHERE id_menu=%(id_menu)s AND id_article = %(id_article)s;"
                                , {"id_menu" : menu.id_menu, 
                                "id_article" : menu.article3.id_article})
                
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :       
                        cursor.execute(
                            "INSERT INTO ensaeats.table_menu_article (id_menu,"\
                                " id_article) VALUES "\
                                "(%(id_menu)s, %(id_article)s)"\
                                        "RETURNING id_menu;"
                                          , {"id_menu" : menu.id_menu,
                                        "id_article": menu.article3.id_article})
                        res = cursor.fetchone()
                    if res :
                        update_article3 = True    
                        return updated_menu,update_article1,update_article2,update_article3

                    

      