from metier.restaurant import Restaurant
from metier.adresse import Adresse
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
    def yelp_location_to_location(location : dict) -> str :
        ''' Transforme en objet Adresse et renvoie en format str '''

        if location["address1"] is None : 
            adresse = ''
        else : 
            adresse = location["address1"]
        code_postal = location["zip_code"]
        pays = location["country"]
        ville = location["city"]
        localisation = Adresse(adresse, code_postal, ville, pays)

        # Permet de récuperer l adresse en format str 
        adresse = localisation.adresse + ' ' + localisation.code_postal + ' ' + localisation.ville + ' ' + localisation.pays
        return adresse
