from Brouillon_Nikiema.yelp_api_service import YelpApiService
from typing import List
from api.metier.restaurant import Restaurant

class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(term, location, radius)
        restaurants = []
        restaurants.append(YelpMapper.businesses_to_restaurants(business)
                           for business in response.json()["businesses"])
        return restaurants

    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.getBusiness(id)
        restaurant = YelpMapper.businesses_to_restaurants(response.json())
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
