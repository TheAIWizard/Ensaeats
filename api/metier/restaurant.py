from API.metier.adresse import Adresse
import hashlib

class Restaurant():
    def __init__(self, id_restaurant : str, nom : str, adresse: Adresse, statut : bool): 
        self.id_restaurant = id_restaurant
        #on a le choix:
        #self.id_restaurant=int(hashlib.sha512(id_restaurant.encode("utf-8")).hexdigest(), 16) % (10 ** 8)
        #self.id_restaurant = self.id_restaurant_hash (plus élégant)
        self.nom = nom 
        self.adresse = adresse
        self.statut = statut
        # ou alors self.id_restaurant = self.id_restaurant_hash

    """ 
    L'API de YELP dispose d'un id pour chaque restaurant mais sous forme de chaine de caractere mélangeant des lettres et chiffres.
    Pour convertir ces id en entier, nous pouvons hacher id_restaurant sous forme de 8 digits
    """
    id_restaurant_hash= lambda self,id_restaurant:int(hashlib.sha512(id_restaurant.encode("utf-8")).hexdigest(), 16) % (10 ** 8)