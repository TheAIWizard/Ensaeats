from service.yelp_api_service import YelpApiService
from service.yelp_mapper import YelpMapper
from metier.restaurant import Restaurant
from typing import List


class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(location, term, radius) # recupere les infos de l'API de yelp
        restaurants = []
        restaurants=YelpMapper.businesses_to_restaurants(response) # recupere une liste d'objets restaurant
        info_restaurants = []
        for restaurant in restaurants : 
            res = [restaurant.id_restaurant, restaurant.nom, restaurant.adresse, restaurant.statut]
            info_restaurants.append(res)
        return info_restaurants

    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.getBusiness(id)
        restaurant = YelpMapper.businesses_to_restaurants(response.json())
        return restaurant

    @staticmethod
    def addArticleOnRestaurant(id_restaurant: str, nom : str, description : str, type : str):
        pass


    @staticmethod
    def addMenuOnRestaurant(id_restaurant: str, id_article1, id_article2, id_article3 ):
        pass

    @staticmethod
    def updateMenuOnRestaurant(id_restaurant: str, id_menu: str, menu):
        pass

    @staticmethod
    def deleteMenuOnRestaurant(id_restaurant: str, id_menu: str):
        pass
