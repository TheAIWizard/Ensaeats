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
async def post_article(article : Article, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here

        # Création de l'objet article

        return RestaurantsService.addArticle(article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")


@router.put("/articles/{id_article}", tags = ['Articles'])
async def put_article(id_article : int, article:Article, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    # l'idée serait de mettre en valeur par défaut la composition et le type de base de l'identifiant article
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        if id_article == article.id_article : 
            return RestaurantsService.updateArticle(article = article)
        else : 
            raise HTTPException(stauts_code=401, detail = "Id has been changed")

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")

@router.delete("/articles/", tags = ['Articles'])
async def delete_article(id_article : int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        article = ArticleDao.find_article_by_id_article(id_article) 
        return RestaurantsService.deleteArticle(article)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")



@router.get("/menus/{id_restaurant}", tags=["Menus"])
async def get_menus_by_id_restaurant(id_restaurant: str , username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getMenus_by_id_restaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")



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
        raise HTTPException(status_code=403, detail="User must be logged")



