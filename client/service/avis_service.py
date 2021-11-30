import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request
from client.service.mapper import BusinessMapper


class AvisService:
    """[Cette classe contient les méthodes permettant d'obtenire les avis concernant un restaurant
    ou de donner son avis par rapport à ce dernier.]

    
        
    """
    
    # Get avis
    @staticmethod
    def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        """Méthode de recupération des avis

        Args:
            id_restaurant ([str]): [L'identifiant du restaurant]
            identifiant ([str]): [L'identifiant de l'utilisateur]
            mot_de_passe ([str]): [Le mot de passe de l'utilisateur]

        Returns:
            [List]: [Liste d'avis]
        """
        # Requête vers api get avis
        headers_avis = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
        params_avis_by_restaurant = {
            'id_restaurant': id_restaurant, 
            'identifiant': identifiant,
            'mot_de_passe': mot_de_passe
         }
        avis_json = requests.get('http://localhost:5000/avis/',
                                 params = params_avis_by_restaurant,
                                 headers = headers_avis).json()
        avis = BusinessMapper.avis_mapper(avis_json)
        return avis
    
    # Post Avis
    @staticmethod
    def post_avis_by_id_restaurant(identifiant, mot_de_passe, avis):
        """[summary]

        Args:
            identifiant ([str]): [L'identifiant de l'utilisateur]
            mot_de_passe ([str]): [Le mot de passe de l'utilisateur]
            avis ([Avis]): [L'avis de l'utilisateur sur le restaurant]

        Returns:
            [Bool]: [Booleen montrant si l'ajout est fait]
        """
        headers_avis = {
        'accept': 'application/json',
        'Content-Type': 'application/json'}
        param_avis_post = {
            'identifiant_client': identifiant,
            'mot_de_passe_client': mot_de_passe
            }
        post_avis = requests.post('http://localhost:5000/avis/', 
                                 json = dict(avis),
                                 params = param_avis_post,
                                 headers= headers_avis)
        
        if post_avis.status_code == 200:
            return True
        else:
            return False