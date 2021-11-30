
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
        """Requete d'obtention des restaurants

        Args:
            localite (str): Zone de recherche
            term (str): Nom restaurant ou spécialite
            radius (str): rayon
            identifiant (str): identifiant de l'utilisateur
            mot_de_passe (str): mot de passe de l'utilisateur

        Returns:
            [type]: [description]
        """
        
        params_restaurants = {'localisation':localite,'term': term,
                            'radius':radius,'identifiant_client': identifiant,
                            'mot_de_passe_client': mot_de_passe}
        restaurants_json = requests.get('http://localhost:5000/restaurants/',
                                 params = params_restaurants).json()
        restaurants = BusinessMapper.restaurant_mapper(restaurants_json)
        return restaurants
    
      
    
    
    
    
        
        
        