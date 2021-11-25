
import json
from fastapi import params
from psycopg2.extensions import STATUS_IN_TRANSACTION
import requests
from requests.api import request
from client.service.mapper import BusinessMapper


class RestaurantService:
    
    #Get restaurants
    @staticmethod
    def getRestaurants(localite, term, radius, identifiant, mot_de_passe):
        
        params_restaurants = {'localisation':localite,'term': term,
                            'radius':radius,'identifiant_client': identifiant,
                            'mot_de_passe_client': mot_de_passe}
        restaurants_json = requests.get('http://localhost:5000/restaurants/',
                                 params = params_restaurants).json()
        restaurants = BusinessMapper.restaurant_mapper(restaurants_json)
        return restaurants
    
    
    
    
    
    
    
    
        
        
        