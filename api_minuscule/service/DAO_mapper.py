from api_minuscule.metier.restaurant import Restaurant
from typing import List
""" INUTIIILLLEEE"""
class DAOMapper:
    """ Classe pour convertir les objets json en métier (et inversement ?)"""
    
    @staticmethod
    def business_to_restaurateur(response) -> Restaurant:
        # transforme le json en une liste d'objet metier
        nom = response["nom"]
        prenom = response["prenom"]
        identifiant = response["identifiant"]
        mot_de_passe = response["mot_de_passe"]
        id_restaurant = response["id_restaurant"]
        restaurant= Restaurant(nom=nom,prenom=prenom,identifiant=identifiant,mot_de_passe=mot_de_passe,id_restaurant=id_restaurant)
            
        return restaurant
