import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request
from client.service.mapper import BusinessMapper


class AvisService:
    
    
    # Get avis
    @staticmethod
    def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {'id_restaurant': id_restaurant, 'identifiant_client': identifiant,
         'mot_de_passe_client': mot_de_passe}
        avis_json = requests.get('http://localhost:5000/avis/', params = params_avis_by_restaurant).json()
        avis = BusinessMapper.avis_mapper(avis_json)
        return avis
    
    # Post Avis
    @staticmethod
    def post_avis_by_id_restaurant(identifiant, mot_de_passe, avis):
        output = False
        param_avis_post = {'identifiant_client': identifiant,
                           'mot_de_passe_client': mot_de_passe}
        post_avis = requests.post('http://localhost:5000/avis/', 
                                 json = dict(avis),
                                 params = param_avis_post).json()
        
        if post_avis:
            output = True
            return output
        return output