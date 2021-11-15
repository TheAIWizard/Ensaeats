from api_minuscule.service.restaurant_service import RestaurantsService

def selection(para_localite, para_nomRestaurant, para_radius):
    list = []
    if para_nomRestaurant =='' and para_radius =='':
        list = RestaurantsService.getRestaurants(location = para_localite) # Recherche avec location seulement
    elif para_nomRestaurant != '' and para_radius == '':
        list = RestaurantsService.getRestaurants(location = para_localite, term = para_nomRestaurant) # Avec location et nom
    elif para_nomRestaurant == '' and para_radius != '':
        list = RestaurantsService.getRestaurants(location= para_localite, radius= para_radius) # Location et rayon
    else :
        list = RestaurantsService.getRestaurants(location= para_localite, term = para_nomRestaurant, radius= para_radius)
    return list