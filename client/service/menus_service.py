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
        """Permet d'obtenir les menus d'un restaurant

        Args:
            id_restaurant (str): identifiant du restaurant
            identifiant (str): L'identifiant de l'utilisateur
            mot_de_passe (str): Le mot de passe de l'utilisateur

        Returns:
            list: Liste de menus
        """
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
        """Afin de faire la requête d'insertion des commandes nous avons besoin
        de transformer les articles de chaque menu sous format dictionnaire.

        Args:
            menu ([type]): [description]

        Returns:
            dict: Dictionnaire menu dont les articles sont transformés en dictionnaie
        """
        menu_seri = Menu_serializable(
            id_menu = menu.id_menu,
            nom = menu.nom,
            prix = menu.prix,
            article1 = dict(menu.article1),
            article2 =dict(menu.article2) ,
            article3 = dict(menu.article3)
        )
        return dict(menu_seri)