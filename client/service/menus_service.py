import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from client.service.mapper import BusinessMapper

class MenusService:
    
    
    # Get menus
    @staticmethod
    def getMenus_By_Id_restaurant(id_restaurant):
        # Requête vers api get menus
        params_menus_by_id_restaurant={'id_restaurant':id_restaurant}
        menus_json = requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()
        
        menus = BusinessMapper.menus_mapper(menus_json)
        return menus
    
    