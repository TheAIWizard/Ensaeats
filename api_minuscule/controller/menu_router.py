from fastapi import APIRouter, Header, HTTPException
from api_minuscule.metier.restaurateur import Restaurateur
from api_minuscule.service.restaurateur_service import RestaurateurService
from typing import Optional
from api_minuscule.exception.restaurateur_not_authenticated_exception import RestaurateurNotAuthenticated
from api_minuscule.service.restaurant_service import RestaurantsService
from brouillon.DAO.menu_DAO import MenuDao
from api_minuscule.dao.article_dao import ArticleDao
from api_minuscule.metier.article import Article
from api_minuscule.metier.menu import Menu 

router = APIRouter()

@router.get("/menus/{id_restaurant}", tags=["Menus"])
async def get_menus_by_id_restaurant(id_restaurant: str , identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     identifiant=identifiant, password=password)
        # print(restaurateur)
        # # call your service here

        return RestaurantsService.getMenus_by_id_restaurant(id_restaurant)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")



@router.post("/menus", tags = ['Menus'])
async def post_menu(id_restaurant : str, menu : Menu, identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     restaurateurname=identifiant, password=password)
        # print(restaurateur)
        # # call your service here
        RestaurantsService.addArticle(menu.article1)
        RestaurantsService.addArticle(menu.article2)
        RestaurantsService.addArticle(menu.article3)
        return RestaurantsService.addMenuOnRestaurant(id_restaurant, menu)

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")


@router.put("/menus/{id_menu}", tags = ['Menus'])
async def update_menu(id_menu : int, menu : Menu, identifiant: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # restaurateur = RestaurateurService.authenticate_and_get_restaurateur(
        #     restaurateurname=identifiant, password=password)
        # print(restaurateur)
        # # call your service here
        if id_menu == menu.id_menu : 
            return RestaurantsService.updateMenuOnRestaurant(menu)
        else : 
            raise HTTPException(stauts_code=401, detail = "Id has been changed")

    except RestaurateurNotAuthenticated:
        raise HTTPException(status_code=403, detail="Restaurateur must be logged")

