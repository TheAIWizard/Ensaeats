from api_minuscule.service.yelp_api_service import YelpApiService
from api_minuscule.service.yelp_mapper import YelpMapper
from api_minuscule.metier.restaurant import Restaurant
from api_minuscule.metier.article import Article
from api_minuscule.metier.menu import Menu 
from api_minuscule.dao.article_dao import ArticleDao
from api_minuscule.dao.menu_dao import MenuDao
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
    def getArticles() -> List[Article]:
        pass

    @staticmethod
    def getMenus_by_id_restaurant(id_restaurant : str) -> List[Menu] :
        return MenuDao.find_all_menus_by_id_restaurant(id_restaurant)
    
    @staticmethod
    def getMenus() :
        pass
        #return MenuDao.find_all_menus()
    
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
        ## Création des objets articles puis objet métier 
        return MenuDao.add_menu_by_id_restaurant(menu, id_restaurant)
    
    @staticmethod
    def updateMenuOnRestaurant(id_restaurant: str, id_menu: int, menu: Menu):
        ''' Prend en entrée l'identifiant de l'ancien menu si jamais celui ci est différent de celui ajouté'''
        return MenuDao.update_menu(id_restaurant, id_menu, menu) 

    @staticmethod
    def deleteMenuOnRestaurant(id_restaurant: str, id_menu: int):
        # prend un menu en entrée 
        return MenuDao.update_menu(id_restaurant, id_menu)