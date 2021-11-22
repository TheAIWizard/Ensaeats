from fastapi import APIRouter, Header, HTTPException
from api.metier.user import User
from api.service.restaurateur_service import RestaurateurService
from typing import Optional
from api.exception.user_not_authenticated_exception import UserNotAuthenticated
from api.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from api.dao.article_dao import ArticleDao
from api.metier.article import Article
from api.metier.menu import Menu 
from api.service.client_service import ClientService

router = APIRouter()


@router.get("/restaurants/", tags=["Restaurants"])
async def get_restaurants(username: Optional[str] = Header(None), password: Optional[str] = Header(None), localisation:str="Bruz", term : str = "", radius : int = 2000):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=username, mot_de_passe=password)
        print(client)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation, term, radius)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="Vous devez vous connecter ou créer un compte en tant que client")


@router.get("/restaurant/{id_restaurant}", tags=["Restaurants"])
async def get_restaurant(username: Optional[str] = Header(None), password: Optional[str] = Header(None), id_restaurant: str = ''):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=username, mot_de_passe=password)
        print(client)
        # # call your service here
        return RestaurantsService.getRestaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="Vous devez vous connecter ou créer un compte en tant que client")



@router.get("/menus/{id_restaurant}", tags=["Menus"])
async def get_menus_by_id_restaurant(id_restaurant: str , username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        client = ClientService.authenticate_and_get_client(identifiant=username, mot_de_passe=password)
        print(client)
        # # call your service here
        return RestaurantsService.getMenus_by_id_restaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="Vous devez vous connecter ou créer un compte en tant que client")





