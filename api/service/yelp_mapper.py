from app.model.location import Location
from app.model.restaurant import Restaurant


class YelpMapper:

    @staticmethod
    def businesses_to_restaurants(response) -> Restaurant:
        # transforme le json en objet metier
        liste_restaurant =[]
        liste_businesses = response['businesses']
        for business in liste_businesses:
            nom = ""
            id = ""
            location = ""
            adresse = YelpMapper.yelp_location_to_location(location)
            restaurant = Restaurant()
            liste_restaurant.append(restaurant)
        return liste_restaurant

    @staticmethod
    def yelp_location_to_location(response) -> Adresse :
        # transforme en objet adresse 
        raise NotImplementedError
