from client.service.restaurant_service import RestaurantService
from client.view.abstract_view import AbstractView

def selection(para_localite, para_nomRestaurant, para_radius, identifiant, mdp):
    list = []
    
    
    if para_nomRestaurant =='' and para_radius =='':
        list = RestaurantService.getRestaurants(localite = para_localite, term =None, radius = None, identifiant = identifiant, 
                                                mot_de_passe = mdp) # Recherche avec location seulement
    elif para_nomRestaurant != '' and para_radius == '':
        list = RestaurantService.getRestaurants(localite = para_localite, identifiant = identifiant, 
                                                mot_de_passe = mdp, term = para_nomRestaurant, radius = None) # Avec location et nom
    elif para_nomRestaurant == '' and para_radius != '':
        list = RestaurantService.getRestaurants(localite = para_localite, identifiant = identifiant, 
                                                mot_de_passe = mdp, radius= para_radius, term = None) # Location et rayon
    else :
        list = RestaurantService.getRestaurants(localite = para_localite, identifiant = identifiant, 
                                                mot_de_passe = mdp, term = para_nomRestaurant, radius= para_radius)
    return list