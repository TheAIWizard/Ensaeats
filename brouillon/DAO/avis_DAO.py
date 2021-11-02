from typing import List
# from api.metier.avis import Avis
from utils.singleton import Singleton
from DAO.db_connection import DBConnection



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

