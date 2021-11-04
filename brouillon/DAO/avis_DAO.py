from typing import List
from brouillon.metier.avis import Avis
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection

 

class AvisDao(metaclass=Singleton):

    def find_avis_by_id_restaurant(self, id_restau : int)-> List:
        '''
        Avoir tous les avis d'un restaurant
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM  ensaeats.avis   "\
                    "\nWHERE restaurant.id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restau}
                )
                res = cursor.fetchone()
        avis_restau = []
        if res :
            for row in res : 
                avis_restau.append(row["avis"])
        return avis_restau


    def add_avis(self, avis : Avis, id_restau : int, nom_auteur : str) -> bool: 
        '''
        Ajouter un avis sur un restaurant
        
        '''
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.avis (id_avis, avis, nom_auteur, id_restaurant) VALUES "\
                    "(%(id_avis)s, %(avis)s, %(nom_auteur)s, %(id_restaurant)s)"\
                    "RETURNING id_avis;"
                , {"id_avis" : avis.id_avis
                  , "avis": avis.avis
                  , "nom_auteur" : avis.nom_auteur
                  , "id_restaurant": id_restau})
                res = cursor.fetchone()
        if res :
            created = True
        return created
