from api.service.yelp_api_service import YelpApiService
from api.service.yelp_mapper import YelpMapper
from api.metier.restaurant import Restaurant
from api.metier.article import Article
from api.metier.menu import Menu 
from api.dao.article_dao import ArticleDao
from api.dao.menu_dao import MenuDao
from typing import List
from api.exception.restaurant_pas_trouve import RestaurantPasTrouveException
from api.exception.restaurants_pas_trouves import RestaurantsPasTrouvesException


class RestaurantsService:

    @staticmethod
    def getRestaurants(location: str, term: str = '', radius : int = 3000) -> List[Restaurant]:
        response = YelpApiService.get_businesses(location, term, radius) # recupere les infos de l'API de yelp
        restaurants = []
        try :
            restaurants=YelpMapper.businesses_to_restaurants(response) # recupere une liste d'objets restaurant
            return restaurants
        except : 
            return restaurants
        
    @staticmethod
    def getRestaurant(id: str) -> Restaurant:
        response = YelpApiService.get_business_by_id(id)
        try : 
            restaurant = YelpMapper.business_to_restaurant(response)
            return restaurant
        except : 
            raise RestaurantPasTrouveException(id_restaurant=id)
        
    @staticmethod
    def getMenus_by_id_restaurant(id_restaurant : str) -> List[Menu] :
        try : 
            RestaurantsService.getRestaurant(id_restaurant) # si cette méthode renvoie une exception 
            # c'est que l'identifiant du restaurant n'existe pas 
            return MenuDao.find_all_menus_by_id_restaurant(id_restaurant) # renvoie une liste vide si pas de menus
        except : 
            raise RestaurantPasTrouveException(id_restaurant=id)
        
    @staticmethod
    def addArticle(article : Article) -> Article :
        ''' Ajoute un article à la base de données des articles commun à tous '''
        return ArticleDao.add_article(article)

    @staticmethod
    def updateArticle(article : Article) -> Article:
        ''' Modifie un article à la base de données des articles commun à tous '''
        return ArticleDao.update_article(article)

    @staticmethod
    def deleteArticle(article : Article):
        ''' Modifie un article à la base de données des articles commun à tous '''
        return ArticleDao.delete_article(article)

    @staticmethod
    def addMenuOnRestaurant(id_restaurant: str, menu : Menu):
        return MenuDao.add_menu_by_id_restaurant(menu, id_restaurant)
    
    @staticmethod
    def updateMenuOnRestaurant(menu: Menu):
        return MenuDao.update_menu(menu) 

    @staticmethod
    def deleteMenuOnRestaurant(menu: Menu):
        # prend un menu en entrée 
        return MenuDao.delete_menu(menu)
