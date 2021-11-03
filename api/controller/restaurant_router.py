from fastapi import APIRouter, Header, HTTPException
from API.metier.user import User
from API.service.user_service import UserService
from typing import Optional
from API.exception.user_not_authenticated_exception import UserNotAuthenticated
from API.service.restaurant_service import RestaurantsService
router = APIRouter()


@router.get("/restaurants/", tags=["restaurants"])
def get_restaurants(username: Optional[str] = Header(None), password: Optional[str] = Header(None), localisation:str="Bruz", term : str = "", radius : int = 2000):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurants(localisation, term, radius)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")


@router.get("/restaurant/{id_restaurant}")
async def get_restaurant(username: Optional[str] = Header(None), password: Optional[str] = Header(None), id_restaurant: str = ''):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.getRestaurant(id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")




@router.post("/restaurant", tags = ['POST'])
async def post_article(nom : str, composition : str, type: str, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.addArticle(nom, composition, type)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")



@router.post("/restaurant", tags = ['POST'])
async def post_menu(nom : str, id_restaurant : str, prix : str, id_article1: int, id_article2 : int, id_article3 : int, username: Optional[str] = Header(None), password: Optional[str] = Header(None)):
    try:
        # user = UserService.authenticate_and_get_user(
        #     username=username, password=password)
        # print(user)
        # # call your service here
        return RestaurantsService.addMenuOnRestaurant(nom, prix, id_article1, id_article2, id_article3, id_restaurant)

    except UserNotAuthenticated:
        raise HTTPException(status_code=401, detail="User must be logged")
