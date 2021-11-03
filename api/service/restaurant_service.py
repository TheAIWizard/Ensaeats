from API.service.yelp_api_service import YelpApiService
from API.service.yelp_mapper import YelpMapper
from API.metier.restaurant import Restaurant
from API.metier.article import Article
from API.metier.menu import Menu 
from typing import List


class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(location, term, radius) # recupere les infos de l'API de yelp
        restaurants = []
        restaurants=YelpMapper.businesses_to_restaurants(response) # recupere une liste d'objets restaurant
        # info_restaurants = []
        # for restaurant in restaurants : 
        #     res = [restaurant.id_restaurant, restaurant.nom, restaurant.adresse, restaurant.statut]
        #     info_restaurants.append(res)
        return restaurants

    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.get_business_by_id(id)
        restaurant = YelpMapper.business_to_restaurant(response)
        return restaurant

    @staticmethod
    def getArticle() -> List[Article]:
        pass

    @staticmethod
    def getMenus() -> List[Article]:
        pass
    
    @staticmethod
    def addArticle(nom : str, composition : str, type : str):
        ''' Ajoute un article à la base de données des articles commun à tous '''
        article = Article(nom , composition, type)
        #return API.dao.article_DAO.add_article(article)

    @staticmethod
    def addMenuOnRestaurant(id_restaurant: str, nom : str, prix : int, id_article1 : int, id_article2 : int , id_article3 : int):
        menu = Menu(nom, prix, id_article1, id_article2, id_article3)
        #return API.dao.article_DAO.add_menu(id_restaurant, menu)

    @staticmethod
    def updateMenuOnRestaurant(id_restaurant: str, id_menu: str, menu):
        pass

    @staticmethod
    def deleteMenuOnRestaurant(id_restaurant: str, id_menu: str):
        pass
