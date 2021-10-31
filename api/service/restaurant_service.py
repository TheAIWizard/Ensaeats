from service.yelp_api_service import YelpApiService
from service.yelp_mapper import YelpMapper
from metier.restaurant import Restaurant
from typing import List


class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(location, term, radius)
        restaurants = []
        restaurants.append(YelpMapper.businesses_to_restaurants(response))
        return restaurants

    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.getBusiness(id)
        restaurant = YelpMapper.businesses_to_restaurants(response.json())
        return restaurant

    @staticmethod
    def addMenuOnRestaurant(id_restaurant: str, id_article1, id_article2, id_article3 ):
        pass

    @staticmethod
    def updateMenuOnRestaurant(id_restaurant: str, id_menu: str, menu):
        pass

    @staticmethod
    def deleteMenuOnRestaurant(id_restaurant: str, id_menu: str):
        pass
