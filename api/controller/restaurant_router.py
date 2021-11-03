from fastapi import APIRouter, Header, HTTPException
from API.metier.user import User
from API.service.user_service import UserService
from typing import Optional
from API.exception.user_not_authenticated_exception import UserNotAuthenticated
from API.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from API.dao.article_dao import ArticleDao
from API.metier.article import Article
from API.metier.menu import Menu 

router = APIRouter()


@router.get("/restaurants/", tags=["Restaurants"])
def get_restaurants(username: Optional[str] = Header(None), password: Optional[str] = Header(None), localisation:str="Bruz", term : str = "", radius : int = 2000):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation, term, radius)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.get("/restaurant/{id_restaurant}", tags=["Restaurants"])
async def get_restaurant(username: Optional[str] = Header(None), password: Optional[str] = Header(None), id_restaurant: str = ''):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.post("/articles/", tags = ['Articles'])
async def post_article(nom : str, composition : str, type: str, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here

        # Création de l'objet article
        article = Article(nom, composition, type)

        return RestaurantsService.addArticle(article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")

@router.put("/articles/", tags = ['Articles'])
async def put_article(id_article : int, nom : str = None, composition : str = None, type: str = None, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    # l'idée serait de mettre en valeur par défaut la composition et le type de base de l'identifiant article
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here

        # Je récupère l'article de la base de données selon l'identifiant de l'article à modifier
        article = ArticleDao.find_article_by_id_article(id_article) 

        if nom is None : # si le restaurateur n'a pas modifié le nom on garde le même 
            nom = article.nom
        if composition is None : # si le restaurateur n'a pas modifié la composition on garde la même 
            composition = article.composition
        if type is None : # si le restaurateur n'a pas modifié le type on garde le même 
            type = article.type 

        article = Article(nom, composition, type)

        return RestaurantsService.updateArticle(id_article, article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.get("/menus/{id_restaurant}", tags=["Menus"])
async def get_menus_by_id_restaurant(id_restaurant: str , username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getMenus_by_id_restaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.post("/menus", tags = ['Menus'])
async def post_menu(id_restaurant : str, nom : str, prix : str, id_article1: int, id_article2 : int, id_article3 : int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here

         # Création des objets articles 
        article1 = ArticleDao.find_article_by_id_article(id_article1)
        article2 = ArticleDao.find_article_by_id_article(id_article2)
        article3 = ArticleDao.find_article_by_id_article(id_article3)

        # Création de l'objet Menu 
        menu = Menu(nom, prix, article1, article2, article3)

        return RestaurantsService.addMenuOnRestaurant(id_restaurant, menu)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.put("/menus", tags = ['Menus'])
async def put_menu(id_restaurant : str, id_menu : int, nom : str = None, prix : str =None , id_article1: int = None, id_article2 : int = None, id_article3 : int = None , username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        # Je récupère le menu à vouloir modifier 
        menu = MenuDao.find_menu_by_id_menu(id_menu)

        # Pour les éléments non modifiés je garde les valeurs de base 
        if nom is None : 
            nom = menu.nom
        if prix is None : 
            prix = menu.prix
        if id_article1 is None : 
            id_article1 = menu.article1
        if id_article2 is None : 
            id_article2 = menu.article2 
        if id_article3 is None : 
            id_article3 = menu.article3
        
        # Création des objets articles 
        article1 = ArticleDao.find_article_by_id_article(id_article1)
        article2 = ArticleDao.find_article_by_id_article(id_article2)
        article3 = ArticleDao.find_article_by_id_article(id_article3)

        # Création du nouveau menu 
        menu = Menu(nom, prix, article1, article2, article3)

        return RestaurantsService.updateMenuOnRestaurant(id_restaurant, id_menu, menu)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.delete("/menus", tags = ['Menus'])
async def delete_menu(id_restaurant : str, id_menu : int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        menu = MenuDao.find_menu_by_id_menu(id_menu) 
        return RestaurantsService.deleteMenuOnRestaurant(id_restaurant, menu)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")

