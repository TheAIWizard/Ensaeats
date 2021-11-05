from API.metier.restaurant import Restaurant
from API.metier.adresse import Adresse
from typing import List

class YelpMapper:

    @staticmethod
    def businesses_to_restaurants(response) -> List[Restaurant]:
        # transforme le json en une liste d'objet metier
        liste_restaurant =[]
        liste_businesses = response['businesses']

        for business in liste_businesses:
            nom = business["name"]
            id = business["id"]
            location = business["location"]
            statut = business["is_closed"]
            adresse = YelpMapper.yelp_location_to_location(location)
            restaurant = Restaurant(id_restaurant = id , nom = nom , adresse = adresse, statut = statut)
            liste_restaurant.append(restaurant)
            
        return liste_restaurant

    @staticmethod
    def business_to_restaurant(response) -> Restaurant:
        # transforme le json en une liste d'objet metier
        nom = response["name"]
        id = response["id"]
        location = response["location"]
        statut = response["is_closed"]
        adresse = YelpMapper.yelp_location_to_location(location)
        restaurant = Restaurant(id_restaurant = id , nom = nom , adresse = adresse, statut = statut)
            
        return restaurant


    @staticmethod
    def yelp_location_to_location(location : dict) -> str :
        ''' Transforme en objet Adresse  '''

        if location["address1"] is None : 
            adresse = ''
        else : 
            adresse = location["address1"]
        code_postal = location["zip_code"]
        pays = location["country"]
        ville = location["city"]
        return Adresse(adresse = adresse, code_postal = code_postal, ville = ville, pays = pays)
