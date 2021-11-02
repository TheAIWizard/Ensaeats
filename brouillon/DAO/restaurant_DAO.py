from typing import List
from api.metier.restaurant import Restaurant
from utils.singleton import Singleton
from DAO.db_connection import DBConnection



class RestaurantDao(metaclass=Singleton):

    def find_restaurant_by_name(self, name:str)-> Restaurant:
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM ensaeats.restaurant JOIN ensaeats.avis ON ensaeats.restaurant.id_restaurant = ensaeats.avis.id_restaurant  "\
                    "\nWHERE restaurant.nom = %(name)s"
                    , {"name": name}
                )
                res = cursor.fetchone()


 