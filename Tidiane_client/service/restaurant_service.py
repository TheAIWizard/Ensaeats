
import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request

class RestaurantService:
    
    #Get restaurants
    @staticmethod
    def getRestaurants(localite, term, radius, identifiant, mot_de_passe):
        
        params_restaurants={'localisation':localite,'term': term,'radius':radius,'username': identifiant,'password': mot_de_passe}
        restaurants=requests.get('http://localhost:5000/restaurants/', params = params_restaurants).json()
        
        return restaurants
    
    
    
    
    
    
    ## Methode d'ajout
    
    
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
    
    
        
        
        