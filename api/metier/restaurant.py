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
