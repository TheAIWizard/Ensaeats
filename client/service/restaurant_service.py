
import json
from fastapi import params
import requests
from requests.api import request

class RestaurantService:
    
    
    @staticmethod
    def getRestaurants(self, localite, term, radius, identifiant, mot_de_passe):
        #requête API pour obtenir les restaurants
        params_restaurants={'localisation':localite,'term': term,'radius':radius,'username': identifiant,'password': mot_de_passe}
        restaurants=requests.get('http://localhost:5000/restaurants/', params = params_restaurants).json()
        
        return restaurants
    
    
    @staticmethod
    def getMenus_By_Id_restaurant(self, id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get menus
        params_menus_by_id_restaurant={'id_restaurant':id_restaurant,'username': identifiant,'password': mot_de_passe}
        menus_by_id_restaurant=requests.get('http://localhost:5000/menus/{}'.format(id_restaurant),params=params_menus_by_id_restaurant).json()

        return menus_by_id_restaurant
    
    @staticmethod
    def getAvis_By_Id_Restaurant(self, id_restaurant, identifiant, mot_de_passe):
        # Requête vers api get avis
        params_avis_by_restaurant = {'id_restaurant': id_restaurant, 'username': identifiant, 'password': mot_de_passe}
        avis = request.get('http://localhost:5000/avis/{}'.format(id_restaurant), params = params_avis_by_restaurant).json()
        
        return avis
    
    
    ## Methode d'ajout
    @staticmethod
    def post_commande_by_id_restaurant(self, id_restaurant, identifiant, mot_de_passe, commande):
        output = False
        params_post_commande = {'id_restaurant': id_restaurant, 'username': identifiant, 'password': mot_de_passe}
        post_commande = request.post('http://localhost:5000/commande/{}'.format(id_restaurant),
                                     json = commande,
                                     params = params_post_commande)
        if post_commande: 
            output = True
            return output
        return output
    
       
        
        
        