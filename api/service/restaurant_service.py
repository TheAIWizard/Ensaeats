from yelp_api import YelpApiService
from typing import List


class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(term, location, radius)
        restaurants = []
        restaurants.append(YelpMapper.buisness_to_restaurant(buisness)
                           for buisness in response.json()["buisnesses"])
        return restaurants

    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.getBuisness(id)
        restaurant = YelpMapper.buisness_to_restaurant(response.json())
        return restaurant

    @staticmethod
    def addMenuOnRestaurant(id_restaurant: str, menu: Menu):
        raise NotImplementedError

    @staticmethod
    def updateMenuOnRestaurant(id_restaurant: str, id_menu: str, menu):
        raise NotImplementedError

    @staticmethod
    def deleteMenuOnRestaurant(id_restaurant: str, id_menu: str):
        raise NotImplementedError
