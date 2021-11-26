import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from client.service.mapper import BusinessMapper
from client.business.menu_serializable import Menu_serializable
class MenusService:
    
    
    # Get menus
    @staticmethod
    def getMenus_By_Id_restaurant(id_restaurant, identifiant, mdp):
        # Requête vers api get menus
        headers = {
            'accept': 'application/json',
            'identifiant': identifiant,
            'mot-de-passe': mdp,
        }
        
        menus_json=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),headers= headers).json()
        menu_business = BusinessMapper.menus_mapper(menus_json)
        return menu_business
    
    
    @staticmethod
    def menu_to_menu_serializable(menu):
        menu_seri = Menu_serializable(
            id_menu = menu.id_menu,
            nom = menu.nom,
            prix = menu.prix,
            article1 = dict(menu.article1),
            article2 =dict(menu.article2) ,
            article3 = dict(menu.article3)
        )
        return dict(menu_seri)