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
async def post_menu(id_restaurant : str, menu : Menu, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        RestaurantsService.addArticle(menu.article1)
        RestaurantsService.addArticle(menu.article2)
        RestaurantsService.addArticle(menu.article3),
        return RestaurantsService.addMenuOnRestaurant(id_restaurant, menu)

    except UserNotAuthenticated:
        raise HTTPException(status_code=403, detail="User must be logged")