from fastapi import APIRouter, Header, HTTPException
from api.metier.user import User
from api.service.user_service import UserService
from typing import Optional
from api.exception.user_not_authenticated_exception import UserNotAuthenticated
from api.service.restaurant_service import RestaurantsService
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
