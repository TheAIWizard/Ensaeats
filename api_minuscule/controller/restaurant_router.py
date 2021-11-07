from fastapi import APIRouter, Header, HTTPException
from api_minuscule.metier.user import User
from api_minuscule.service.user_service import UserService
from typing import Optional
from api_minuscule.exception.user_not_authenticated_exception import UserNotAuthenticated
from api_minuscule.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from api_minuscule.dao.article_dao import ArticleDao
from api_minuscule.metier.article import Article
from api_minuscule.metier.menu import Menu 

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





