import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request

class MenusService:
    
    
    # Get menus
    @staticmethod
    def getMenus_By_Id_restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get menus
        params_menus_by_id_restaurant={'id_restaurant':id_restaurant,'username': identifiant,'password': mot_de_passe}
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()

        return menus_by_id_restaurant
    
    