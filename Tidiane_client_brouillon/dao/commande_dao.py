from typing import List, Optional
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection
from Tidiane_client_brouillon.metier.panier import Panier

class CommandeDAO(metaclass=Singleton):
    inserted = False
   
    def add_commande(self, id_commande, panier: Panier, date_commande, statut_commande):
        """Ajout d'une commande dans la base de données
        """
        ## penser à tenir compte des id auto increment après
        requete = "INSERT INTO ensaeats.commande (id_commande, date, prix_total, statut_commande) VALUES "\
            "({}, '{}', {}, '{}') RETURNING id_commande".format(id_commande, date_commande, panier.calcul_total(), statut_commande)
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(requete)
                res = cursor.fetchone()
                if res :
                    inserted = True
                return inserted