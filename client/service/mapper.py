from client.business.restaurant import Restaurant
from client.business.avis import Avis
from client.business.menu import Menu
from client.business.client import Client

class BusinessMapper:
    
    @staticmethod
    def avis_mapper(avis_json):
        list_avis = []
        for element in avis_json:
            avis_metier = Avis(avis = element["avis"], identifiant_auteur = element["identifiant_auteur"],
                               date = element['date'], id_restaurant = element['id_restaurant'])
            
            list_avis.append(avis_metier)
        
        return list_avis
    
    
    @staticmethod
    def menus_mapper(menu_json):
        liste_menus = []
        
        for element in menu_json:
            menus_metier = Menu(id_menu = element['id_menu'],
                                nom = element['nom'],
                                prix = element['prix'],
                                article1 = element['article1'],
                                article2 = element['article2'],
                                article3 = element['article3'])
            liste_menus.append(menus_metier)
        return liste_menus
    
    
    @staticmethod
    def restaurant_mapper(restaurant_json):
        liste_restaurant = []
        for element in restaurant_json:
            restaurant_metier = Restaurant(id_restaurant = element['id_restaurant'],
                                           nom = element['nom'],
                                           adresse = element['adresse'],
                                           statut = element['statut'])
            liste_restaurant.append(restaurant_metier)
        return liste_restaurant
        
        
    @staticmethod
    def client_mapper(client_json):
        client_metier = Client(
            id_client = client_json['id_client'],
            nom = client_json['nom'],
            prenom = client_json['prenom'],
            adresse = client_json['adresse'],
            identifiant = client_json['identifiant'],
            mot_de_passe = client_json['mot_de_passe'],
            telephone = client_json['telephone']
        )

        return client_metier

