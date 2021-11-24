import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request



class AvisService:
    
    
    # Get avis
    @staticmethod
    def getAvis_By_Id_Restaurant(id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {'id_restaurant': id_restaurant, 'username': identifiant, 'password': mot_de_passe}
        avis = request.get('http://localhost:5000/avis/{}'.format(id_restaurant), params = params_avis_by_restaurant).json()
        
        return avis
    
    # Post Avis
    @staticmethod
    def post_avis_by_id_restaurant(id_restaurant, identifiant, mot_de_passe, avis):
        output = False
        param_avis_post = {'id_restraurant': id_restaurant,
                           'username': identifiant,
                           'password': mot_de_passe}
        post_avis = request.post('http://localhost:5000/avis/{}'.format(id_restaurant), 
                                 json = dict(avis),
                                 params = param_avis_post)
        
        if post_avis:
            output = True
            return output
        return output