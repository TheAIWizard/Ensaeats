from api.dao.db_connection import DBConnection
from api.metier.commande import Commande

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
                
    
    ## Lien avec restaurant