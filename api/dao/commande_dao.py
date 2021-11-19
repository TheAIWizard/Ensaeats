
from api.dao.db_connection import DBConnection
from api.metier.commande import Commande
from api.metier.restaurant import Restaurant
from api.metier.restaurateur import Restaurateur
from api.metier.client import Client
from api.dao.menu_dao import MenuDao
from api.metier.menu import Menu

class CommandeDAO():
    inserted = False
    @staticmethod
    def add_commande(commande: Commande):
        """Ajout d'une commande dans la base de données
        """
       
        requete = "INSERT INTO ensaeats.commande (date, prix_total, statut_commande) VALUES "\
            "('{}', {}, '{}') RETURNING id_commande".format(commande.date, commande.prix_total(), commande.statut_commande)
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(requete)
                res = cursor.fetchone()
                if res :
                    return res['id_commande']
                
    
    ## Lien entre commande et menus
    def lien_commande_menus(commande: Commande, id_commande):
        list_id_menus = [menu.id_menu for menu in commande.liste_menu]

        ## Insertion dans la table commande_menu
        for id_menu in list_id_menus:
            requete = "INSERT INTO ensaeats.table_menu_commande (id_menu, id_commande) VALUES ({}, {}) "\
            "RETURNING id".format(id_menu, id_commande)
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(requete)
                    res = cursor.fetchone()
                    if res :
                        return res
        

        ## Tenir compte du lien avec le client (Table_client_commande)
       
    def lien_commande_client(id_client, id_commande):
        requete = "INSERT INTO ensaeats.table_client_commande (id_commande, id_client) VALUES"\
            "({}, {})".format(id_commande, id_client)
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(requete)
                
    @staticmethod 
    def obtenir_menus_par_id_commande(id_commande : int): 
        request = "SELECT * FROM ensaeats.menu "\
                  "JOIN ensaeats.table_menu_commande USING(id_menu) "\
                  "WHERE table_menu_commande.id_commande=%(id_commande)s;"

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    request,
                    {"id_commande": id_commande}
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
    def obtenir_commandes(client : Client) : 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_commande FROM ensaeats.table_client_commande"\
                    " WHERE id_client = %(id_client)s ;"
                , {"id_client" : client.id_client})
                res = cursor.fetchall()
                
        if res : 
            commandes=[]
            for r in res:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor :
                        cursor.execute(
                            "SELECT * FROM ensaeats.commande"\
                            " WHERE id_commande = %(id_commande)s;"
                        , {"id_commande" : r["id_commande"]})
                        res = cursor.fetchone()
                        commande = Commande(id_commande = res['id_commande'] , 
                                            date = res['date'] , 
                                            statut_commande = res['statut_commande'], 
                                            liste_menu= CommandeDAO.obtenir_menus_par_id_commande(r["id_commande"]),
                                            liste_quantite = res['liste_quantite'])
                commandes.append(commande)
        else : 
            return 'Le client ne possède pas de commandes'


    @staticmethod
    def obtenir_commandes_restaurant(restaurant : Restaurant) : 
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT id_commande FROM table_restaurant_commande"\
                    "WHERE id_restaurant = %(id_restaurant)s;"
                , {"id_client" : restaurant.id_restaurant})
                res = cursor.fetchall()
                
        if res : 
            with DBConnection().connection as connection:
                with connection.cursor() as cursor :
                    cursor.execute(
                        "SELECT * FROM commande"\
                        "WHERE id_commande in %(id_commande)s;"
                    , {"id_commande" : res})
                    res = cursor.fetchall()
                if res : 
                    return res
        else : 
            return 'Le restaurant ne possède pas de commandes'
                