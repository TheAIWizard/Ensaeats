
from brouillon.DAO.db_connection import DBConnection
from brouillon.metier.commande import Commande

class CommandeDAO():
    inserted = False
    @staticmethod
    def add_commande(self, commande: Commande):
        """Ajout d'une commande dans la base de données
        """
        ## penser à tenir compte des id auto increment après
        requete = "INSERT INTO ensaeats.commande (id_commande, date, prix_total, statut_commande) VALUES "\
            "({}, '{}', {}, '{}') RETURNING id_commande".format(commande.id_commande, commande.date, commande.prix_total(), commande.statut_commande)
        
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(requete)
                res = cursor.fetchone()
                if res :
                    inserted = True
                return inserted
    
        ## Tenir compte du lien avec le client (Table_client_commande)
       
    