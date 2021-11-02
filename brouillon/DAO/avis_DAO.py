from typing import List
from brouillon.metier.avis import Avis
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection



class AvisDao(metaclass=Singleton):

    def find_avis_by_id_restaurant(self, id_restau:int)-> List:
        '''
        Avoir tous les avis d'un restaurant
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM ensaeats.restaurant JOIN ensaeats.avis ON ensaeats.restaurant.id_restaurant = ensaeats.avis.id_restaurant  "\
                    "\nWHERE restaurant.id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restau}
                )
                res = cursor.fetchone()
        avis_restau = []
        if res :
            for row in res : 
                avis_restau.append(row["avis"])
        return avis_restau


    def add_avis(self, avis : Avis) -> bool:
        created = False

        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "INSERT INTO ensaeats.avis (id_menu, value) VALUES "\
                    "(%(id_menu)s, %(nom)s, %(prix)s)"\
                    "RETURNING id_menu;"
                , {"id_menu" : menu.id_menu
                  , "name": menu.nom_menu
                  , "prix": menu.prix_menu})
                res = cursor.fetchone()
        if res :
            menu.id=res['id_menu']
            created = True
        return created
