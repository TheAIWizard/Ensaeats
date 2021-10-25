from app.model.location import Location
from app.model.restaurant import Restaurant


class YelpMapper:

    @staticmethod
    def businesses_to_restaurants(response) -> list(Restaurant) :
        # transforme le json en objet metier
        liste_restaurant =[]
        liste_businesses = response['businesses']
        for business in liste_businesses:
            nom = business["name"]
            id = business["id"]
            location = business["location"]
            statut = business["is_closed"]
            adresse = YelpMapper.yelp_location_to_location(location)
            restaurant = Restaurant(id= id, nom = nom, location= adresse, statut = statut)
            liste_restaurant.append(restaurant)
        return liste_restaurant

    @staticmethod
    def yelp_location_to_location(location : dict) -> Adresse :
        # transforme en objet adresse 
        for elem in location : 
            adresse = elem['address1']
            code_postal = elem['zip_code']
            pays = elem['country']
            ville = elem['city']
            adresse = Adresse(adresse, code_postal, ville, pays)
        return adresse
