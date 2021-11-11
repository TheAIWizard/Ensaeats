from typing import List
from api.metier.restaurant import Restaurant
from brouillon.utils.singleton import Singleton
from brouillon.DAO.db_connection import DBConnection



class RestaurantDao(metaclass=Singleton):

    def find_id_restaurant_by_name(self, name : str)-> List:
        '''
        Get the id of a restaurant thanks to its name
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM ensaeats.restaurant "\
                    "\nWHERE restaurant.nom = %(name)s"
                    , {"name": name}
                )
                res = cursor.fetchone()
        if res:
            return res["nom", "id_restaurant"]


    def find_restaurant_by_id_restau(self, id_restaurant : str)-> List:
        '''
        Get the name of a restaurant thanks to its id
        
        '''
        with DBConnection().connection as connection:
            with connection.cursor() as cursor :
                cursor.execute(
                    "SELECT * " \
                    "\nFROM ensaeats.restaurant "\
                    "\nWHERE restaurant.id_restaurant = %(id_restaurant)s"
                    , {"id_restaurant": id_restaurant}
                )
                res = cursor.fetchone()
        if res:
            return res["nom", "id_restaurant"]
